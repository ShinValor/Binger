<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <chart :options="option" />
    <a-button class="swiper" @click="toggleModal">Try Our Swiper</a-button>
    <FavoriteMovieList class="favoriteList" />
    <a-modal
      v-model="modalVisible"
      :title="'Movie Swiper'"
      :width="600"
      :footer="null"
    >
      <MovieSwiper />
    </a-modal>
  </a-layout>
</template>

<script>
import ECharts from "vue-echarts";
import "echarts/lib/chart/line";
import "echarts/lib/component/polar";
import "echarts/theme/dark";
import FavoriteMovieList from "@/components/FavoriteMovieList.vue";
import MovieSwiper from "@/components/MovieSwiper.vue";

export default {
  name: "Favorites",
  components: {
    FavoriteMovieList,
    MovieSwiper,
    chart: ECharts
  },
  data() {
    return {
      modalVisible: false,
      option: {
        title: {
          text: "Most Searched Movie Genre",
          subtext: "Compared With Other Users",
          left: "center",
          textStyle: {
            color: "white"
          }
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
          ],
          textStyle: {
            color: "white"
          }
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
            name: "You",
            type: "pie",
            radius: [30, 110],
            center: ["50%", "50%"],
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
  },
  methods: {
    toggleModal() {
      this.modalVisible = !this.modalVisible;
    }
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

.favoriteList {
  margin: 25px;
}

.swiper {
  position: absolute;
  top: 10%;
  right: 1%;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .echarts {
    width: 600px;
    margin: 0px auto;
  }

  .favoriteList {
    margin: 15px 10px;
  }
}
</style>
