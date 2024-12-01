import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import { createRouter, createWebHistory } from 'vue-router';

//Mapa necesita leaflet
import "leaflet/dist/leaflet.css";
//Graficas necesita apexCharts
import VueApexCharts from 'vue3-apexcharts';


//vistas
import MapView from './views/Mapa.vue';
import GraficasView from './views/Graficas.vue';

// Definir las rutas
const routes = [
  { path: '/', component: MapView },
  { path: '/graficas', component: GraficasView },
];

// Crear el router
const router = createRouter({
  history: createWebHistory(),
  routes, // Aquí es donde lo usas
});

loadFonts()

createApp(App)
  .use(vuetify)
  .use(router) // Agregar el router a la app
  .use(VueApexCharts) // Agregar ApexCharts a la app
  .mount('#app')