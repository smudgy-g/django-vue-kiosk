import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/public/HomeView.vue'
import PortalLayout from '@/layouts/PortalLayout.vue'
import ProductList from '@/views/portal/ProductList.vue'
import DashboardView from '@/views/portal/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/public/LoginView.vue'),
    },
    {
      path: '/register',
      name: 'register',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/public/RegisterView.vue'),
    },
    {
      path: '/portal',
      // name: 'portal',
      component: PortalLayout,
      children: [
        {
          path: 'dashboard',
          name: 'dashboard',
          component: DashboardView,
        },
        {
          path: 'products',
          name: 'products',
          component: ProductList,
        },
        // {
        //   path: 'suppliers',
        //   component: ProductList,
        // },
        // {
        //   path: 'orders',
        //   component: ProductList,
        // },
        // {
        //   path: 'reports',
        //   component: ProductList,
        // },
      ],
    },
  ],
})

export default router
