<template>
  <div class="hello">
    <img alt="Vue logo" src="../assets/yeom.jpg">
    <h1>Welcome to my blog, Yeomlog!</h1>
    <p>
      If you want to know about me,
      <button type="button" @click="openModal">click me</button>
    </p>
  </div>
</template>

<script>
import ClickMeModal from './ClickMeModal'

export default {
<<<<<<< HEAD:src/components/HelloWorld.vue
  name: 'HelloWorld',
  components: {
    ClickMeModal
  },
=======
  name: 'Homepage',
>>>>>>> 38d76a06b82a0ec7ab6d28ce0f07959b3ae1a921:src/views/Homepage.vue
  props: {
    msg: String
  },
  methods: {
    openModal() {
      this.dialog = true
    }
  }
}
</script>

