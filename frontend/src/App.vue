<template>
    <div>
    <Navigation/>
    <v-app>
      <v-content>
        <router-view/>
      </v-content>
    </v-app>
    </div>
</template>

<script>
  import Navigation from './components/Navigation.vue'
  import '../tailwind.css'

  export default {
    name: 'app',
    components: {
      Navigation
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 10px;
  }
</style>