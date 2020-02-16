<template>
  <div justify-content="center">
  <v-form
    ref="form"
    lazy-validation
  >
    <v-text-field
      v-model="title"
      label="title"
      required
    ></v-text-field>

    <v-textarea
      label="content"
      auto-grow
    ></v-textarea>

    <v-btn
      color="success"
      class="mr-4"
    >
      게시
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
    >
      취소
    </v-btn>
  </v-form>
    </div>
</template>
<script>
  export default {
    name: 'CreateForm',
    data: () => ({
      title: '',
      content: '',
    }),

    methods: {

    },
  }
</script>