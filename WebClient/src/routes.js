import {createRouter, createWebHistory } from 'vue-router';
import { getCookie } from './components/utils';
import Login from './pages/Login.vue'
import store from './store.js'

const routes = [
    {
        path: '/',
        alias: '/login',
        name: 'Login',
        component: Login,
        meta: {
            guest: true,
        },
    },
    {
        path: '/forgot-password',
        name: 'Forgot Password',
        component: () => import('./pages/ForgotPassword.vue'),
        meta: {
            guest: true,
        },
    },
    {
        path: '/recover-password',
        name: 'Recover Password',
        component: () => import('./pages/RecoverPassword.vue'),
        meta: {
            guest: true,
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

router.beforeEach(async(to, from, next) => {
    if (to.matched.some((record) => record.meta.guest)) {
        if(store.getters.isAuthenticated){
            next("/admin/dashboard");
            return;
        }
        let token = getCookie('vueadmin-login-access-token')
        if(!token){
            next();
            return;
        }
        
        try {
            const response = await fetch(`${import.meta.env.VITE_APP_API_BASE_ENDPOINT}/v1/auth/getUser`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "X-APP-TOKEN": token
                }
            });
            const result = await response.json();
            console.log(result);
            if (!response.ok | response.status != 200) {
                next();
            }
            store.commit('setUser', result.user);
            store.commit('setToken', token);
            next("/admin/dashboard");
            return;
        } catch (error) {
            console.log(error)
            console.error('error in user access token', JSON.stringify(error));
            next();
        }
    } else if (to.matched.some((record) => record.meta.requiresAuth)){
        if(store.getters.isAuthenticated){
            next();
            return;
        }
        let token = getCookie('vueadmin-login-access-token');
        if(!token){
            next('/login');
        }
        try {
            const response = await fetch(`${import.meta.env.VITE_APP_API_BASE_ENDPOINT}/v1/auth/getUser`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "X-APP-TOKEN": token
                }
            });
            const result = await response.json();
            if (!response.ok | response.status != 200) {
                next('/login');
            }
            
            store.commit('setUser', result.user);
            store.commit('setToken', token);
            next();
        } catch (error) {
            console.error('error in user access token', JSON.stringify(error));
            next('/login');
        }
    } else {
        next();
    }
});
export default router;
