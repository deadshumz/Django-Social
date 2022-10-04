import { createApp } from 'vue'
import App from './App'
import VueCookies from 'vue-cookies'
import './assets/tailwind.css'


createApp(App)
  .use(VueCookies)
  .mount('#app')
