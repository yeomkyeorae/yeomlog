<template>
  <div>
	<h1>{{ title }}</h1>    
  <ul>
      <li><span class="span" @click="change('Algorithm')">Algorithm</span></li>
      <li><span class="span" @click="change('Os')">OS</span></li>
      <li><span class="span" @click="change('Network')">Network</span></li>
      <li><span class="span" @click="change('Web')">Web</span></li>
			<li><span class="span" @click="change('Deep Learning')">Deep Learning</span></li>
    </ul>
    <v-btn class="mt-3 mb-3" to="/create">글 쓰기</v-btn>
    <PostList></PostList>
  </div>
</template>

<script>
import PostList from '@/components/PostList.vue'

export default {
    name: 'Interest',
    components: {
      PostList
    },
    data() {
      return {
        title: 'Algorithm'
      }
    },
    methods: {
      change(title) {
        this.title = title
      }
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