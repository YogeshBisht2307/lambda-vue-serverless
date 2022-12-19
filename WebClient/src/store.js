import { createStore } from 'vuex'
import { setCookie } from './components/utils.js'

// Create a new store instance.
const store = createStore({
    state: {
        user: null,
        token: null,
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        },
        setToken(state, token) {
            state.token = token;
            setCookie("vueadmin-login-access-token", token)
        },
        logOut(state){
            state.user = null
            state.token = null
        }
    },
    actions: {
        getUser(){
            return state.user
        }
    },
    getters: {
        isAuthenticated: state => !!state.token,    
        StateUser: state => state.user,
    }
})

export default store;