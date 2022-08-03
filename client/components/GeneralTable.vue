<template>
  <v-card style="padding: 2rem">
    <v-card-title>
      Listado de Trayectos
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Buscar"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon class="mr-4 icons" small v-model="item.actions">
          mdi-pencil
        </v-icon>
        <v-icon class="icons" small v-model="item.actions"> mdi-delete </v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        {
          text: "ID",
          align: "start",
          sortable: true,
          value: "id",
        },
        { text: "Trayecto", value: "name" },
        { text: "Fecha Inicio", value: "start_date" },
        { text: "Fecha Final", value: "end_date" },
        { text: "% Pasajeros", value: "capacity" },
        { text: "Acciones", value: "actions" },
      ],
      desserts: [
        {
          id: 1,
          name: "San blas",
          start_date: "19/07/2022",
          end_date: "20/07/2022",
          capacity: "55%",
          actions: "1%",
        },
        {
          id: 2,
          name: "Caminito",
          start_date: "19/07/2022",
          end_date: "20/07/2022",
          capacity: "65%",
          actions: "1%",
        },
        {
          id: 3,
          name: "Puerto Madero",
          start_date: "19/07/2022",
          end_date: "20/07/2022",
          capacity: "55%",
          actions: "7%",
        },
        {
          id: 4,
          name: "Chaarita",
          start_date: "19/07/2022",
          end_date: "20/07/2022",
          capacity: "55%",
          actions: "8%",
        },
        {
          id: 5,
          name: "Costanera",
          start_date: "19/07/2022",
          end_date: "20/07/2022",
          capacity: "85%",
          actions: "16%",
        },
      ],
    };
  },
};
</script>
<style>
.v-card__title {
  padding: 1rem 0;
  font-family: "Muli", sans-serif !important;
}
.icons {
  cursor: pointer;
}
</style>
