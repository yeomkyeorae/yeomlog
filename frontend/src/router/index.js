import Vue from 'vue'
import VueRouter from 'vue-router'
import Homepage from '../views/Homepage.vue'
import Cv from '../views/Cv.vue'
import Profile from '../components/Cv/Profile.vue'
import Account from '../components/Cv/Account.vue'
import Certificate from '../components/Cv/Certificate.vue'
import Interest from '../components/Cv/Interest.vue'
import Skill from '../components/Cv/Skill.vue'
import CvProject from '../components/Cv/CvProject.vue'
import Projects from '../views/Projects.vue'
import Project from '../components/Project.vue'

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
    children: [
      { path: 'profile', name: 'Profile', component: Profile},
      { path: 'account', name: 'Account', component: Account},
      { path: 'certificate', name: 'Certificate', component: Certificate},
      { path: 'interest', name: 'Interest', component: Interest},
      { path: 'skill', name: 'Skill', component: Skill},
      { path: 'project', name: 'CvProject', component: CvProject},
    ]
  },
  {
    path: '/projects',
    name: 'projects',
    component: Projects,
    children: [
      { path: ':projectId', name: 'project', component: Project, props: true}
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router