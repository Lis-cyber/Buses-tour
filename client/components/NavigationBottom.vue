<template>
  <div class="row">
    <template v-if="windowWidth > 1000 && windowHeight > 300"
      ><div></div
    ></template>
    <template v-else>
      <div
        class="col test"
        style="
          display: flex !important;
          justify-content: center !important;
          padding-top: 0px;
        "
      >
        <span style="font-size: 12px; color: #3e3e42; margin-right: 10px"
          >© Destácame {{ year }}</span
        >&nbsp;

        <span style="font-size: 12px; color: #3e3e42">¿Necesitas ayuda?</span
        >&nbsp;
        <a
          style="
            font-weight: bold;
            text-decoration: none;
            font-size: 12px;
            color: #3743aa;
          "
          href="mailto:ayuda@ayudita.cl"
          >ayuda@ayudita.cl</a
        >
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
  computed: {
    year() {
      const date = new Date();
      return date.getFullYear();
    },
  },
};
</script>
<style>
.test {
  background-color: #fff;
  position: fixed;
  bottom: 0%;
  right: 0%;
  left: 0%;
}
</style>
