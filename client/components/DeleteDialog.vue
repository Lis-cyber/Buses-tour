<template>
  <v-dialog class="dialogStyle" v-model="dialogDelete" max-width="500px" persistent>
    <v-card>
      <v-card-title class="text-h5"
        >Eliminar {{ this.labels.subTitle }}</v-card-title
      >
      <v-card-text
        >¿Estás seguro que deseas eliminar el {{ this.labels.subTitle }}
        {{ this.item.name }}?</v-card-text
      >
      <v-card-actions>
        <v-btn
          color="primary"
          class="ma-2"
          outlined
          elevation="2"
          @click="close"
          >Cancelar</v-btn
        >
        <v-btn color="primary" elevation="2" @click="onFinish()">Eliminar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    close: Function,
    item: Object,
    labels: Object,
    routes: Array
  },
  data: () => ({
    dialogDelete: true,
    filteredRoutes: []
  }),
  mounted() {
    this.filteredRoutes = this.routes
  },
  methods: {
    onFinish() {
      if(this.labels.subTitle === "Pasajero"){
        this.filteredRoutes = this.filteredRoutes.filter((data) => {
          if(data.id === this.item.route.id){
            return data 
          }
        })
        this.filteredRoutes[0].pax_num = this.filteredRoutes[0].pax_num - 1
        this.filteredRoutes[0].pax_pct =  Math.round((this.filteredRoutes[0].pax_num * 100) / (this.filteredRoutes[0].assigned_buses.length * 10))
        this.filteredRoutes[0].assigned_buses.map((bus) =>{
          if(bus.id === this.item.route.assigned_buses[0].id){            
            bus.pax_num = bus.pax_num-1 
            bus.pax_pct = bus.pax_pct.filter(i => i !== this.item.seat)
            return bus 
          } else {
            return bus
          }
        })

        this.$emit("onFinish", this.item.id, this.filteredRoutes[0]);
      } else {
        this.$emit("onFinish", this.item.id);
      }
    },
  },
};
</script>
