import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import Vuetify from 'vuetify'
import './assets/styles/tailwind.css'

Vue.config.productionTip = false

Vue.use(Vuetify)

new Vue({
  router,
  vuetify,
  render: h => h(App),
  template: "<App/>"
}).$mount('#app')
