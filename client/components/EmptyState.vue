<template>
  <v-card class="elevation-4 empty-card">
    <div :style="{ backgroundImage: `url(${image})` }" class="empty-img" ></div>
    <div class="empty-text">
      <h1>Aún no existen registros de {{ this.labels.title }}</h1>
      <h2>Tips:</h2>
      <template v-for="(item, i) in labels.tips">
        <li v-bind:key="i" style="padding-left: 1rem">
          {{ item }}
        </li>
      </template>
      <div style="display: flex; justify-content: end; margin-top: 4rem">
        <div style="text-align: end">
          <v-btn
            :to="this.labels.step_path"
            class="mx-2 my-2 emp-btn"
            color="secondary"
            icon
            large
          >
            Ir a {{ this.labels.prev_step }}
            <v-icon x-large style="justify-content: left">
              mdi-arrow-right-bold-box
            </v-icon>
          </v-btn>
        </div>
      </div>
    </div>
  </v-card>
</template>

<script>
export default {
  props: {
    imageName: String,
    labels: Object,
  },
  data: () => ({
    image: "",
  }),
  created() {
    this.image = "/_nuxt/static/" + this.labels.image
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bellota:wght@700&display=swap");

.empty-card {
  padding: 2rem;
  margin: auto;
  display: flex;
  justify-content: center;
  text-align: -webkit-center;
}
.empty-img {
  background-image: url("../static/pax.jpg");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  width: 50vh;
  height: 50vh;
}
.empty-text {
  padding-left: 2rem;
  text-align: -webkit-left;
  font-family: "Bellota", cursive;
}
.empty-text h1 {
  font-size: x-large;
  font-weight: bolder;
  margin-bottom: 2rem;
}
.emp-btn {
  justify-content: end;
  font-size: 1.1rem;
}
</style>
