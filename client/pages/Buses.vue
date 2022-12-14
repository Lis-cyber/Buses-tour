<template>
  <v-app>
    <div class="container">
      <NavigationTop />
      <GeneralTable
        :labels="this.labels"
        :dataTable="this.buses"
        :customHeaders="this.customHeaders"
        :deleteById="this.deleteById"
        :createEdit="this.createEdit"
        :drivers="this.drivers"
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
  name: "Buses",
  layout: "main",
  scrollToTop: true,
  head() {
    return {
      title: "Buses",
      icon: "mdi-chart-bubble",
      to: "/buses",
    };
  },
  data: () => ({
    labels: {
      title: "Buses",
      subTitle: "Bus",
      path: "buses",
      tips: ["Recuerda que para registrar un Bus debes completar previamente el formulario de conductor"],
      prev_step: "Conductores",
      step_path: "/Drivers",
      image: "bus-asign.jpg"
    },
    customHeaders: [
      { text: "ID", value: "id", align: "start", sortable: true, edit: false, show: true},
      { text: "Nombre", value: "name", edit: true, show: true },
      { text: "Conductor", value: "driver.full_name" , edit: true, show: true },
      { text: "Cant. Asientos", value: "capacity", edit: false, show: true },
      { text: "Acciones", value: "actions", width: "13%", edit: false, show: true},
    ],
    buses: [],
    drivers: [],
    loading: false,
    error: "",
  }),
  mounted() {
    this.loading = true
    API.service.init();
    this.getBuses();
  },
  methods: {
    async getBuses() {
      const { data, error } = await API.getAllItems(`buses/`);
      if (error) {
        this.loading = false
        this.error = error;        
      } else {
        this.buses = data;
        this.getDrivers();
      }
    },
    async getDrivers() {
      const { data, error } = await API.getAllItems(`drivers/`);
      if (error) {
        this.loading = false
        this.error = error;        
      } else {
        const driversId = [...new Set(Object.values(this.buses)
          .map(function(val) {
            return val.driver.id;
          })
        )]
        const useDrivers = data.filter((item) => {
          if(!driversId.includes(item.id)){
            return item
          }
        })
        this.drivers = useDrivers;
        this.loading = false
      }
    },
    async deleteById(id) {
      this.loading = true
      const { error } = await API.deleteItem(this.labels.path, id);
      if (error) {
        this.loading = false
        this.error = error;        
      } else {
        await this.getBuses();
      }
    },
    async createEdit(item, id = null) {
      this.loading = true
      if (id) {
        const { error } = await API.putItem(this.labels.path, id, item);
        if (error) {
          this.loading = false
          this.error = error;          
        } else {
          await this.getBuses();
        }
      } else {
        const { error } = await API.postItem(this.labels.path, item);
        if (error) {
          this.loading = false
          this.error = error;          
        } else {
          await this.getBuses();
        }
      }
    },
    cleanError(){
      this.error = ""
    },
    displayError(){
      this.error = "No puedes eliminar un Bus asignado a un Trayecto"
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
