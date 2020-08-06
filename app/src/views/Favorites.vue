<template>
  <a-layout>
    <div :style="{ display: 'inline' }">
      <a-button class="swiper-btn" @click="toggleSwiper">
        Try Our Swiper
      </a-button>
    </div>
    <a-tabs class="tabs" default-active-key="1">
      <a-tab-pane key="1" tab="My Dashboard" force-render>
        <ECharts :options="config" v-if="favoriteGenres.length" />
        <h1 class="message" v-else>No Data To Display</h1>
      </a-tab-pane>
      <a-tab-pane key="2" tab="Liked Movies">
        <FavoriteMovieList
          class="favorite-movie"
          :movieList="likedMovies"
          v-if="likedMovies.length"
        />
        <h1 class="message" v-else>You Did Not Liked Any Movies</h1>
      </a-tab-pane>
      <a-tab-pane key="3" tab="Disliked Movies" force-render>
        <FavoriteMovieList
          class="favorite-movie"
          :movieList="dislikedMovies"
          v-if="dislikedMovies.length"
        />
        <h1 class="message" v-else>You Did Not Disliked Any Movies</h1>
      </a-tab-pane>
      <a-tab-pane key="4" tab="Recommendations" force-render>
        <div class="container" v-if="recommendations">
          <img
            class="small-image"
            v-for="(movie, index) in recommendations"
            v-bind:key="index"
            :src="loadImg(movie.poster_path)"
            :alt="movie.title"
            @click="toggleMovie(movie)"
          />
        </div>
        <h1 class="message" v-else>No Recommendation Available</h1>
        <!-- <a-button @click="initialize" :style="{ margin: '25px' }"
          >Initialize
        </a-button>
        <br />
        <a-button @click="request" :style="{ margin: '25px' }"
          >Request
        </a-button>
        <br />
        <a-button @click="reply" :style="{ margin: '25px' }">Reply</a-button> -->
      </a-tab-pane>
    </a-tabs>
    <a-modal
      v-model="movieModal"
      :title="this.movieTitle"
      :width="650"
      :footer="null"
    >
      <div :style="{ display: 'flex' }">
        <p class="content">{{ this.movieSummary }}</p>
        <img
          class="large-image"
          :src="movieImg"
          :alt="movieTitle"
          onerror="this.style.display='none'"
        />
      </div>
      <a-button class="info-btn">
        <router-link
          :to="{ name: 'MovieSynopsis', params: { id: this.movieId } }"
        >
          More Info
        </router-link>
      </a-button>
    </a-modal>
    <a-modal v-model="swiperModal" :width="650" :footer="null">
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
import { eChartsOption } from "../util/eChartsOption";
// import { GENRE_NAME_TO_ID } from "../util/genres";

import axios from "axios";
import FavoriteMovieList from "@/components/FavoriteMovieList.vue";
import MovieSwiper from "@/components/MovieSwiper.vue";
import BackToTop from "@/components/BackToTop.vue";

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
      swiperModal: false,
      config: {},
      recommendations: Array,
      movieModal: false,
      movieId: String,
      movieTitle: String,
      movieImg: String,
      movieSummary: String
    };
  },
  methods: {
    toggleSwiper() {
      this.swiperModal = !this.swiperModal;
    },
    toggleMovie(movie) {
      this.movieModal = !this.movieModal;
      this.movieId = movie.id;
      this.movieTitle = movie.original_title;
      this.movieImg = this.loadImg(movie.poster_path);
      this.movieSummary = movie.overview;
    },
    updateChart(dataset) {
      eChartsOption.series[0].data = dataset;
      this.config = eChartsOption;
    },
    async fetchRecommendations(genres) {
      let topGenres = [];
      genres.map(genre => {
        // topGenres.push(GENRE_NAME_TO_ID[genre.name]);
        topGenres.push(genre.name);
      });
      // console.log("Genre ID", topGenres);
      // console.log("Genre Name", topGenres.join(","));

      if (topGenres.length > 0) {
        try {
          const res = await axios.get(
            "https://binger-api-testv1.azurewebsites.net/movie/search/genre",
            { params: { with_genres: topGenres.join(",") } }
          );
          // console.log(res.data);
          this.recommendations = res.data.results;
        } catch (err) {
          this.error = err;
        }
      }
    },
    loadImg(path) {
      if (path != null) {
        return "https://image.tmdb.org/t/p/w342" + path;
      }
    }
    // async initialize() {
    //   let interestedGenre = "12,14,35,28";
    //   const uid = this.userUID;
    //   console.log(uid);

    //   await axios
    //     .get(
    //       "https://binger-api-testv1.azurewebsites.net/game/recommendation/intialize",
    //       {
    //         params: { user_uid: uid, interested_genres: interestedGenre }
    //       }
    //     )
    //     .then(res => {
    //       console.log(res.data);
    //     })
    //     .catch(err => {
    //       console.log(err);
    //     });
    // },
    // async request() {
    //   const uid = this.userUID;
    //   console.log(uid);

    //   await axios
    //     .get(
    //       "https://binger-api-testv1.azurewebsites.net/game/recommendation/request",
    //       {
    //         params: { user_uid: uid }
    //       }
    //     )
    //     .then(res => {
    //       console.log(res.data);
    //     })
    //     .catch(err => {
    //       console.log(err);
    //     });
    // },
    // async reply() {
    //   const uid = this.userUID;
    //   console.log(uid);

    //   let current_movie_id = 11324;
    //   let current_movie_reply = "like";

    //   await axios
    //     .get(
    //       "https://binger-api-testv1.azurewebsites.net/game/recommendation/reply",
    //       {
    //         params: {
    //           user_uid: uid,
    //           movie_id: current_movie_id,
    //           movie_reply: current_movie_reply
    //         }
    //       }
    //     )
    //     .then(res => {
    //       console.log(res.data);
    //     })
    //     .catch(err => {
    //       console.log(err);
    //     });
    // }
  },
  computed: {
    userUID() {
      return this.$store.state.uid;
    },
    topGenres() {
      return this.$store.getters.topGenres;
    },
    favoriteGenres() {
      return this.$store.state.genres;
    },
    likedMovies() {
      return this.$store.state.likedMovies;
    },
    dislikedMovies() {
      return this.$store.state.dislikedMovies;
    }
  },
  watch: {
    // topGenres(newTopGenres, oldTopGenres) {
    topGenres(newTopGenres) {
      // console.log("Old Top Genres", oldTopGenres);
      // console.log("New Top Genres", newTopGenres);
      this.fetchRecommendations(newTopGenres);
    },
    // favoriteGenres(newGenres, oldGenres) {
    favoriteGenres(newGenres) {
      // console.log("Old Genres", oldGenres);
      // console.log("New Genres", newGenres);
      this.updateChart(newGenres);
    }
  },
  mounted() {
    this.updateChart(this.favoriteGenres);
    this.fetchRecommendations(this.topGenres);
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

.info-btn {
  background-color: transparent;
  color: white;
  border-color: #f3c669;
}

.info-btn:hover {
  background-color: #f3c669;
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

.message {
  color: white;
}

.container {
  margin: 20px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
}

.small-image {
  width: 250px;
  height: 100%;
  margin: 20px 10px;
  object-fit: cover;
}

.small-image:hover {
  opacity: 0.7;
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
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
