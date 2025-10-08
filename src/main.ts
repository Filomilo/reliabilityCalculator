import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Noir from './presets/Noir';
import { pyodideModule } from './modules/pyodide';
 import LoadScript from "vue-plugin-load-script";

const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
    theme: {
        preset: Noir,
        options: {
            prefix: 'p',
            darkModeSelector: '.p-dark',
            cssLayer: false,
        }
    }
});
  app.use(LoadScript);
pyodideModule.initialize(['RelCalcualtor.py']);
app.mount('#app')
