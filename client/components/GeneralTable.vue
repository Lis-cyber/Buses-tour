<template>
  <v-card class="elevation-0" style="padding: 2rem">
    <v-card-title>
      <div>Listado de {{ this.labels.title }}</div>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Buscar"
        single-line
        style="width: 0%"
      ></v-text-field>
      <template>
        <v-btn
          color="primary"
          dark
          class="mb-2 ml-5"
          @click="addEditItem(null, true)"
        >
          Agregar
        </v-btn>
      </template>
    </v-card-title>

    <div v-if="dialog">
      <AddEditDialog
        v-model="dialog"
        :form="this.form"
        :close="close"
        :item="this.item"
        :labels="this.labels"
        :customHeaders="this.customHeaders"
        :drivers="this.drivers"
        :buses="this.buses"
        @onFinish="save"
      />
    </div>
    <div v-if="dialogDelete">
      <DeleteDialog
        v-model="dialogDelete"
        :close="closeDelete"
        :item="this.item"
        :labels="this.labels"
        @onFinish="deleteItemConfirm"
      />
    </div>

    <v-data-table
      no-data-text="No hay información disponible"
      :headers="headers"
      :items="dataTable"
      :items-per-page="5"
      :search="search"
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
  },
  data: () => ({
    search: "",
    dialog: false,
    dialogDelete: false,
    headers: [],
    form: {},
    item: {},
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
      this.headers = this.customHeaders;
    },

    addEditItem(item, action) {
      this.item = Object.assign({}, item);
      this.dialog = true;
      if (action) {
        this.form = {
          title: "Agregar",
        };
      } else {
        this.form = {
          title: "Editar",
        };
      }
    },
    close() {
      this.dialog = false;
      if (this.item.driver) {
        this.drivers.pop();
      }
      this.$nextTick(() => {
        this.item = Object.assign({});
      });
    },
    save(item) {
      this.createEdit(item, item.id);
      this.close();
    },
    // Delete ------
    deleteItem(item) {
      this.item = Object.assign({}, item);
      this.dialogDelete = true;
    },
    deleteItemConfirm(id) {
      this.deleteById(id);
      this.closeDelete();
    },
    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.item = Object.assign({});
      });
    },
  },
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
</style>
