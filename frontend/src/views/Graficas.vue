<template>
  <div class="charts-container">
    <!-- Gráfica de Barras por Estados -->
    <div class="chart-wrapper">
      <h2>Gráfica de Barras (Por Estados)</h2>
      <p>Comparativa de suicidios por estados a lo largo de los años.</p>
      <div id="bar-chart-states"></div>
    </div>

    <!-- Gráfica de Barras Total Nacional -->
    <div class="chart-wrapper">
      <h2>Gráfica de Barras (Total Nacional)</h2>
      <p>Total de suicidios nacionales por año.</p>
      <div id="bar-chart-total"></div>
    </div>

    <!-- Gráfica de Líneas -->
    <div class="chart-wrapper">
      <h2>Gráfica de Líneas</h2>
      <p>Tendencia de métodos de suicidio a través del tiempo.</p>
      <div id="line-chart"></div>
    </div>

    <!-- Gráfica de Pastel -->
    <div class="chart-wrapper">
      <h2>Gráfica de Pastel</h2>
      <p>Distribución porcentual de métodos en 2023.</p>
      <div id="pie-chart"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
///import ApexCharts from "apexcharts"; //para mi DEVelopment
import ApexCharts from 'apexcharts'; //para mi BUILD de produccion en TEST


export default {
  data() {
    return {
      barChartStatesOptions: {
        chart: {
          id: "bar-chart-states",
          type: "bar",
          height: "100%",

        },
        xaxis: {
          categories: [],
        },
        yaxis: {
          title: {
            text: "Número de suicidios por Estados",
          },
        },
      },
      barChartTotalOptions: {
        chart: {
          id: "bar-chart-total",
          type: "bar",
          height: "100%",

        },
        xaxis: {
          categories: ["2021", "2022", "2023"],
        },
        yaxis: {
          title: {
            text: "Total Nacional",
          },
        },
      },
      lineChartOptions: {
        chart: {
          id: "line-chart",
          type: "line",
          height: "100%",
        },
        xaxis: {
          categories: [
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
            "2023",
          ],
        },
        yaxis: {
          title: {
            text: "Número de suicidios",
          },
        },
      },
      pieChartOptions: {
        chart: {
          id: "pie-chart",
          type: "pie",
          height: "100%",
        },
        labels: [],
      },
      barStatesData: [],
      barTotalData: [],
      lineData: [],
      pieData: [],
    };
  },
  methods: {
    fetchBarChartData() {
      axios.get("http://localhost:5000/api/suicidios_por_anio")
      .then((response) => {
        const data = response.data;
        console.log("Datos recibidos para BarChart:", data);
  
        // Validar que los datos sean correctos
        if (!Array.isArray(data) || data.length === 0) {
          console.error("Datos inválidos o vacíos:", data);
          return;
        }

        // Filtrar datos para los Estados (excluyendo el total)
        const estadosData = data.filter(
          (item) =>
            item.Entidad &&
            item.Entidad !== "Total" && // Ajustado a 'Total'
            item["2021"] != null
        );

        // Configuración para BarChart de Estados
        this.barChartStatesOptions.xaxis.categories = estadosData.map(
          (item) => item.Entidad
        );
        this.barChartStatesOptions.series = [
          { name: "2021", data: estadosData.map((item) => item["2021"]) },
          { name: "2022", data: estadosData.map((item) => item["2022"]) },
          { name: "2023", data: estadosData.map((item) => item["2023"]) },
        ];

        // Obtener datos para Total Nacional
        const totalData = data.find((item) => item.Entidad === "Total"); // Ajustado a 'Total'
        if (!totalData) {
          console.error("Total no encontrado.");
          return;
        }

        // Configuración para BarChart de Total Nacional
        this.barChartTotalOptions.series = [
          {
            name: "Total Nacional",
            data: [totalData["2021"], totalData["2022"], totalData["2023"]],
          },
        ];

        // Renderizar gráficas
        this.renderBarChartStates();
        this.renderBarChartTotal();
      })
      .catch((error) => {
        console.error("Error al cargar los datos del gráfico de barras:", error);
      });
    },
    fetchLineChartData() {
      axios.get('http://localhost:5000/api/metodos_por_anio')
        .then(response => {
          const data = response.data;
          this.lineData = data;

          // Encontrar el valor máximo en los datos de las series
          const allValues = data.flatMap(method => method.Totales); // Obtiene todos los valores de 'Totales'
          const maxValue = Math.max(...allValues); // Encuentra el valor máximo

          // Configura el eje Y dinámicamente
          this.lineChartOptions.yaxis.max = maxValue + 10; // Puedes añadir un margen al máximo si lo deseas

      // Configuración de las series de datos para el gráfico de líneas
      this.lineChartOptions.series = data.map(method => ({
        name: method.Metodo,
        data: method.Totales
      }));

      this.renderLineChart();
      })
      .catch(error => {
        console.error('Error al cargar los datos del gráfico de líneas:', error);
      });
    },
    fetchPieChartData() {
      axios
        .get("http://localhost:5000/api/metodos_2023")
        .then((response) => {
          const data = response.data;
          this.pieData = data;
          this.pieChartOptions.labels = data.map((item) => item.Metodo);
          this.pieChartOptions.series = data.map((item) => item["2023"]);
          this.renderPieChart();
        })
        .catch((error) => {
          console.error("Error al cargar los datos del gráfico de pastel:", error);
        });
    },
    renderBarChartStates() {
      this.$nextTick(() => {
        const chart = new ApexCharts(
          document.querySelector("#bar-chart-states"),
          this.barChartStatesOptions
        );
        chart.render();
      });
    },

    renderBarChartTotal() {
      this.$nextTick(() => {
        const chart = new ApexCharts(
          document.querySelector("#bar-chart-total"),
          this.barChartTotalOptions
        );
        chart.render();
      });
    },

    renderLineChart() {
      this.$nextTick(() => {
        const chart = new ApexCharts(
          document.querySelector("#line-chart"),
          this.lineChartOptions
        );
        chart.render();
      });
    },

    renderPieChart() {
      this.$nextTick(() => {
        const chart = new ApexCharts(
          document.querySelector("#pie-chart"),
          this.pieChartOptions
        );
        chart.render();
      });
    }
  },
  mounted() {
    this.fetchBarChartData();
    this.fetchLineChartData();
    this.fetchPieChartData();
  },
};
</script>

<style scoped>
.charts-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
}

.chart-wrapper {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.chart-wrapper h2 {
  margin: 0 0 10px;
}

.chart-wrapper p {
  margin: 0 0 20px;
  color: #555;
}

#bar-chart-states,
#bar-chart-total,
#line-chart,
#pie-chart {
  width: 100%;
  min-height: 400px;
}
</style>
