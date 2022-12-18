import {createRouter, createWebHistory } from 'vue-router';
import Login from './pages/Login.vue'

const routes = [
    {
        path: '/',
        alias: '/login',
        name: 'Login',
        component: Login,
        meta: {
            requiresAuth: false,
        },
    },
    {
        path: '/forgot-password',
        name: 'Forgot Password',
        component: () => import('./pages/ForgotPassword.vue'),
        meta: {
            requiresAuth: false,
        },
    },
    {
        path: '/recover-password',
        name: 'Recover Password',
        component: () => import('./pages/RecoverPassword.vue'),
        meta: {
            requiresAuth: false,
        },
    },
    {
        path: '/admin',
        alias: '/admin/dashboard',
        name: "Dashboard",
        component: () => import('./pages/Dashboard.vue'),
        meta: {
            requiresAuth: true,
        },
    }
]

const router = createRouter({ history: createWebHistory(), routes: routes });
router.beforeEach((to, from, next) => {
    let documentTitle = `${import.meta.env.VITE_APP_TITLE} - ${to.name}`
    if (to.params.title){
        documentTitle += ` - ${to.params.title}`
    }
    document.title = documentTitle
    next()
});
export default router;
