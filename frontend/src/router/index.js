import Vue from 'vue'
import VueRouter from 'vue-router'
import Series from '../views/SeriesView.vue'
import HomeView from '../views/HomeView.vue'
import EventDetailView from '../views/EventDetailView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component : HomeView
  },
  {
    path: '/race_series',
    name: 'series',
    component: Series
  },
  {
    path: '/race_series/:id',
    name: 'race_series_detail',
    component: EventDetailView
  },
  {
    path: '*',
    redirect: '/'
  },
  
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
