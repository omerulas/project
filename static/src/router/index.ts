import Home from '@/pages/public/Home.vue'
import Login from '@/pages/public/Login.vue'
import Main from '@/pages/workspace/Main.vue'
import { useAuth } from '@/stores/auth'
import Workspace from '@/views/Workspace.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', children: [
        {
          path: '',
          name: 'home',
          component: Home
        },
        {
          path: 'login',
          name: 'login',
          component: Login,
          meta: { requiresGuest: true }
        }
      ]
    },
    {
      path: '/workspace',
      meta: { requiresAuth: true },
      component: Workspace,
      children: [
        { path: '', name: 'workspace', component: Main }
      ]
    }
  ],
})

// --- Navigation Guard ---
router.beforeEach(async (to, from, next) => {
  const auth = useAuth()
  await auth.checkAuth()

  const isAuthenticated = auth.user.is_authenticated
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const requiresGuest = to.matched.some(record => record.meta.requiresGuest)

  if (requiresAuth && !isAuthenticated) {
    // Redirect parametresi ile login'e gönder
    return next({ name: 'login', query: { redirect: to.fullPath } })
  }

  if (requiresGuest && isAuthenticated) {
    return next({ name: 'workspace' })
  }

  next()
})

export default router
