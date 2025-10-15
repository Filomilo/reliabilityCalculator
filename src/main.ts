import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Noir from './presets/Noir';
import { pyodideModule } from './modules/pyodide';
 import LoadScript from "vue-plugin-load-script";

const app = createApp(App)

function toggleDarkMode() {
    document.documentElement.classList.toggle('my-app-dark');
}

app.use(router)
app.use(PrimeVue, {
    theme: {
        preset: Noir,
        options: {
            prefix: 'p',
            darkModeSelector: '.my-app-dark',
            cssLayer: false,
        }
    }
});
  app.use(LoadScript);
pyodideModule.initialize();

toggleDarkMode();
app.mount('#app')
