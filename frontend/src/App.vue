<!--Esto es App cuando importo App de ./App.vue -->
<template>
  <v-app>
    <!-- -----Barra de navegación------------- -->
    <v-app-bar app>
      <v-toolbar-title>Halther</v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- Navegación -->
      <v-btn text to="/">Mapa</v-btn>
      <v-btn text to="/graficas">Gráficas</v-btn>
    </v-app-bar>

    <!-- Contenido principal -->
    <v-main>
      <!-- Las vistas de cada ruta se renderizan aquí -->
      <router-view />
    </v-main>

    <!-- -----Footer-------------------------- -->
    <v-footer app>
      <div style="text-align: center; width: 100%;">
        <span>© 2024 Halther. Todos los derechos reservados.</span>
        <br />
        <small style="color: gray;">Desarrollado con ❤️ por el equipo de Halther (Ozkar, Linares, Walter, Gab).</small>
      </div>
    </v-footer>
  </v-app>
</template>


<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
}
</script>
