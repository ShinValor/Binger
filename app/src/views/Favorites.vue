<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <a-button class="swiper-btn" @click="toggleModal">Try Our Swiper</a-button>
    <a-tabs class="tabs" default-active-key="1" @change="switchTabs">
      <a-tab-pane key="1" tab="Dashboard" force-render>
        <chart :options="option" />
      </a-tab-pane>
      <a-tab-pane key="2" tab="Liked Movies">
        <FavoriteMovieList :movieList="likedMovies" />
      </a-tab-pane>
      <a-tab-pane key="3" tab="Disliked Movies" force-render>
        <FavoriteMovieList :movieList="dislikedMovies" />
      </a-tab-pane>
    </a-tabs>
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
          text: "Movie Dashboard",
          subtext: "Most Searched Movie Genres",
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
            "Adventure",
            "Fantasy",
            "Animation",
            "Drama",
            "Horror",
            "Action",
            "Comedy",
            "History",
            "Western",
            "Thriller",
            "Crime",
            "Documentary",
            "Science Fiction",
            "Mystery",
            "Music",
            "Romance",
            "Family",
            "War",
            "Action & Adventure",
            "Kids",
            "News",
            "Reality",
            "Sci-Fi & Fantasy",
            "Soaps",
            "Talk",
            "War & Politics",
            "TV Movie"
          ],
          textStyle: {
            color: "white"
          }
        },
        series: [
          {
            name: "You",
            type: "pie",
            radius: [30, 100],
            center: ["50%", "50%"],
            roseType: "area",
            data: this.dataset()
          }
        ]
      }
    };
  },
  methods: {
    toggleModal() {
      this.modalVisible = !this.modalVisible;
    },
    dataset() {
      let dataset = this.$store.state.genres;
      dataset = JSON.parse(JSON.stringify(dataset));
      return dataset;
    },
    switchTabs(key) {
      console.log(key);
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

.tabs {
  width: 90%;
  margin: 100px auto;
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

  .swiper-btn {
    top: 12%;
    right: 5%;
  }
}
</style>
