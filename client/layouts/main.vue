<template>
  <v-app class="main">
    <template v-if="windowWidth > 1000 && windowHeight > 300">
      <div class="main-control">
        <div class="main-control-logo"></div>
        <NuxtLink class="main-control-logoText" to="/">Buses Tour</NuxtLink>
        <div class="main-control-powered">
          <span style="font-weight: 600; font-size: 14px; color: white"
            >¿Necesitas ayuda?</span
          >
          <a href="mailto:ayuda@ayudita.cl">ayuda@ayudita.cl</a><br />
          <span>
            Powered by
            <span style="font-weight: bold; font-size: 18px; color: black"
              >Destácame</span
            >
          </span>
        </div>
      </div>
      <div class="main-body">
        <Nuxt />
      </div>
    </template>
    <template v-else>
      <div class="main-body-mobile">
        <Nuxt />
        <Navigatimainottom />
      </div>
    </template>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      windowWidth: 0,
      windowHeight: 0,
    };
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      this.windowWidth = window.innerWidth;
      this.windowHeight = window.innerHeight;
    },
  },
};
</script>

<style scoped>
.main {
  display: block;
  position: absolute;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
.main-control {
  background-image: url("../static/start.jpg");
  background-image: url("../static/sidebar.jpg");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  position: absolute;
  top: 0%;
  left: 0%;
  width: 25%;
  height: 100%;
  display: grid;
  grid-template-rows: 70px auto 70px;
  padding-top: 2%;
}
.main-body {
  background-color: #fff;
  position: absolute;
  top: 0%;
  left: 25%;
  width: 75%;
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
}
.main-body-mobile {
  background-color: #fff;
  position: fixed;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
}
.main-control-logo {
  background-image: url("../static/bus.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: contain;
}
.main-control-logoText {
  font-size: xxx-large;
  text-align: center;
  color: orange;
  font-weight: bolder;
  font-variant: small-caps;
  font-family: "Muli", sans-serif !important;
  text-decoration: none;
  text-shadow: rgb(255, 255, 255) 1px 2px 10px;
}
.main-control-powered {
  text-align: center;
  align-self: end;
  margin-bottom: 1rem;
  background-color: #37878585;
}
.main-control-powered span {
  font-weight: 300;
  width: 200px;
  font-size: 15px;
  color: white;
}
.main-control-powered a {
  color: black;
  font-weight: 600;
  font-size: 14px;
  text-decoration: none;
  text-transform: none;
  font-feature-settings: normal;
  font-variant: normal;
}
</style>
