<template>
  <v-dialog v-model="dialogError" max-width="500px" persistent>
    <v-card class="elevation-4 error-card">
      <div class="empty-img"></div>
      <v-card-title class="text-h5">Opss ocurrió un error!</v-card-title>
      <v-card-text> {{ this.error }}. Contacta a soporte para más información.</v-card-text>
      <v-card-actions>
        <v-btn
          color="primary"
          class="ma-2"
          outlined
          elevation="2"
          @click="close"
          >Cerrar</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    close: Function,
    error: String,
    labels: Object,
  },
  data: () => ({
    dialogError: true,
  }),
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bellota:wght@700&display=swap");
.error-card {
  padding: 2rem;
  margin: auto;
  display: block;
  justify-content: center;
  text-align: -webkit-center;
}
.empty-img {
  background-image: url("../static/error.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  width: 50vh;
  height: 50vh;
}
</style>
