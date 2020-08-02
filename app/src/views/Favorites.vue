<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div :style="{ display: 'flex', 'justify-content': 'flex-end' }">
      <a-button class="swiper-btn" @click="toggleModal"
        >Try Our Swiper</a-button
      >
    </div>
    <a-tabs class="tabs" default-active-key="1" @change="switchTabs">
      <a-tab-pane key="1" tab="My Dashboard" force-render>
        <chart :options="option" />
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

export default {
  name: "Favorites",
  components: {
    FavoriteMovieList,
    MovieSwiper,
    chart: ECharts,
    BackToTop
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
            radius: [30, 200],
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
