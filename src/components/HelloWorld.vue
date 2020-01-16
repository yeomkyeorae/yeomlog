<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      If you want to know about me,
      <a href="#" target="_blank" rel="noopener">click me</a>.
    </p>
    <ul>
      <li><router-link to="/cv">CV</router-link></li>
      <li><a href="#" target="_blank" rel="noopener">Projects</a></li>
      <li><a href="#" target="_blank" rel="noopener">Interests</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
