import { createApp } from 'vue'
import App from './App.vue'
import router from './routes.js'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faEnvelope, faLock } from '@fortawesome/free-solid-svg-icons'

library.add(faEnvelope, faLock)


const app = createApp(App)
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount("#app")