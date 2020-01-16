import Vue from 'vue'
import VueRouter from 'vue-router'
import Cv from '../views/Cv.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/cv',
    name: 'cv',
    component: Cv,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router