import Vue from 'vue'
import VueRouter from 'vue-router'
import Cv from '../views/Cv.vue'
import Projects from '../views/Projects.vue'
import Interests from '../views/Interests.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/cv',
    name: 'cv',
    component: Cv,
  },
  {
    path: '/projects',
    name: 'projects',
    component: Projects
  },
  {
    path: '/interests',
    name: 'interests',
    component: Interests
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router