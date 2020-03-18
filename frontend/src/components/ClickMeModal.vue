<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" width="600px">
      <template v-slot:activator="{ on }">
        <v-btn style="background-color:#F9ACAA" v-on="on">Click Me</v-btn>
      </template>
      <v-card class="fontStylish">
        <v-card-title>
          <span class="headline">Welcome to my world!</span>
        </v-card-title>
        <v-card-text class="fontStylish">My name is kyeorae Yeom. <br>
        I want to live as I wish.<br>
        Programming will help make a better world.<br>
        So I do it.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
  export default {
    name: 'ClickMeModal',
    data() {
      return {
        dialog: false
      }
    },
  }
</script>

<style>
  .fontStylish {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    font-size: 1.3rem;
    text-align: center;
  }
</style>