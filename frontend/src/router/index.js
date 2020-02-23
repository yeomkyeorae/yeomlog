import Vue from 'vue'
import VueRouter from 'vue-router'
import Homepage from '../views/Homepage.vue'
import Cv from '../views/Cv.vue'
import InterestCreate from '@/components/InterestCreate.vue'
import Projects from '../views/Projects.vue'
import Project from '../components/Project.vue'
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
    component: Projects,
    children: [
      { path: ':projectId', name: 'project', component: Project, props: true}
    ]
  },
  {
    path: '/interests',
    name: 'interests',
    component: Interests,
  },
  {
    path: '/interests/create',
    name: 'InterestCreate',
    component: InterestCreate,
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router