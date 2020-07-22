<template>
  <a-layout class="container">
    <SearchBar />
    <div v-if="loading">
      <Loading />
    </div>
    <div :style="{ width: '90%', margin: '0 auto' }" v-else>
      <!-- <a-tabs class="tabs">
        <a-tab-pane key="1" tab="Top Rated">
          <h1 class="title">Top Rated</h1>
          <Carousel />
        </a-tab-pane>
        <a-tab-pane key="2" tab="Worst Rated">
          <h1 class="title">Worst Rated</h1>
          <Carousel />
        </a-tab-pane>
        <a-tab-pane key="3" tab="Most Popular">
          <h1 class="title">Most Popular</h1>
          <Carousel />
        </a-tab-pane>
        <a-tab-pane key="4" tab="Least Popular">
          <h1 class="title">Least Popular</h1>
          <Carousel />
        </a-tab-pane>
        <a-tab-pane key="5" tab="Most Recent">
          <h1 class="title">Most Recent</h1>
          <Carousel />
        </a-tab-pane>
        <a-tab-pane key="6" tab="Oldest">
          <h1 class="title">Oldest Movie</h1>
          <Carousel />
        </a-tab-pane>
      </a-tabs>-->
      <h1 class="title">Top Rated</h1>
      <Carousel :url="'https://binger-api-testv1.azurewebsites.net/movie/ratings/best'" />
      <h1 class="title">Worst Rated</h1>
      <Carousel :url="'https://binger-api-testv1.azurewebsites.net/movie/ratings/worst'" />
      <h1 class="title">Most Popular</h1>
      <Carousel :url="'https://binger-api-testv1.azurewebsites.net/movie/popular'" />
      <h1 class="title">Least Popular</h1>
      <Carousel :url="'https://binger-api-testv1.azurewebsites.net/movie/unpopular'" />
      <h1 class="title">Most Recent</h1>
      <Carousel :url="'https://binger-api-testv1.azurewebsites.net/movie/latest'" />
      <h1 class="title">Oldest Movie</h1>
      <Carousel :url="'https://binger-api-testv1.azurewebsites.net/movie/oldest'" />
    </div>
    <Footer></Footer>
  </a-layout>
</template>

<script>
import firebase from "firebase";
import axios from "axios";
import SearchBar from "@/components/SearchBar.vue";
import Carousel from "@/components/Carousel.vue";
import Loading from "@/components/Loading.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    SearchBar,
    Carousel,
    Loading,
    Footer
  },
  data() {
    return {
      loading: true,
      userToken: String,
      movieQuery: String,
      movies: {
        best: {},
        worst: {},
        popular: {},
        unpopular: {},
        latest: {},
        oldest: {}
      }
    };
  },
  methods: {
    async fetchMovies() {
      this.loading = true;
      await axios
        .all([
          axios.get(
            "https://binger-api-testv1.azurewebsites.net/movie/ratings/worst"
          ),
          axios.get(
            "https://binger-api-testv1.azurewebsites.net/movie/ratings/best"
          ),
          axios.get(
            "https://binger-api-testv1.azurewebsites.net/movie/popular"
          ),
          axios.get(
            "https://binger-api-testv1.azurewebsites.net/movie/unpopular"
          ),
          axios.get("https://binger-api-testv1.azurewebsites.net/movie/latest"),
          axios.get("https://binger-api-testv1.azurewebsites.net/movie/oldest")
        ])
        .then(
          axios.spread((best, worst, popular, unpopular, latest, oldest) => {
            this.movies["best"] = best;
            this.movies["worst"] = worst;
            this.movies["popular"] = popular;
            this.movies["unpopular"] = unpopular;
            this.movies["latest"] = latest;
            this.movies["oldest"] = oldest;
          })
        )
        .catch(error => {
          this.error = error.message;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  },
  created() {
    firebase.auth().onAuthStateChanged(user => {
      // user.getIdToken().then(token => {
      //   this.userToken = token;
      // });
      if (!user) {
        this.$router.replace({ name: "Home" });
      }
    });
  },
  mounted() {
    this.fetchMovies();
  }
};
</script>

<style scoped>
.container {
  min-height: 100%;
  overflow: auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.tabs {
  width: 90%;
  margin: 50px auto 25px;
}

.search-bar {
  width: 50%;
  margin: 50px auto 25px;
}

.title {
  margin: 20px;
  text-align: left;
  font-size: 30px;
  color: white;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .tabs {
    width: 100%;
    margin: 0 auto;
  }

  .search-bar {
    width: 75%;
    margin: 15px auto;
  }

  .title {
    margin: 0 auto;
    text-align: center;
    font-size: 20px;
  }
}
</style>
