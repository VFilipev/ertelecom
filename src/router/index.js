import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home-page',
      component: () => import( '../views/HomePage.vue')
    },
    {
      path: '/login',
      name: 'login-page',
      component: () => import( '../views/LoginPage.vue')
    },
    {
        path: '/register',
        name: 'register-page',
        component: () => import( '../views/RegisterPage.vue')
      }
  ]
})

export default router
