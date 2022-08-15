<template>
  <v-app class="init">
    <div class="text-box">
      <div class="logo"></div>
      <h1>Buses Tour</h1>
      <p class="mt-3">
        Te ayudamos a elegir la mejor ruta a tus sueños... Viajar es vivir!
      </p>
      <p class="text-adm">Bienvenido al Administrador</p>
      <v-btn
        @click.stop="miniVariant = !miniVariant"
        color="primary"
        elevation="2"
        :to="{ name: 'Drivers' }"
      >
        Ingresar
      </v-btn>
    </div>
  </v-app>
</template>

<script>
export default {
  name: "HomePage",
  head() {
    return {
      title: "Home page",
      icon: "mdi-chart-bubble",
      title: "Home",
      to: "/buses",
    };
  },
  data() {
    return {
      logo: this?.window?.innerWidth > 1000 ? "8rem" : "4rem",
      size: this?.window?.innerWidth > 1000 ? "5rem" : "3rem",
      windowWidth: this?.window?.innerWidth,
      windowHeight: this?.window?.innerHeight,
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

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bellota:wght@700&display=swap");
.text-box {
  position: absolute;
  top: 45%;
  left: 7%;
  transform: translateY(-50%);
  color: rgb(0, 0, 0);
  width: 35%;
}
.text-box h1 {
  font-size: v-bind('size');
  font-family: "Bellota", cursive;
}
.text-box p {
  font-size: 1.5rem;
  font-weight: lighter;
}
.text-adm {
  margin-top: 4rem;
  font-weight: bold;
  font-family: monospace;
}
.logo {
  background-image: url("../static/bus.png");
  background-repeat: no-repeat;
  background-position: left center;
  background-size: contain;
  height: v-bind('logo');
}
.init {
  background-image: url("../static/init-page.jpg");
  background-repeat: no-repeat;
  background-position: left center;
  background-size: cover;
  width: 100%;
}
</style>
