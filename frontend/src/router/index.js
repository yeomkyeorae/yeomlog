import Vue from 'vue'
import VueRouter from 'vue-router'
import Homepage from '../views/Homepage.vue'
import Cv from '../views/Cv.vue'
import Algorithm from '@/components/Algorithm.vue'
import Os from '@/components/Os.vue'
import Network from '@/components/Network.vue'
import Web from '@/components/Web.vue'
import DeepLearning from '@/components/DeepLearning.vue'
import CreateForm from '@/components/CreateForm.vue'
import Projects from '../views/Projects.vue'
import Project1 from '../components/Projects/Project1.vue'
import Project2 from '../components/Projects/Project2.vue'
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
    component: Projects
  },
  {
    path: '/interests',
    name: 'interests',
    component: Interests,
    children: [
      { path: 'algorithm', name: 'Algorithm', component: Algorithm },
      { path: 'os', name: 'OS', component: Os },
      { path: 'network', name: 'Network', component: Network },
      { path: 'web', name: 'Web', component: Web },
      { path: 'deeplearning', name: 'DeepLearning', component: DeepLearning },
      { path: ':category/create', name: 'CreateForm', component: CreateForm, props: true}
    ]
  },
  {
		path: '/projects/0',
		name: 'project1',
		component: Project1
	},
	{
		path: '/projects/1',
		name: 'project2',
		component: Project2
	}
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router