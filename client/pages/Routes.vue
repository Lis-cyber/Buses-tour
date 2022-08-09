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
  error: "",
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
    },
    customHeaders: [
      { text: "ID", value: "id", align: "start", sortable: true, edit: false, show: false},
      { text: "Nombre", value: "name", edit: true, show: true },
      { text: "Bus", value: "assigned_bus", edit: true, show: true },
      { text: "Fecha Inicio", value: "start_date", edit: true, show: true, type: "date" },
      { text: "Fecha Fin", value: "end_date", edit: true, show: true, type: "date" },
      { text: "Acciones", value: "actions", width: "13%", edit: false, show: false},
    ],
    routes: [],
    buses: [],
  }),
  mounted() {
    API.service.init();
    this.getRoutes();
    this.getBuses();
  },
  methods: {
    async getBuses() {
      const { data, error } = await API.getAllItems(`buses/`);
      if (error) {
        this.error = error;
      } else {
        this.buses = data;
      }
    },
    async getRoutes() {
      const { data, error } = await API.getAllItems(`routes/`);
      if (error) {
        this.error = error;
      } else {
        this.routes = data;
      }
    },
    async deleteById(id) {
      const { error } = await API.deleteItem(this.labels.path, id);
      if (error) {
        this.error = error;
      } else {
        await this.getRoutes();
      }
    },
    async createEdit(item, id = null) {
      if (id) {
        const { error } = await API.putItem(this.labels.path, id, item);
        if (error) {
          this.error = error;
        } else {
          await this.getRoutes();
        }
      } else {
        const { error } = await API.postItem(this.labels.path, item);
        if (error) {
          this.error = error;
        } else {
          await this.getRoutes();
        }
      }
    },
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
