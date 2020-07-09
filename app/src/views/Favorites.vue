<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <chart :options="option" />
  </a-layout>
</template>

<script>
import ECharts from "vue-echarts";
import "echarts/lib/chart/line";
import "echarts/lib/component/polar";
import "echarts/theme/dark";

export default {
  name: "Favorites",
  components: {
    chart: ECharts
  },
  data() {
    return {
      option: {
        title: {
          text: "Most Searched Movie Genre",
          subtext: "Compared With Other Users",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          left: "center",
          top: "bottom",
          data: [
            "Action",
            "Comedy",
            "Thriller",
            "Crime Film",
            "Drama",
            "Horror",
            "Adventure",
            "Night Shows"
          ]
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            magicType: {
              show: true,
              type: ["pie", "funnel"]
            },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        series: [
          {
            name: "Other",
            type: "pie",
            radius: [20, 110],
            center: ["25%", "50%"],
            roseType: "radius",
            label: {
              show: false
            },
            emphasis: {
              label: {
                show: true
              }
            },
            data: [
              { value: 10, name: "Action" },
              { value: 5, name: "Comedy" },
              { value: 15, name: "Thriller" },
              { value: 25, name: "Crime Film" },
              { value: 20, name: "Drama" },
              { value: 35, name: "Horror" },
              { value: 30, name: "Adventure" },
              { value: 40, name: "Night Shows" }
            ]
          },
          {
            name: "You",
            type: "pie",
            radius: [30, 110],
            center: ["75%", "50%"],
            roseType: "area",
            data: [
              { value: 10, name: "Action" },
              { value: 5, name: "Comedy" },
              { value: 15, name: "Thriller" },
              { value: 25, name: "Crime Film" },
              { value: 20, name: "Drama" },
              { value: 35, name: "Horror" },
              { value: 30, name: "Adventure" },
              { value: 40, name: "Night Shows" }
            ]
          }
        ]
      }
    };
  }
};
</script>

<style scoped>
/**
 * The default size is 600px×400px, for responsive charts
 * you may need to set percentage values as follows (also
 * don't forget to provide a size for the container).
 */
.echarts {
  width: 800px;
  height: 400px;
  margin: 100px auto;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .echarts {
    width: 600px;
    margin: 0px auto;
  }
}
</style>
