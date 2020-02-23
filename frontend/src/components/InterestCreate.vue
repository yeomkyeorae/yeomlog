<template>
  <div justify-content="center">
    <v-form ref="form" lazy-validation>
      <v-text-field v-model="title" label="title" required></v-text-field>
      <v-textarea label="content" auto-grow></v-textarea>
      <v-btn color="success" class="mr-4" @click="submit">게시</v-btn>
      <v-btn color="error" class="mr-4" @click="back">취소</v-btn>
    </v-form>
  </div>
</template>
<script>
// import axios from 'axios'

  export default {
    name: 'InterestCreate',
    props: {
      category: {
        type: String
      }
    },
    data: () => ({
      title: '',
      content: '',
    }),
    methods: {
      back() {
        this.$router.push(`/interests/${this.category}`)
      },
      submit() {
        // axios.post()
        //   .then(response => {
            
        //   })
      }
    },
  }
</script>