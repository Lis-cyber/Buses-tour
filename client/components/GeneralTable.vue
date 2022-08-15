<template>
  <v-card class="elevation-0" style="padding: 2rem">
    <v-card-title>
      <div class="list-title">Listado de {{ this.labels.title }}</div>
      <v-spacer></v-spacer>
      <v-text-field
        v-if="dataTable.length > 0"
        v-model="search"
        append-icon="mdi-magnify"
        label="Buscar"
        single-line
        style="width: 0%"
      ></v-text-field>
      <template v-if="this.labels.title == 'Pasajeros'">
        <v-btn
          color="primary"          
          class="mb-2 ml-5"
          :disabled="validate"
          @click="addPaasanger(null, true)"
        >
          Generar Boleto
        </v-btn>
      </template>
      <template v-else>
        <v-btn
          color="primary"          
          class="mb-2 ml-5"
          :disabled="validate"
          @click="addEditItem(null, true)"
        >
          Agregar
        </v-btn>
      </template>
    </v-card-title>

    <div v-if="dialog">
      <AddEditDialog
        v-model="dialog"
        :action="this.action"
        :close="close"
        :item="this.item"
        :labels="this.labels"
        :customHeaders="this.customHeaders"
        :drivers="this.drivers"
        :buses="this.buses"
        :schedules="this.schedules"
        @onFinish="save"
      />
    </div>
    <div v-if="dialogDelete">
      <DeleteDialog
        v-model="dialogDelete"
        :close="closeDelete"
        :item="this.item"
        :labels="this.labels"
        :routes="this.routes"
        @onFinish="deleteItemConfirm"
      />
    </div>
    <div v-if="dialogTicket">
      <BuyTicket
        :buses="this.buses"
        :routes="this.routes"
        :close="closeTicket"
        @onFinish="printed"
      />
    </div>

    <EmptyState v-if="dataTable.length === 0 && !loading" :labels="this.labels" />

    <ErrorState
      v-if="error"
      :labels="this.labels"
      :error="this.error"
      :close="onCloseError"
    />

    <template v-if="loading && dataTable.length === 0">
      <div class="text-center">
        <v-progress-circular
          :size="80"
          :width="8"
          color="#216ea5"
          indeterminate
        ></v-progress-circular>
      </div>
    </template>
    

    <v-data-table
      v-if="dataTable.length > 0"
      no-data-text="No hay información disponible"
      :headers="headers"
      :items="dataTable"
      :items-per-page="5"
      :search="search"
      :single-expand="true"
      :expanded.sync="expanded"
      :show-expand="showExpand"
      class="elevation-3"
      style="padding: 1rem"
    >
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          class="mr-4 icons"
          small
          :close="close"
          :save="save"
          @click="addEditItem(item, false)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          class="icons"
          small
          @click="deleteItem(item)"
          v-model="item.actions"
        >
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:expanded-item="{ item }">
        <td
          :colspan="headers.length + 1"
          style="height: 2rem !important; padding: 0 9rem"
        >
          <v-simple-table>
            <thead class="second-table-h">
              <tr>
                <th>Bus</th>
                <th>Horario</th>
                <th>Tickets Sold</th>
                <th>Pax Cant.</th>
                <th>
                  <v-text-field
                    v-model="num_pct"
                    min="0"
                    max="100"
                    type="number"
                    label="More than"
                    small
                  ></v-text-field>
                </th>
        
              </tr>
            </thead>
            <tbody class="second-table-b">
              <tr v-for="(bus, index) in item.assigned_buses" :key="index">
                <template v-if="bus.pax_pct.length * 10 >= num_pct">
                  <td>{{ bus.bus.name }}</td>
                  <td>{{ bus.schedule }}</td>
                  <td>{{ bus.pax_pct.length * 10 }}%</td>
                  <td>{{ bus.pax_num }} pax</td>
                </template>
              </tr>
            </tbody>
          </v-simple-table>
        </td>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  props: {
    labels: Object,
    dataTable: Array,
    customHeaders: Array,
    deleteById: Function,
    createEdit: Function,
    drivers: Array,
    buses: Array,
    routes: Array,
    schedules: Array,
    error: String,
    loading: Boolean
  },
  data: () => ({
    num_pct: 0,
    search: "",
    dialog: false,
    dialogError: false,
    dialogDelete: false,
    dialogTicket: false,
    headers: [],
    action: "",
    item: {},
    expanded: [],
    showExpand: false,
  }),
  watch: {
    dialogDelete(item) {
      item || this.closeDelete();
    },
  },
  created() {
    this.initialize();
  },
  methods: {
    initialize() {
      this.headers = this.customHeaders.filter((item) => item.show);
      if (this.customHeaders[0].expanded) {
        this.showExpand = true;
      } else {
        this.showExpand = false;
      }
    },

    addEditItem(item, action) {
      this.item = Object.assign({}, item);
      this.dialog = true;
      if (action) {
        this.action = "Agregar";
      } else {
        this.action = "Editar";
      }
    },
    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.item = Object.assign({});
      });
    },
    save(item) {
      this.createEdit(item, item.id);
      this.close(true);
    },
    // Delete ------
    deleteItem(item) {
      if(item.onRoute || item.pax_num > 0){
        this.$emit("displayError");
      } else {
        this.item = Object.assign({}, item);
        this.dialogDelete = true;
      }
    },
    deleteItemConfirm(id, route = false) {
      this.deleteById(id, route);
      this.closeDelete();
    },
    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.item = Object.assign({});
      });
    },
    closeTicket(){
      this.dialogTicket = false
      this.$emit("onGetPax");
    },
    addPaasanger(item, action) {
      this.dialogTicket = true;
      if (action) {
        this.action = {
          title: "Agregar",
        };
      } else {
        this.action = {
          title: "Editar",
        };
      }
    },
    printed(item, routes) {
      this.createEdit(item, false, routes);
      this.dialogTicket = false;
    },
    onCloseError() {
      this.$emit("onError");
    },
  },
  computed: {
    validate: {
      get() {
        if(this.labels.title == 'Trayectos' && this.buses.length === 0){
          return true
        }
        if(this.labels.title == 'Buses' && this.drivers.length === 0){
          return true
        }
        if(this.labels.title == 'Pasajeros' && this.routes.length === 0){
          return true
        }
      },
    },
  }
};
</script>
<style>
.v-card__title {
  padding: 0 0 1rem;
  font-family: "Muli", sans-serif !important;
}
.icons {
  cursor: pointer;
}
.v-card__actions {
  justify-content: flex-end;
}
.v-data-table
  > .v-data-table__wrapper
  tbody
  tr.v-data-table__expanded__content {
  box-shadow: none;
}
.v-data-table > .v-data-table__wrapper > table > thead > tr > th {
  background-color: #fdecd9;
  font-size: 1.1rem;
  font-variant: petite-caps;
}
.second-table-h > tr > th {
  background-color: #d2faf9 !important;
  font-size: 0.9rem !important;
  height: 2rem;
}
.second-table-b > tr > td {
  font-size: 0.8rem !important;
}
.list-title {
  font-variant: petite-caps;
  color: darkorange;
  font-size: 1.5rem;
  text-decoration: underline;
}
.text-center {
  z-index: 999;
  text-align: center !important;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0%;
  left: 0%;
  background-color: #5656565e;
}
.v-progress-circular {
  margin: 1rem;
  margin-top: 18%;
}

</style>
