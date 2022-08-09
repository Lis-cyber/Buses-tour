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
  error: "",
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
    },
    customHeaders: [
      { text: "ID", value: "id", align: "start", sortable: true, edit: false, show: false},
      { text: "Nombre", value: "name", edit: true, show: true },
      { text: "Apellido", value: "last_name", edit: true, show: true },
      { text: "Ruta", value: "route", edit: false, show: true },
      { text: "Acciones", value: "actions", width: "13%", edit: false, show: false},
    ],
    passengers: [],
  }),
  mounted() {
    API.service.init();
    this.getPassengers();
  },
  methods: {
    async getPassengers() {
      const { data, error } = await API.getAllItems(`passengers/`);
      if (error) {
        this.error = error;
      } else {
        this.passengers = data;
      }
    },
    async deleteById(id) {
      const { error } = await API.deleteItem(this.labels.path, id);
      if (error) {
        this.error = error;
      } else {
        await this.getPassengers();
      }
    },
    async createEdit(item, id = null) {
      if (id) {
        const { error } = await API.putItem(this.labels.path, id, item);
        if (error) {
          this.error = error;
        } else {
          await this.getPassengers();
        }
      } else {
        const { error } = await API.postItem(this.labels.path, item);
        if (error) {
          this.error = error;
        } else {
          await this.getPassengers();
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
