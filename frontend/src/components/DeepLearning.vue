<template>
  <div>
	<h1>DeepLearning</h1>
    <v-btn class="mt-3 mb-3" to="deeplearning/create">글 쓰기</v-btn>
    <PostList></PostList>
  </div>
</template>

<script>
import PostList from '@/components/PostList.vue'

export default {
    name: 'DeepLearning',
    components: {
      PostList
    }
}
</script>
<style>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>