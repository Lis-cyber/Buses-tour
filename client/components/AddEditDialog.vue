<template>
  <v-dialog class="dialogStyle" v-model="dialog" max-width="500px" persistent>
    <v-card>
      <v-card-title class="text-h5"
        >{{ this.action }} {{ this.labels.subTitle }}</v-card-title
      >
      <v-card-text style="padding: 0">
        <v-container>
          <v-row>
            <template v-for="field in this.customHeaders">
              <v-col
                style="margin-bottom: -2rem"
                v-if="field.edit && (field.text.includes('Bus') || field.text === 'Conductor')"
                v-bind:key="field.text"
                cols="12"
                :sm="field.col || 6"
                :md="field.col || 6"
              >
                <v-select
                  v-if="field.text.includes('Bus')"
                  outlined
                  dense
                  v-model="selectBus"
                  v-bind:label="field.text"
                  :items="filterBuses"
                  item-text="name"
                  return-object
                >
                  <template slot="selection" slot-scope="data">
                    {{ data.item.name }}
                  </template>
                  <template slot="item" slot-scope="data">
                    {{ data.item.name }}
                  </template>
                </v-select>
                <v-select
                  v-else
                  outlined
                  dense
                  v-model="edit['driver']"
                  v-bind:label="field.text"
                  :items="filterDrivers"
                  item-text="name"
                  return-object
                >
                  <template slot="selection" slot-scope="data">
                    {{ data.item.name }} {{ data.item.last_name }}
                  </template>
                  <template slot="item" slot-scope="data">
                    {{ data.item.name }} {{ data.item.last_name }}
                  </template>
                </v-select>
              </v-col>
              <v-col
                style="display: flex; margin-bottom: -2rem"
                v-else-if="field.edit && field.text === 'Horario'"
                v-bind:key="field.text"
                cols="12"
                :sm="field.col || 6"
                :md="field.col || 6"
              >
                <v-select
                  outlined
                  dense
                  v-model="selectSchedule"
                  v-bind:label="field.text"
                  :items="filterSchedules"
                >
                </v-select>               
                <v-btn
                  style="margin-left: 1rem !important;"
                  class="mx-2"
                  color="primary"
                  x-small
                  fab
                  :disabled="!add"
                  @click="addBus"
                >
                  <v-icon dark> mdi-plus </v-icon>
                </v-btn>
              </v-col>
              <v-col
                style="margin-bottom: -2rem"
                v-else-if="field.edit"
                v-bind:key="field.text"
                cols="12"
                :sm="field.col || 6"
                :md="field.col || 6"
              >
                <v-text-field
                  outlined
                  dense
                  v-bind:label="field.text"
                  v-model="edit[field.value]"
                ></v-text-field>
              </v-col>
            </template>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-text v-if="this.vias.length > 0" style="padding: 0">
        <v-container>
          <v-divider style="margin: 0 12px"></v-divider>
          <template v-for="(route, index) in this.vias">
            <v-row v-bind:key="index">
              <v-col style="padding-bottom: 0" cols="12" :sm="4" :md="4">
                {{ route.schedule }}
              </v-col>
              <v-col style="padding-bottom: 0" cols="12" :sm="7" :md="7">
                {{ route.bus.name }}
              </v-col>
              <v-col style="padding-bottom: 0" cols="12" :sm="1" :md="1">                
                <v-btn :disabled="route.pax_num > 0 ? true : false" @click="deleteBus(route.id)" style="margin: 0px !important;" icon class="mx-1" color="primary" x-small>
                  <v-icon end dark> mdi-cancel </v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </template>
        </v-container>
      </v-card-text>

      <v-card-actions style="padding: 12px 24px">
        <v-btn
          color="primary"
          class="ma-2"
          outlined
          elevation="2"
          @click="onClose()"
          >Cancelar</v-btn
        >
        <v-btn color="primary" elevation="2" :disabled="validate" @click="onFinish()">Guardar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  props: {
    close: Function,
    item: Object,
    action: String,
    labels: Object,
    customHeaders: Array,
    drivers: Array,
    buses: Array,
    schedules: Array,
  },
  data: () => ({
    dialog: true,
    edit: {},
    vias: [],
    filterBuses: [],
    filterSchedules: [],
    filterDrivers: [],
    add: false,
  }),
  mounted() {
    this.filterBuses = this.buses
    this.filterSchedules = this.schedules
    this.filterDrivers = this.drivers
    this.edit = this.item;
    if (this.edit.driver) {
      this.drivers.push(this.edit.driver);
    }
    if(this.edit.assigned_buses){
      this.vias = this.edit.assigned_buses
    }
  },
  methods: {
    onClose() {
      if(this.action ==="Editar" && this.edit.driver){
        this.drivers.pop();
      }
      this.close()
    },
    onFinish() {
      if(this.labels.subTitle === "Trayecto"){
        const route = {
          name: this.edit.name,
          pax_pct: 0,
          pax_num: 0,
          assigned_buses: this.vias
        }
        if(this.edit.id){
          route["id"] = this.edit.id
        }
        this.$emit("onFinish", route);
      } else if(this.labels.subTitle === "Bus"){
        this.edit['capacity'] = 10
        this.$emit("onFinish", this.edit);
      } else {
        this.$emit("onFinish", this.edit);
      }
    },
    addBus() {
      const test = { id: this.vias.length + 1, bus: this.edit.bus, schedule: this.edit.schedule, pax_pct: [], pax_num: 0 };
      this.vias = [...this.vias, test];
      this.filterBuses = this.buses
      this.filterSchedules = this.filterSchedules.filter(item => item !== this.edit.schedule )
      this.edit.schedule= ""
      this.add = false
    },
    deleteBus(id) {      
      this.vias = this.vias.filter(item => item.id !== id)
    },
  },
  computed: {
    selectBus: {
      get() {
        return this.buses;
      },
      set(value) {
        this.edit.bus = value;
        if(this.edit.schedule){
          this.add = true
        }
      },
    },
    selectSchedule: {
      get() {
        return this.edit.schedule;
      },
      set(value) {
        this.edit.schedule = value;
        if(this.edit.bus){
          this.add = true
        }
      },
    },
    validate: {
      get() {
        if(this.edit.name && this.edit.last_name){
          return false
        } else if(this.edit.name && this.edit.driver){
          return false
        } else if(this.edit.name && this.vias.length > 0){
          return false
        } else {
          return true
        }
      },
    }
  },
};
</script>