<template>
  <div justify-content="center">
    {{ categoryId }}
    <v-form ref="form" lazy-validation>
      <v-text-field v-model="title" label="title" required></v-text-field>
      <v-textarea v-model="content" label="content" auto-grow></v-textarea>
      <v-btn color="success" class="mr-4" @click="submit">게시</v-btn>
      <v-btn color="error" class="mr-4" @click="back">취소</v-btn>
    </v-form>
  </div>
</template>
<script>
import axios from 'axios'

  export default {
    name: 'InterestCreate',
    props: {
      categoryId: {
        type: Number
      }
    },
    data: () => ({
      title: '',
      content: '',
    }),
    methods: {
      back() {
        this.$router.push(`/interests`)
      },
      submit() {
        const data = {
          'category_id': this.categoryId,
          'title': this.title,
          'content': this.content
        }
        console.log(data, 123123)
        axios.post('http://127.0.0.1:5000/interest', data)
          .then(response => {
            console.log(response, 111)
          })
      }
    },
  }
</script>