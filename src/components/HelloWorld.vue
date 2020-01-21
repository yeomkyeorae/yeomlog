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
  name: 'HelloWorld',
  components: {
    ClickMeModal
  },
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
