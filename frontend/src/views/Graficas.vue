<template>
  <div class="charts-container">
    <!-- Gráfica de Barras por Estados -->
    <div class="chart-wrapper">
      <h2>Gráfica de Barras (Por Estados)</h2>
      <p>Comparativa de suicidios por estados a lo largo de 2021 a 2023.</p>
      <div id="bar-chart-states"></div>
    </div>

    <!-- Gráfica de Barras Total Nacional -->
    <div class="chart-wrapper">
      <h2>Gráfica de Barras (Total Nacional)</h2>
      <p>Total de suicidios nacionales de 2021 a 2023.</p>
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

  <div class="signature">
    <p>✨ Grav estuvo aquí ✨</p>
  </div>
</template>

<script>
import axios from "axios";
import ApexCharts from "apexcharts";

export default {
  data() {
    return {
      barChartStatesOptions: {
        chart: {
          id: "bar-chart-states",
          type: "bar",
          height: "400px",
        },
        xaxis: {
          categories: [],
        },
        yaxis: {
          title: {
            text: "Número de suicidios por Estados",
          },
        },
        series: [], // Series vacías inicializadas
      },
      barChartTotalOptions: {
        chart: {
          id: "bar-chart-total",
          type: "bar",
          height: "400px",
        },
        xaxis: {
          categories: ["2021", "2022", "2023"],
        },
        yaxis: {
          title: {
            text: "Total Nacional",
          },
        },
        series: [], // Series vacías inicializadas
      },
      lineChartOptions: {
        chart: {
          id: "line-chart",
          type: "line",
          height: "400px",
        },
        xaxis: {
          categories: [],
        },
        yaxis: {
          title: {
            text: "Número de suicidios",
          },
        },
        series: [], // Series vacías inicializadas
      },
      pieChartOptions: {
        chart: {
          id: "pie-chart",
          type: "pie",
          height: "400px",
        },
        labels: [],
        series: [], // Series vacías inicializadas
      },
    };
  },
  methods: {
    getApiBaseUrl() {
      return process.env.NODE_ENV === "production"
        ? "http://34.213.42.7:5000"
        : "http://127.0.0.1:5000";
    },
    fetchBarChartData() {
      axios
        .get(`${this.getApiBaseUrl()}/api/suicidios_por_anio`)
        .then((response) => {
          const data = response.data;
          const estadosData = data.filter(
            (item) => item.Entidad && item.Entidad !== "Total"
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

          // Configuración para BarChart de Total Nacional
          const totalData = data.find((item) => item.Entidad === "Total");
          if (totalData) {
            this.barChartTotalOptions.series = [
              {
                name: "Total Nacional",
                data: [totalData["2021"], totalData["2022"], totalData["2023"]],
              },
            ];
          }

          // Renderizar gráficas
          this.renderBarChartStates();
          this.renderBarChartTotal();
        })
        .catch((error) =>
          console.error("Error al cargar los datos del gráfico de barras:", error)
        );
    },
    fetchLineChartData() {
      axios
        .get(`${this.getApiBaseUrl()}/api/metodos_por_anio`)
        .then((response) => {
          const data = response.data;

          this.lineChartOptions.series = data.map((method) => ({
            name: method.Metodo,
            data: method.Totales,
          }));

          this.lineChartOptions.xaxis.categories = [
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
          ];

          this.renderLineChart();
        })
        .catch((error) =>
          console.error("Error al cargar los datos del gráfico de líneas:", error)
        );
    },
    fetchPieChartData() {
      axios
        .get(`${this.getApiBaseUrl()}/api/metodos_2023`)
        .then((response) => {
          const data = response.data;
          this.pieChartOptions.labels = data.map((item) => item.Metodo);
          this.pieChartOptions.series = data.map((item) => item["2023"]);

          this.renderPieChart();
        })
        .catch((error) =>
          console.error("Error al cargar los datos del gráfico de pastel:", error)
        );
    },
    renderBarChartStates() {
      const chart = new ApexCharts(
        document.querySelector("#bar-chart-states"),
        this.barChartStatesOptions
      );
      chart.render();
    },
    renderBarChartTotal() {
      const chart = new ApexCharts(
        document.querySelector("#bar-chart-total"),
        this.barChartTotalOptions
      );
      chart.render();
    },
    renderLineChart() {
      const chart = new ApexCharts(
        document.querySelector("#line-chart"),
        this.lineChartOptions
      );
      chart.render();
    },
    renderPieChart() {
      const chart = new ApexCharts(
        document.querySelector("#pie-chart"),
        this.pieChartOptions
      );
      chart.render();
    },
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

.signature {
  text-align: center;
  margin-top: 20px;
  padding: 10px;
  background: linear-gradient(90deg, #ffafbd, #ffc3a0);
  border-radius: 8px;
  font-size: 1.2rem;
  font-weight: bold;
  color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

</style>
