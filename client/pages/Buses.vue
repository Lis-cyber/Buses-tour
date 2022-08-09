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
  error: "",
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
    },
    customHeaders: [
      { text: "ID", value: "id", align: "start", sortable: true, edit: false, show: false},
      { text: "Nombre", value: "name", edit: true, show: true },
      { text: "Conductor", value: "driver.full_name" , edit: true, show: true },
      { text: "Capacidad", value: "capacity", edit: true, show: true },
      { text: "Acciones", value: "actions", width: "13%", edit: false, show: false},
    ],
    buses: [],
    drivers: [],
  }),
  mounted() {
    API.service.init();
    this.getBuses();
  },
  methods: {
    async getBuses() {
      const { data, error } = await API.getAllItems(`buses/`);
      if (error) {
        this.error = error;
      } else {
        const arr = Array(24 * 4).fill(0).map((_, i) => { return ('0' + ~~(i / 4) + ': 0' + 60  * (i / 4 % 1)).replace(/\d(\d\d)/g, '$1') });
        // console.log("Arr: ", arr)
        this.buses = data;
        this.getDrivers();
      }
    },
    async getDrivers() {
      const { data, error } = await API.getAllItems(`drivers/`);
      if (error) {
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
      }
    },
    async deleteById(id) {
      const { error } = await API.deleteItem(this.labels.path, id);
      if (error) {
        this.error = error;
      } else {
        await this.getBuses();
      }
    },
    async createEdit(item, id = null) {
      if (id) {
        const { error } = await API.putItem(this.labels.path, id, item);
        if (error) {
          this.error = error;
        } else {
          await this.getBuses();
        }
      } else {
        const { error } = await API.postItem(this.labels.path, item);
        if (error) {
          this.error = error;
        } else {
          await this.getBuses();
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
