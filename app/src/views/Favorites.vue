<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <chart :options="option" />
    <a-button class="swiper-btn" @click="toggleModal">Try Our Swiper</a-button>
    <h1 :style="{ color: 'white' }">Liked Movie Id</h1>
    <ul :style="{ color: 'white' }">
      <li v-for="(movieId, index) in likedMovies" :key="index">
        {{ movieId }}
      </li>
    </ul>
    <h1 :style="{ color: 'white' }">Disliked Movie Id</h1>
    <ul :style="{ color: 'white' }">
      <li v-for="(movieId, index) in dislikedMovies" :key="index">
        {{ movieId }}
      </li>
    </ul>
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
          text: "Your Movie Dashboard",
          subtext: "Most Searched Movie Genre",
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
        // toolbox: {
        //   show: true,
        //   feature: {
        //     mark: { show: true },
        //     dataView: { show: true, readOnly: false },
        //     magicType: {
        //       show: true,
        //       type: ["pie", "funnel"]
        //     },
        //     restore: { show: true },
        //     saveAsImage: { show: true }
        //   }
        // },
        series: [
          {
            name: "You",
            type: "pie",
            radius: [30, 110],
            center: ["50%", "50%"],
            roseType: "area",
            data: [
              { name: "Action", value: 10 },
              { name: "Comedy", value: 5 },
              { name: "Thriller", value: 15 },
              { name: "Crime Film", value: 25 },
              { name: "Drama", value: 20 },
              { name: "Horror", value: 35 },
              { name: "Adventure", value: 30 },
              { name: "Night Shows", value: 40 }
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
  },
  computed: {
    likedMovies() {
      return this.$store.state.likedMovies;
    },
    dislikedMovies() {
      return this.$store.state.dislikedMovies;
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
  margin: 50px auto;
}

.favoriteList {
  margin: 25px;
}

.swiper-btn {
  position: absolute;
  top: 10%;
  right: 1%;
  background-color: transparent;
  color: white;
}

.swiper-btn:hover,
.swiper-btn:active,
.swiper-btn:focus {
  border-color: white;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .echarts {
    width: 600px;
    margin: 25px auto;
  }

  .favoriteList {
    margin: 15px 10px;
  }
}
</style>
