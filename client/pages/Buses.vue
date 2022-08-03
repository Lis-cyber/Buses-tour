<template>
  <v-app>
    <div class="container">
      <NavigationTop />
      <GeneralTable />
    </div>
  </v-app>
</template>

<script>
export default {
  name: "Buses",
  layout: "main",
  scrollToTop: true,
    head() {
    return {
      title: "Buses page",
      icon: "mdi-chart-bubble",
      title: "Buses",
      to: "/buses",
    };
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
