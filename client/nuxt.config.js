import colors from "vuetify/es5/util/colors";

export default {
  axios: {
    baseURL: "http://localhost:8000/api/v1.0/",
  },
  head: {
    titleTemplate: "%s - Tours",
    title: "Tours",
    htmlAttrs: {
      lang: "es",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },
  css: [],
  plugins: [{ src: "~plugins/v-calendar.js", ssr: false }],
  components: true,
  buildModules: ["@nuxtjs/vuetify", "@nuxtjs/dotenv", "@nuxtjs/moment"],
  moment: {
    defaultLocale: "de",
    locales: ["de"],
    timezone: true,
    plugin: false,
  },
  modules: [],
  vuetify: {
    customVariables: ["~/assets/variables.scss"],
    theme: {
      light: true,
      themes: {
        light: {
          primary: colors.blue.darken2,
          accent: colors.grey.lighten3,
          secondary: colors.orange.darken1,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },
  build: {},
};
