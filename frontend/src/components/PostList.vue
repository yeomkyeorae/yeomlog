<template>
  <v-card
    max-width="800"
    class="mx-auto"
  >
    <v-container>
      <v-row v-for="post in posts" :key="post.id" dense>
        <v-col cols="12">
          <v-card
            color="#385F73"
            dark
          >
            <v-card-title class="headline">{{ post.title }}</v-card-title>
            <v-card-subtitle>{{ post.content }}</v-card-subtitle>
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
            this.posts = response.data
            console.log(response, 4444)
          })
      }
    },
    watch: { 
      categoryId: function () {
         this.getInterests() 
      } 
    },
}
</script>

<style>

</style>