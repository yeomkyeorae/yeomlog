<template>
  <div>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/cv">CV</router-link></li>
      <li><router-link to="/projects">Projects</router-link></li>
      <li><router-link to="/interests">Interests</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
    name: 'Navigation',
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