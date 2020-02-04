<template>
  <div>
	<h1>Network</h1>
    <MenuBar></MenuBar>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue'

export default {
    name: 'Network',
    components: {
      MenuBar
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