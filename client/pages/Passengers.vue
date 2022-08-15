<template>
  <v-app>
    <div class="container">
      <NavigationTop />
      <GeneralTable
        :labels="this.labels"
        :dataTable="this.passengers"
        :customHeaders="this.customHeaders"
        :deleteById="this.deleteById"
        :createEdit="this.createEdit"
        :buses="this.buses"
        :schedules="this.schedules"
        :routes="this.routes"
        :error="this.error"
        @onError="cleanError()"
        @onGetPax="getPassengers()"
        :loading="this.loading"
      />     
    </div>
  </v-app>
</template>

<script>
import * as API from "@/http/api";

export default {
  name: "Passengers",
  layout: "main",
  scrollToTop: true,
  head() {
    return {
      title: "Passengers",
      icon: "mdi-chart-bubble",
      to: "/passengers",
    };
  },
  data: () => ({
    labels: {
      title: "Pasajeros",
      subTitle: "Pasajero",
      path: "passengers",
      tips: ["Recuerda que para emitir un Ticket debes completar previamente el Trayecto", "Recuerda tener a mano, los datos del pasajero para completar el registro"],
      prev_step: "Trayectos",
      step_path: "/Routes",
      image: "pax.jpg"     
    },
    customHeaders: [
      { text: "ID", value: "id", align: "start", sortable: true, edit: false, show: true},
      { text: "Nombre", value: "name", edit: true, show: true },
      { text: "Apellido", value: "last_name", edit: true, show: true },
      { text: "Asiento", value: "seat", edit: false, show: true },
      { text: "Ruta", value: "route.name", edit: false, show: true },
      { text: "Horario", value: "route.assigned_buses[0].schedule", edit: false, show: true },
      { text: "Acciones", value: "actions", width: "13%", edit: false, show: true},
    ],
    passengers: [],
    routes: [],
    buses: [],
    schedules: [],
    loading: false,
    error: "",
  }),
  mounted() {
    this.loading = true
    API.service.init();
    this.getPassengers();

  },
  methods: {
    async getPassengers() {
      const { data, error } = await API.getAllItems(`passengers/`);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        this.passengers = data;
        this.getBuses();
      }
    },
    async getBuses() {
      const { data, error } = await API.getAllItems(`buses/`);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        this.getRoutes();
        this.buses = data;
      }
    },
    async putBuses(item, id) {
      this.loading = true
      const { error } = await API.putItem(`buses`, id, item);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        await this.getBuses();
      }
    },
    async getRoutes() {
      const { data, error } = await API.getAllItems(`routes/`);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        this.routes = data;
        this.getSchedules();
      }
    },
    async putRoutes(item, id) {
      this.loading = true
      const { error } = await API.putItem(`routes`, id, item);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        await this.getRoutes();
      }
    },
    async getSchedules(){
      this.schedules = await API.getTimes();      
      this.loading = false
    },
    async deleteById(id, routes) {
      this.loading = true
      const { error } = await API.deleteItem(this.labels.path, id);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        await this.putRoutes(routes, routes.id)
        await this.getPassengers();
      }
    },
    async createEdit(item, id = null, routes = null) {
      this.loading = true
      if (id) {
        const { error } = await API.putItem(this.labels.path, id, item);
        if (error) {
          this.error = error;
          this.loading = false
        } else {
          await this.getPassengers();
        }
      } else {       
        const { error } = await API.postItem(this.labels.path, item);
        if (error) {
          this.error = error;
          this.loading = false
        } else {
          await this.putBuses(item.route.assigned_buses[0]?.bus, item.route.assigned_buses[0]?.bus.id)
          await this.putRoutes(routes, routes.id)
          await this.getPassengers();
        }
      }

    },
    cleanError(){
      this.error = ""
    }
  },
};
</script>

<style scoped>
.container {
  max-width: 100%;
  padding: 0%;
  height: 100%;
  background-color: white;
}
</style>
