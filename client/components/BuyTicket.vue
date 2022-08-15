<template>
  <v-dialog class="dialogStyle" v-model="dialogDelete" max-width="500px" persistent>
    <v-card>
      <template>
        <v-stepper v-model="e1">
          <v-stepper-header>
            <v-stepper-step :complete="e1 > 1" step="1"> Fecha </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step :complete="e1 > 2" step="2"> Buses </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step :complete="e1 > 3" step="3"> Asiento </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step :complete="e1 > 4" step="4"> Datos </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step :complete="e1 > 5" step="5">Ticket</v-stepper-step>
          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <v-card class="mb-8">
                <v-col class="label-col" cols="12" :sm="8" :md="8">
                  Seleccionar Ruta
                  <v-select :items="routes" v-model="selectRoute" return-object outlined dense >
                    <template slot="selection" slot-scope="data">
                      {{ data.item.name }}
                    </template>
                    <template slot="item" slot-scope="data">
                      {{ data.item.name }}
                    </template>
                  </v-select>
                </v-col>
                <v-col cols="12" :sm="8" :md="8">
                  Fecha de Viaje
                  <v-text-field
                    v-model="selectDate"
                    type="date"
                    :min="this.minDate" 
                    :max="this.maxDate" 
                    outlined
                    dense
                  />                 
                </v-col>
              </v-card>
              <div style="text-align: end">
                <v-btn color="primary" class="ma-2" outlined @click="close">Cancelar</v-btn>
                <v-btn :disabled="passenger.date && passenger.route.id ? false : true" @click="changeStep(2)" color="primary" >
                  Continuar
                </v-btn>
              </div>
            </v-stepper-content>

            <v-stepper-content step="2" style="overflow: visible">
              <template v-for="(item, index) in this.routeBuses">
                <v-card
                  v-bind:key="index"
                  outlined
                  :class="item.id === index_bus ? 'card-bus-select' : 'card-bus'">
                  <div class="image-bus"></div>
                  <v-list-item-content style="padding: 12px">
                    <div class="text-overline mb-4">
                      {{ passenger.route.name }}
                    </div>
                    <v-list-item-title class="text-h5 mb-1">
                      {{ item.bus.name }}
                    </v-list-item-title>
                    <v-list-item-subtitle>Horario: {{ item.schedule }}</v-list-item-subtitle>
                    <v-list-item-subtitle style="font-size: 0.7rem">
                      Disponibilidad: {{10 - item.pax_pct.length}} asientos</v-list-item-subtitle>
                  </v-list-item-content>
                  <v-btn icon class="mx-2 my-2" color="primary" small>
                    <v-icon @click="selectedBus(item, index)">
                      mdi-checkbox-marked-circle-plus-outline
                    </v-icon>
                  </v-btn>
                </v-card>
              </template>
              <div style="display: flex; justify-content: space-between;" >
                <v-btn icon class="mx-2 my-2" color="secondary" style="margin: 0 !important; justify-content: left;" large >
                  <v-icon @click="changeStep(1)" x-large style="justify-content: left;">
                    mdi-arrow-left-bold-box
                  </v-icon>
                </v-btn>
                <div style="text-align: end">
                  <v-btn color="primary" class="ma-2" outlined @click="close">Cancelar</v-btn>
                  <v-btn :disabled="passenger.route.assigned_buses.length == 1 ? false : true" @click="changeStep(3)" color="primary" >
                    Continuar
                  </v-btn>
                </div>
              </div>
            </v-stepper-content>

            <v-stepper-content step="3">
              <template>
                <v-card class="mb-12" style="display: flex">
                  <v-container class="grey lighten-5">
                    <v-row v-for="(i, index) in seats" :key="index">
                      <div class="seat-row">{{ index + 1 }}</div>
                      <template v-for="(j, a) in i">
                        <v-col :key="a" v-if="j !== '_'" class="px-1 py-0">
                          <v-card
                            v-if="passenger.route?.assigned_buses[0] &&
                              passenger.route?.assigned_buses[0]?.pax_pct?.indexOf( Number(j)) !== -1"
                            class="pa-1 my-0 seats"
                            :color="passenger.seat === j ? 'orange' : 'gray'"
                          >
                            <button style="cursor: auto">{{ j }}</button>
                          </v-card>
                          <button v-else @click="selectSeat(j)" class="pa-1 my-0 seats-up">
                            {{ j }}
                          </button>
                        </v-col>
                        <v-col v-else :key="a" class="pa-1 my-0">
                          <div v-if="index === 0 && a === 0" class="driver"></div>
                        </v-col>
                      </template>
                    </v-row>
                  </v-container>
                  <v-container>
                    <v-list-item-title class="text-h5 mb-1">
                      Detalle
                    </v-list-item-title>
                    <v-list-item-content>
                      <div class="text-overline mb-4">
                        Asiento: #{{ passenger.seat }}
                      </div>
                      <v-list-item-subtitle>Economy </v-list-item-subtitle>
                      <v-list-item-subtitle style="font-size: 0.7rem"
                        >Total a Pagar: 50 usd</v-list-item-subtitle
                      >
                    </v-list-item-content>
                  </v-container>
                </v-card>
              </template>
              <div style="display: flex; justify-content: space-between;" >
                <v-btn icon class="mx-2 my-2" color="secondary" style="margin: 0 !important; justify-content: left;" large >
                  <v-icon @click="changeStep(2)" x-large style="justify-content: left;">
                    mdi-arrow-left-bold-box
                  </v-icon>
                </v-btn>
                <div style="text-align: end">
                  <v-btn color="primary" class="ma-2" outlined @click="close">Cancelar</v-btn>
                  <v-btn color="primary" @click="changeStep(4)" :disabled="passenger.seat !== 0 ? false : true">
                    Continuar
                  </v-btn>
                </div>
              </div>
            </v-stepper-content>

            <v-stepper-content step="4">
              <v-card class="mb-12" height="12rem">
                <v-row>
                  <v-col v-model="name" class="label-col" cols="12" :sm="6" :md="6">
                    Nombre
                    <v-text-field type="text" outlined dense />
                  </v-col>
                  <v-col v-model="last_name" class="label-col" cols="12" :sm="6" :md="6">
                    Apellido
                    <v-text-field type="text" outlined dense />
                  </v-col>
                  <v-col v-model="email" :rule="validate.email" class="label-col" cols="12" :sm="6" :md="6">
                    Email
                    <v-text-field type="text" outlined dense />
                  </v-col>
                </v-row>
              </v-card>

              <div style="display: flex; justify-content: space-between;" >
                <v-btn icon class="mx-2 my-2" color="secondary" style="margin: 0 !important; justify-content: left;" large >
                  <v-icon @click="changeStep(3)" x-large style="justify-content: left;">
                    mdi-arrow-left-bold-box
                  </v-icon>
                </v-btn>
                <div style="text-align: end">
                  <v-btn color="primary" class="ma-2" outlined @click="close">Cancelar</v-btn>
                  <v-btn color="primary" @click="changeStep(5)"
                    :disabled="validate.name === true && validate.last_name === true && validate.email === true ? false : true ">
                    Continuar
                  </v-btn>
                </div>
              </div>
            </v-stepper-content>

            <v-stepper-content id="ticket" step="5">
              <v-card class="mb-12" height="300px" style="border-radius: 0.8rem">
                <div class="ticket-header">
                  <div class="ticket-header-img"></div>
                  <div class="ticket-header-text">Bus Ticket</div>
                </div>
                <div class="ticket-content">
                  <div class="ticket-content-img"></div>
                  <v-row class="content-row">
                    <v-col class="label-col" cols="12">
                      <v-text-field v-model="name" label="Nombre" dense disabled />
                    </v-col>
                    <v-col class="label-col" cols="12">
                      <v-text-field v-model="last_name" label="Apellido" dense disabled />
                    </v-col>
                    <v-col class="label-col" cols="12">
                      <v-text-field v-model="email" label="Email" dense disabled />
                    </v-col>
                  </v-row>
                  <v-row class="content-row print-ticket">
                    <v-col class="text-col" cols="12">
                      Fecha:<br />
                      {{ passenger.date }}
                    </v-col>
                    <v-col class="text-col" cols="12">
                      Asiento: {{ passenger.seat }}
                    </v-col>
                    <v-col class="text-col" cols="12">
                      Ruta: <br />
                      {{ passenger.route.name }}
                    </v-col>
                    <v-col class="text-col" cols="12">
                      Horario: <br />
                      {{ passenger.route?.assigned_buses[0]?.schedule }}
                    </v-col>
                  </v-row>
                </div>
                <div class="ticket-footer">Buses Tour Inc ©</div>
              </v-card>
              <div style="display: flex; justify-content: space-between;" >
                <v-btn icon class="mx-2 my-2" color="secondary" style="margin: 0 !important; justify-content: left;" large >
                  <v-icon @click="changeStep(4)" x-large style="justify-content: left;">
                    mdi-arrow-left-bold-box
                  </v-icon>
                </v-btn>
                <div style="text-align: end">
                  <div style="text-align: end">
                    <v-btn color="primary" class="ma-2" outlined @click="close">Cancelar</v-btn>
                    <v-btn color="primary" @click="download(passenger)">Finalizar</v-btn>
                  </div>
                </div>
              </div>          
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </template>
    </v-card>
  </v-dialog>
</template>

<script>
import html2canvas from "html2canvas";
import Validations from '~/rules/validations';

export default {
  props: {
    close: Function,
    item: Object,
    labels: Object,
    buses: Array,
    routes: Array,
  },
  data: () => ({
    dialogDelete: true,
    e1: 1,
    filterBuses: [],
    filterRoutes: [],
    seats: [
      ["_", "_", "_", 1, 2],
      [3, 4, "_", 5, 6],
      [7, 8, "_", 9, 10],
    ],
    routeBuses: [],
    passenger: {
      date: "",
      route: {
        id: "",
        name: "",
        pax_pct: "",
        assigned_buses: [],
      },
      seat: 0,
      name: "",
      last_name: "",
      email: "",
    },
    validate: {
      name: "",
      last_name: "",
      email: "",
    },
    minDate: new Date().toISOString().substr(0, 10),
    maxDate: "",
    index_bus: ""
  }),
  mounted() {
    this.filterBuses = this.buses;
    this.filterRoutes = this.routes;

    function addMonths(numOfMonths, date = new Date()) {
      date.setMonth(date.getMonth() + numOfMonths);
      return date;
    }
    this.maxDate = addMonths(1).toISOString().substr(0, 10)
  },
  methods: {
    onFinish() {
      this.$emit("onFinish");
    },
    selectedBus(item, index) {
      this.passenger.route.assigned_buses = [item];
      this.index_bus = item.id
    },
    changeStep(e) {
      this.e1 = e;
    },
    selectSeat(e) {
      if(this.passenger.seat == 0){
        this.passenger.seat = e;
        this.passenger.route.assigned_buses[0]?.pax_pct.push(e)
        this.passenger.route.assigned_buses[0].pax_num = this.passenger.route.assigned_buses[0]?.pax_num + 1
      } else {
        this.passenger.route.assigned_buses[0]?.pax_pct.pop()
        this.passenger.seat = e;
        this.passenger.route.assigned_buses[0]?.pax_pct.push(e)
      }
    },
    async download(item) {      
      let busesFilter = this.filterRoutes.filter((data) => {
        if(data.id === item.route.id){
          return data
        }
      })
      busesFilter[0].pax_num = busesFilter[0].pax_num + 1
      busesFilter[0].pax_pct =  Math.round((busesFilter[0].pax_num * 100) / (busesFilter[0].assigned_buses.length * 10))
      
      await html2canvas(document.querySelector("#ticket")).then(function (canvas) {
        document.querySelector("#ticket").appendChild(canvas);
        let baba = document.querySelector("canvas");
        baba.style.display = "none";
        baba.toBlob(function (blob) {
          const link = document.createElement("a");
          link.href = URL.createObjectURL(blob);
          link.download = `ticket-${item.name}-${item.last_name}`;
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          // window.open(URL.createObjectURL(blob), '_blank')
        });
      });
      this.$emit("onFinish", item, this.filterRoutes[0]);
    },
  },
  computed: {
    selectRoute: {
      get() {
        return this.routeBuses && this.passenger.route;
      },
      set(value) {
        this.routeBuses = value.assigned_buses;
        this.passenger.route.id = value.id;
        this.passenger.route.name = value.name;
        this.passenger.route.pax_pct = value.pax_pct;
      },
    },
    selectDate: {
      get() {
        return (this.passenger.date = new Date().toISOString().substr(0, 10));
      },
      set(value) {
        this.passenger.date = value;
      },
    },
    name: {
      get() {
        return this.passenger.name;
      },
      set(value) {
        this.validate.name = Validations.input_text_required[0](value.target.value)
        if(this.validate.name === true){
          this.passenger.name = value.target.value;
        }
      },
    },
    last_name: {
      get() {
        return this.passenger.last_name;
      },
      set(value) {
        this.validate.last_name = Validations.input_text_required[0](value.target.value)
        if(this.validate.last_name === true){
          this.passenger.last_name = value.target.value;
        }
      },
    },
    email: {
      get() {
        return this.passenger.email;
      },
      set(value) {
        this.validate.email = Validations.email[0](value.target.value)
        if(this.validate.email === true){
          this.passenger.email = value.target.value;
        }
      },
    },
  },
};
</script>
<style>
.v-stepper__header {
  flex-wrap: nowrap;
}
.v-stepper__header {
  font-size: 0.8rem;
}
.v-stepper__step__step {
  height: 20px;
  width: 20px;
  min-width: 20px;
}
.image-bus {
  background-image: url("../static/bus-avatar.jpg");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  width: 25%;
}
.seats {
  border-radius: 5px !important;
  background-color: #969696 !important ;
  color: #ffffff !important;
  cursor: pointer;
  text-align: center;
}
.seats-up {
  border-radius: 5px !important;
  background-color: #478f17 !important ;
  color: #ffffff !important;
  cursor: pointer;
  text-align: center;
  width: inherit;
}
.driver {
  background-image: url("../static/driver.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  position: absolute;
  width: 10%;
  height: 25%;
  left: 2.6rem;
  top: 0.5rem;
}
.seat-row {
  align-self: center;
  padding-right: 0.4rem;
}
.label-col {
  margin-bottom: -2rem;
}
.text-col {
  height: 2rem;
  padding: 0 0.5rem;
  font-size: 12px;
}
.ticket-header {
  display: flex;
  background-color: #ff9501;
  background-color: #ffb700;
  height: 3.5rem;
  padding: 0.5rem;
  color: white;
}
.ticket-header-text {
  align-self: center;
  font-size: 1.5rem;
  text-transform: uppercase;
}
.ticket-header-img {
  background-image: url("../static/bus-ticket.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  width: 15%;
  margin-right: 1rem;
}
.ticket-footer {
  display: flex;
  background-color: rgb(67 165 200 / 80%);
  height: 12%;
  padding: 0.5rem;
  color: #ffffff;
  justify-content: right;
}
.ticket-content {
  display: flex;
  height: 70%;
  z-index: 999;
}
.ticket-content-img {
  background-image: url("../static/barcode.gif");
  background-repeat: no-repeat;
  background-size: contain;
  opacity: 0.4;
  width: 10rem;
  margin: 1rem 0;
}
.print-ticket {
  width: 80%;
  font-size: smaller;
  border-left: dotted rgb(193, 193, 193);
  background-color: beige;
  margin-top: 0 !important;
}
.content-row {
  padding: 1rem 0;
}
.card-bus {
  margin-bottom: 1rem;
  display: flex;
}
.card-bus-select {
  margin-bottom: 1rem;
  display: flex;
  color: #fb8c00 !important;
}
</style>
