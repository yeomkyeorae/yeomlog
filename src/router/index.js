import Vue from 'vue'
import VueRouter from 'vue-router'
import Homepage from '../views/Homepage.vue'
import Cv from '../views/Cv.vue'
import Projects from '../views/Projects.vue'
import Interests from '../views/Interests.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'homepage',
    component: Homepage,
  },
  {
    path: '/cv',
    name: 'cv',
    component: Cv,
  },
  {
    path: '/projects',
    name: 'projects',
<<<<<<< HEAD
    component: Projects
=======
    component: Projects,
>>>>>>> 38d76a06b82a0ec7ab6d28ce0f07959b3ae1a921
  },
  {
    path: '/interests',
    name: 'interests',
<<<<<<< HEAD
    component: Interests
=======
    component: Interests,
>>>>>>> 38d76a06b82a0ec7ab6d28ce0f07959b3ae1a921
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router