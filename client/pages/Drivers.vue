<template>
  <v-app>
    <div class="container">
      <NavigationTop />
      <GeneralTable
        :labels="this.labels"
        :dataTable="this.drivers"
        :customHeaders="this.customHeaders"
        :deleteById="this.deleteById"
        :createEdit="this.createEdit"
        :error="this.error"
        @onError="cleanError()"
        :loading="this.loading"
      />
    </div>
  </v-app>
</template>

<script>
import * as API from "@/http/api";

export default {
  name: "Drivers",
  layout: "main",
  scrollToTop: true,
  test: {},
  head() {
    return {
      title: "Drivers",
      icon: "mdi-chart-bubble",
      to: "/drivers",
    };
  },
  data: () => ({
    labels: {
      title: "Conductores",
      subTitle: "Conductor",
      path: "drivers",
      tips: ["Recuerda tener a mano los datos del conductor para completar el registro"],
      prev_step: "Inicio",
      step_path: "/",
      image: "driver-form.jpg"
    },
    customHeaders: [
      { text: "ID", value: "id", align: "start", sortable: true, edit: false, show: true },
      { text: "Nombre", value: "name", edit: true, show: true },
      { text: "Apellido", value: "last_name", edit: true, show: true },
      { text: "Bus Asignado", value: "assigned_bus", edit: false, show: true },
      { text: "Acciones", value: "actions", width: "13%", edit: false, show: true },
    ],
    drivers: [],
    buses: [],
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
        let driver = []
        data.map((item) => {
          driver.push({
            id: item.driver.id,
            name: item.driver.name,
            last_name: item.driver.last_name,
            full_name: item.driver.full_name,
            assigned_bus: item.name,
          })
        })
        this.buses = driver 
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
            return val.id;
          })
        )]
        let driverDat = data.map((item) => {
          if(driversId.indexOf(item.id) !== -1){
            return this.buses[driversId.indexOf(item.id)]
          } else {
            item.assigned_bus = "Sin asignar"
            return item
          }
        })
        this.drivers = driverDat;
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
