<template>
  <v-card
    max-width="800"
    class="mx-auto"
  >
    <v-container>
      <v-row dense>
        <v-col cols="12">
          <v-card
            color="#385F73"
            dark
          >
            <v-card-title class="headline">{{ categoryId }}Unlimited music now</v-card-title>
            <v-card-subtitle>Listen to your favorite artists and albums whenever and wherever, online and offline.</v-card-subtitle>
          </v-card>
        </v-col>
        <v-col cols="12">
          <v-card
            color="#385F73"
            dark
          >
            <v-card-title class="headline">Unlimited music now</v-card-title>
            <v-card-subtitle>Listen to your favorite artists and albums whenever and wherever, online and offline.</v-card-subtitle>
          </v-card>
        </v-col>
        <v-col cols="12">
          <v-card
            color="#385F73"
            dark
          >
            <v-card-title class="headline">Unlimited music now</v-card-title>
            <v-card-subtitle>Listen to your favorite artists and albums whenever and wherever, online and offline.</v-card-subtitle>
          </v-card>
        </v-col>

      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
    name: 'PostList',
    props: {
      categoryId: {type: Number}
    },
    data(){
      return {
        posts: [],
			}
    },
    mounted() {
      this.getInterests()
    },
    methods: {
      getInterests() {
        axios.get(`http://127.0.0.1:5000/interest/${this.categoryId}`)
          .then(response => {
            console.log(response, 4444)
          })
      }
    }
}
</script>

<style>

</style>