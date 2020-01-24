<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" width="600px">
      <template v-slot:activator="{ on }">
        <v-btn color="blue" dark v-on="on">Click Me</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Introduce!</span>
        </v-card-title>
        <v-card-text>My name is kyeorae Yeom. I want to be a man who lives as I want to do. I believe that doing programming will make world better than now. So I do it.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
    name: 'ClickMeModal',
    data () {
      return {
        dialog: false
    }
  },
}
</script>

<style>

</style>