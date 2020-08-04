<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div :style="{ display: 'inline' }">
      <a-button class="swiper-btn" @click="toggleModal">
        Try Our Swiper
      </a-button>
    </div>
    <a-tabs class="tabs" default-active-key="1" @change="switchTabs">
      <a-tab-pane key="1" tab="My Dashboard" force-render>
        <ECharts ref="echarts" :options="eChartsOption" />
        <!-- <a-button @click="updateChart"> View </a-button> -->
      </a-tab-pane>
      <a-tab-pane key="2" tab="Liked Movies">
        <FavoriteMovieList class="favorite-movie" :movieList="likedMovies" />
      </a-tab-pane>
      <a-tab-pane key="3" tab="Disliked Movies" force-render>
        <FavoriteMovieList class="favorite-movie" :movieList="dislikedMovies" />
      </a-tab-pane>
      <a-tab-pane key="4" tab="Recommendations" force-render>
        <h1 :style="{ color: 'white' }">Something</h1>
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
    <BackToTop />
  </a-layout>
</template>

<script>
import ECharts from "vue-echarts";
import "echarts/lib/chart/line";
import "echarts/lib/component/polar";
import "echarts/theme/dark";
import FavoriteMovieList from "@/components/FavoriteMovieList.vue";
import MovieSwiper from "@/components/MovieSwiper.vue";
import BackToTop from "@/components/BackToTop.vue";
import { eChartsOption } from "../util/eChartsOption";

export default {
  name: "Favorites",
  components: {
    FavoriteMovieList,
    MovieSwiper,
    ECharts,
    BackToTop
  },
  data() {
    return {
      modalVisible: false,
      eChartsOption
    };
  },
  methods: {
    toggleModal() {
      this.modalVisible = !this.modalVisible;
    },
    switchTabs(key) {
      console.log(key);
    }
    // updateChart() {
    //   this.$refs.echarts.mergeOptions({
    //     series: [
    //       {
    //         data: this.$store.state.genres
    //       }
    //     ]
    //   });
    // }
  },
  computed: {
    likedMovies() {
      return this.$store.state.likedMovies;
    },
    dislikedMovies() {
      return this.$store.state.dislikedMovies;
    }
  },
  beforeUpdate() {
    this.$refs.echarts.mergeOptions({
      series: [
        {
          data: this.$store.state.genres
        }
      ]
    });
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
  width: 100%;
  height: 600px;
  margin: 20px auto;
}

.tabs {
  width: 85%;
  margin: 25px auto 50px;
}

.favorite-movie {
  margin-top: 20px;
}

.swiper-btn {
  background-color: transparent;
  width: 125px;
  height: 100%;
  margin: 20px;
  padding: 5px;
  color: white;
  border-color: #f3c669;
  float: right;
}

.swiper-btn:hover {
  background-color: #f3c669;
}

@media screen and (max-width: 800px) {
  .tabs {
    width: 95%;
    margin: 10px auto;
  }

  .echarts {
    width: 600px;
    height: 700px;
  }

  .swiper-btn {
    margin: 10px;
  }
}
</style>
