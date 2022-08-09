<template>
  <v-dialog class="dialogStyle" v-model="dialogDelete" max-width="500px">
    <v-card>
      <v-card-title class="text-h5"
        >Eliminar {{ this.labels.subTitle }}</v-card-title
      >
      <v-card-text
        >¿Estás seguro que deseas eliminar el {{ this.labels.subTitle }}
        {{ this.item.name }}?</v-card-text
      >
      <v-card-actions>
        <v-btn
          color="primary"
          class="ma-2"
          outlined
          elevation="2"
          @click="close"
          >Cancelar</v-btn
        >
        <v-btn color="primary" elevation="2" @click="onFinish()">Eliminar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    close: Function,
    // confirm: Function,
    item: Object,
    labels: Object,
  },
  data: () => ({
    dialogDelete: true,
  }),
  methods: {
    onFinish() {
      this.$emit("onFinish", this.item.id);
    },
  },
};
</script>
