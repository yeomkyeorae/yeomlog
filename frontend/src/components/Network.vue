<template>
  <div>
	<h1>Network</h1>
    <MenuBar></MenuBar>
    <v-btn class="mt-3 mb-3">글 쓰기</v-btn>
    <PostList></PostList>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue'
import PostList from '@/components/PostList.vue'

export default {
    name: 'Network',
    components: {
      MenuBar,
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