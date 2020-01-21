<template>
  <div class="hello">
    <img alt="Vue logo" src="../assets/yeom.jpg">
    <h1>Welcome to my blog, Yeomlog!</h1>
    <p>
      If you want to know about me,
    </p>
    <ClickMeModal/>
  </div>
</template>

<script>
import ClickMeModal from '../components/ClickMeModal'

export default {
  name: 'Homepage',
  components: {
    ClickMeModal
  },
  data() {
    return {

    }
  },
  props: {
    msg: String
  },
}
</script>

