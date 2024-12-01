import { createRouter, createWebHistory } from 'vue-router';
import MapaView from '../views/MapaView.vue';
import GraficasView from '../views/GraficasView.vue';

const routes = [
  { path: '/', name: 'Mapa', component: MapaView },
  { path: '/graficas', name: 'Gráficas', component: GraficasView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
