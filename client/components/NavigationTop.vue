<template>
  <div class="row">
    <template v-if="windowWidth > 1000 && windowHeight > 300">
      <v-app-bar
        color="white"
        dark
        prominent
        shrink-on-scroll
        fade-img-on-scroll
        outlined
        elevation="8"
      >
        <template>
          <v-tabs style="margin-left: 0.1rem">
            <v-tab to="/Drivers">Conductores</v-tab>
            <v-tab to="/Buses">Buses</v-tab>
            <v-tab to="/Routes">Trayectos</v-tab>
            <v-tab to="/Passengers">Pasajeros</v-tab>
          </v-tabs>
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
.row {
  margin: 0px;
}
.v-application a {
  font-size: 1.2rem;
  font-family: "Muli", sans-serif !important;
  font-feature-settings: "smcp";
  letter-spacing: 0ch;
  font-variant: small-caps;
  text-decoration: none;
  text-transform: none;
}
.v-tab--active {
  font-weight: bold;
}
.v-tab.v-tab {
  color: #fb8c00;
}
.theme--dark.v-tabs > .v-tabs-bar .v-tab:not(.v-tab--active) {
  color: #383e56;
}
.theme--dark.v-app-bar.v-toolbar.v-sheet {
  background-image: url("../static/dots2.jpg");
  background-repeat: no-repeat;
  background-position: left center;
  background-size: cover;
  width: 100%;
}
</style>
