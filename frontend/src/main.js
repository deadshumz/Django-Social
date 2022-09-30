import { createApp } from 'vue'
import App from './App'
import VueCookies from 'vue-cookies'


createApp(App)
  .use(VueCookies)
  .mount('#app')
