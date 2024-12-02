<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="4">
          <v-select
            v-model="selectedYear"
            :items="years"
            label="Selecciona un año"
            outlined
          />
          <v-btn
            color="primary"
            class="mt-4"
            @click="fetchData"
            :disabled="!selectedYear"
          >
            Cargar Datos
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <div id="map" style="height: 500px;"></div>
  </div>
</template>

<script>
// Importa Leaflet
import L from 'leaflet';
import 'leaflet/dist/leaflet.css'; // Importa los estilos de Leaflet

export default {
  name: "MapView",
  data() {
    return {
      mapInstance: null,
      selectedYear: null,
      years: [
        2010, 2011, 2012, 2013, 2014, 2015,
        2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
      ],
      markers: [],
    };
  },
  methods: {
    async fetchData() {
      const url = `${await this.getApiBaseUrl()}/api/suicidios?year=${this.selectedYear}`;
      try {
        const response = await fetch(url);
        const data = await response.json();
        if (response.ok) {
          this.updateMap(data);
        } else {
          console.error(data.error);
          alert("Error al cargar los datos.");
        }
      } catch (error) {
        console.error("Error de conexión:", error);
        alert("Error al conectar con el servidor.");
      }
    },
    async getApiBaseUrl() {
      try {
        const response = await fetch("http://169.254.169.254/latest/meta-data/public-ipv4");
        if (response.ok) {
          const ip = await response.text();
          return `http://${ip}:5000`;
        }
      } catch (error) {
        console.warn("No se pudo obtener la IP pública de AWS. Usando 127.0.0.1");
      }
      return "http://127.0.0.1:5000";
    },
    updateMap(data) {
      // Limpiar los marcadores previos
      this.markers.forEach(marker => this.mapInstance.removeLayer(marker));
      this.markers = [];

      // Crear un ícono personalizado
      const customIcon = L.icon({
        iconUrl: '/images/marker-icon.png', // Asegúrate que esté en el directorio correcto
        iconSize: [25, 41], // Tamaño del ícono
        iconAnchor: [12, 41], // Ancla del ícono para posicionarlo correctamente
        popupAnchor: [1, -34], // Lugar donde aparecerá el popup respecto al ícono
        shadowUrl: '/images/marker-shadow.png', // Sombra del ícono
        shadowSize: [41, 41], // Tamaño de la sombra
      });

      // Agregar marcadores con el ícono personalizado
      data.forEach(location => {
        const markerInstance = L.marker([location.Lat, location.Lon], { icon: customIcon })
          .bindPopup(`<b>${location.Entidad}</b><br>Total: ${location.Total}`)
          .addTo(this.mapInstance);
        this.markers.push(markerInstance);
      });
    },
  },
  mounted() {
    // Inicializar mapa
    this.mapInstance = L.map("map").setView([23.634501, -102.552784], 5);

    // Cargar el fondo del mapa
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.mapInstance);
  },
};
</script>

<style scoped>
#map {
  margin-top: 20px;
  width: 100%;
  height: 500px;
}
</style>
