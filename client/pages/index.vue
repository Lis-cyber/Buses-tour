<template>
  <v-app>
    <div class="text-box">
      <h1>Buses Tour</h1>
      <p class="mt-3">
        Te ayudamos a elegir la mejor ruta a tus sueños... Viajar es vivir!
      </p>      
      <v-btn
        @click.stop="miniVariant = !miniVariant"
        color="primary"
        elevation="2"
        :to="{ name: 'Buses' }"
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
      title: "Inspire",
      to: "/buses",
    };
  },
};
</script>

<style>
.v-application--wrap {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.6),
      rgba(0, 0, 0, 0.2)
    ),
    url("../static/banner.jpg");
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box h1 {
  font-size: 5rem;
  font-weight: 400;
  font-family: "Source Sans Pro", sans-serif;
}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
