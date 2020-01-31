<template>
  <div>
    <ul>
      <li><router-link to="/interests/Bulletin"><span class="span">Algorithm</span></router-link></li>
      <li><router-link to="/"><span class="span">OS</span></router-link></li>
      <li><router-link to="/"><span class="span">Network</span></router-link></li>
      <li><router-link to="/"><span class="span">Web</span></router-link></li>
			<li><router-link to="/"><span class="span">Deep Learning</span></router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
    name: 'MenuBar',
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
.span {
  color: green;
}
</style>