<template>
  <v-dialog class="dialogStyle" v-model="dialog" max-width="500px">
    <v-card>
      <v-card-title class="text-h5">{{ this.form.title }} </v-card-title>
      <v-card-text style="padding: 0">
        <v-container>
          <v-row>
            <template v-for="inputField in this.customHeaders">
              <v-col
                v-if="inputField.edit && inputField.text === 'Conductor'"
                v-bind:key="inputField.text"
                cols="12"
                sm="6"
                md="6"
              >
                <v-select
                  v-model="selectDriver"
                  v-bind:label="inputField.text"
                  :items="drivers"
                  item-text="name"
                  return-object
                >
                  <!-- item-value="id" -->
                  <template slot="selection" slot-scope="data">
                    {{ data.item.name }} {{ data.item.last_name }}
                  </template>
                  <template slot="item" slot-scope="data">
                    {{ data.item.name }} {{ data.item.last_name }}
                  </template>
                </v-select>
              </v-col>
              <v-col
                v-else-if="inputField.edit && inputField.type === 'date'"
                v-bind:key="inputField.text"
                cols="12"
                sm="6"
                md="6"
              >
                <v-text-field
                  type="datetime-local"
                  v-bind:label="inputField.text"
                  v-model="edit[inputField.value]"
                ></v-text-field>
              </v-col>
              <v-col
                v-else-if="inputField.edit"
                v-bind:key="inputField.text"
                cols="12"
                sm="6"
                md="6"
              >
                <v-text-field
                  v-bind:label="inputField.text"
                  v-model="edit[inputField.value]"
                ></v-text-field>
              </v-col>
            </template>
          </v-row>
        </v-container>
      </v-card-text>

      <v-card-actions style="padding: 12px 24px">
        <v-btn
          color="primary"
          class="ma-2"
          outlined
          elevation="2"
          @click="close"
          >Cancelar</v-btn
        >
        <v-btn color="primary" elevation="2" @click="onFinish()">Guardar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    close: Function,
    // save: Function,
    item: Object,
    form: Object,
    customHeaders: Array,
    drivers: Array,
  },
  data: () => ({
    dialog: true,
    edit: {},
  }),
  mounted() {
    this.edit = this.item;
    if (this.edit.driver) {
      this.drivers.push(this.edit.driver);
    }
  },
  methods: {
    onFinish() {
      this.$emit("onFinish", this.edit);
    },
  },
  computed: {
    selectDriver: {
      get() {
        return this.edit.driver;
      },
      set(value) {
        this.edit.driver = value;
      },
    },
  },
};
</script>
