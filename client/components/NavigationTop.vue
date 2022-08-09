<template>
  <div class="row">
    <template v-if="windowWidth > 1000 && windowHeight > 300">
      <v-app-bar outlined elevation="6" light>
        <template>
          <v-tab><NuxtLink to="/Routes">Trayectos</NuxtLink></v-tab>
          <v-tab><NuxtLink to="/Buses">Buses</NuxtLink></v-tab>
          <v-tab><NuxtLink to="/Drivers">Conductores</NuxtLink></v-tab>
          <v-tab><NuxtLink to="/Passengers">Pasajeros</NuxtLink></v-tab>
        </template>
      </v-app-bar>
    </template>
    <template v-else>
      <div>
        <v-app-bar dense color="green" light>
          <template v-slot:extension>
            <v-tab>Home</v-tab>
          </template>
        </v-app-bar>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  data() {
    return {
      windowWidth: window?.innerWidth,
      windowHeight: window?.innerHeight,
    };
  },
  async mounted() {
    this.$nextTick(() => {
      window?.addEventListener("resize", this.onResize);
    });
  },
  methods: {
    onResize() {
      this.windowWidth = window?.innerWidth;
      this.windowHeight = window?.innerHeight;
    },
  },
};
</script>
<style>
.v-application a {
  color: black;
  font-size: 1.2rem;
  font-family: "Muli", sans-serif !important;
  font-feature-settings: "smcp";
  letter-spacing: 0ch;
  font-variant: small-caps;
  text-decoration: none;
  text-transform: none;
}
.row {
  margin: 0px;
}
.v-toolbar__content,
.v-toolbar__extension {
  background-color: #37878662;
}
a.nuxt-link-active {
  font-weight: bold;
}
a.nuxt-link-exact-active {
  color: #c5b800;
}
</style>
