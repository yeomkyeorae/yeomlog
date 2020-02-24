<template>
  <div>
    <h1>{{ title }}</h1>
    <ul>
      <li><span class="span" @click="change('Algorithm', 0)">Algorithm</span></li>
      <li><span class="span" @click="change('Os', 1)">OS</span></li>
      <li><span class="span" @click="change('Network', 2)">Network</span></li>
      <li><span class="span" @click="change('Web', 3)">Web</span></li>
      <li><span class="span" @click="change('Deep Learning', 4)">Deep Learning</span></li>
    </ul>
    <v-btn class="mt-3 mb-3" :to="{ name: 'InterestCreate', params: {categoryId: categoryId, interestTitle: title}}">글 쓰기</v-btn>
    <PostList :categoryId="categoryId"></PostList>
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
        title: 'Algorithm',
        categoryId: 0
      }
    },
    methods: {
      change(title, categoryId) {
        this.title = title
        this.categoryId = categoryId
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