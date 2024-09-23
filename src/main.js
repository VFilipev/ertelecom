import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import axios from 'axios'
import './index.css'
// import VueTreeList from 'vue-tree-list'
// import Vue from 'vue'

// Vue.use(VueTreeList)


const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
const app = createApp(App)

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'
// app.use(VueTreeList)
app.use(pinia)
app.use(router)
app.mount('#app')
