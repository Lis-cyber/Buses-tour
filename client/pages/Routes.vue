<template>
  <v-app>
    <div class="container">
      <NavigationTop />
      <GeneralTable
        :labels="this.labels"
        :dataTable="this.routes"
        :customHeaders="this.customHeaders"
        :deleteById="this.deleteById"
        :createEdit="this.createEdit"
        :buses="this.buses"
        :schedules="this.schedules"
        :error="this.error"
        @onError="cleanError()"
        @displayError="displayError()"
        :loading="this.loading"
      />
    </div>
  </v-app>
</template>

<script>
import * as API from "@/http/api";

export default {
  name: "Routes",
  layout: "main",
  scrollToTop: true,
  head() {
    return {
      title: "Routes",
      icon: "mdi-chart-bubble",
      to: "/routes",
    };
  },
  data: () => ({
    labels: {
      title: "Trayectos",
      subTitle: "Trayecto",
      path: "routes",
      tips: ["Recuerda que para generar un trayecto debes completar previamente la carga de Buses"],
      prev_step: "Buses",
      step_path: "/Buses",
      image: "route.jpg"
    },
    id: 11,
    customHeaders: [
      { text: "ID", value: "id", align: "start", sortable: true, edit: false, show: true, expanded: true},
      { text: "Nombre", value: "name", edit: true, show: true, col: 12 },
      { text: "Buses", value: "assigned_buses.length", edit: true, show: false, col: 5},
      { text: "% Pax", value: "pax_pct", edit: false, show: true, col: 7},
      { text: "N° Pax", value: "pax_num", edit: false, show: true, col: 7},
      { text: "Horario", value: "schedule", edit: true, show: false, col: 7 },
      { text: "Acciones", value: "actions", width: "13%", edit: false, show: true},
    ],
    routes: [],
    buses: [],
    schedules: [],
    loading: false,
    error: "",
  }),
  mounted() {
    this.loading = true
    API.service.init();
    this.getRoutes();
  },
  methods: {
    async getBuses() {
      const { data, error } = await API.getAllItems(`buses/`);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        this.buses = data;
        this.getSchedules();
      }
    },
    async getRoutes() {
      const { data, error } = await API.getAllItems(`routes/`);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        this.routes = data;
        this.getBuses();
      }
    },
    async deleteById(id) {
      this.loading = true
      const { error } = await API.deleteItem(this.labels.path, id);
      if (error) {
        this.error = error;
        this.loading = false
      } else {
        await this.getRoutes();
      }
    },
    async createEdit(item, id = null) {
      this.loading = true
      if (id) {
        const { error } = await API.putItem(this.labels.path, id, item);
        if (error) {
          this.error = error;
          this.loading = false
        } else {
          await this.getRoutes();
        }
      } else {
        const { error } = await API.postItem(this.labels.path, item);
        if (error) {
          this.error = error;
          this.loading = false
        } else {
          await this.getRoutes();
        }
      }
    },
    async getSchedules(){
      this.schedules = await API.getTimes(); 
      this.loading = false     
    },
    cleanError(){
      this.error = ""
    },
    displayError(){
      this.error = "No puedes eliminar un Trayecto con buses asignados y/o tickets emitidos."
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
