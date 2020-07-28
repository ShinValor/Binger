<template>
  <a-layout class="container">
    <SearchBar class="searchBar" />
    <div :style="{ width: '90%', margin: '0 auto' }">
      <div class="header">
        <h1 class="title">Random</h1>
        <a-button class="more-btn" @click="onMore('/random', true)">
          More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/random'"
      />
      <div class="header">
        <h1 class="title">Top Rated</h1>
        <a-button class="more-btn" @click="onMore('/ratings/best', false)">
          More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/ratings/best'"
      />
      <div class="header">
        <h1 class="title">Worst Rated</h1>
        <a-button class="more-btn" @click="onMore('/ratings/worst', false)">
          More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/ratings/worst'"
      />
      <div class="header">
        <h1 class="title">Most Popular</h1>
        <a-button class="more-btn" @click="onMore('/popular', false)">
          More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/popular'"
      />
      <div class="header">
        <h1 class="title">Least Popular</h1>
        <a-button class="more-btn" @click="onMore('/unpopular', false)">
          More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/unpopular'"
      />
      <div class="header">
        <h1 class="title">Most Recent</h1>
        <a-button class="more-btn" @click="onMore('/latest', false)">
          More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/latest'"
      />
      <div class="header">
        <h1 class="title">Oldest Movie</h1>
        <a-button class="more-btn" @click="onMore('/oldest', false)">
          More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/oldest'"
      />
    </div>
    <Footer />
  </a-layout>
</template>

<script>
import firebase from "firebase";
import SearchBar from "@/components/SearchBar.vue";
import Carousel from "@/components/Carousel.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    SearchBar,
    Carousel,
    Footer
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
  methods: {
    onMore(path, random) {
      if (random) {
        this.$router.push({
          name: "MovieList",
          params: { path: path, random: random }
        });
      } else {
        this.$router.push({
          name: "MovieList",
          params: { path: path },
          query: { current_page: 1 }
        });
      }
    }
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

.search-bar {
  width: 50%;
  margin: 50px auto 25px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title {
  margin: 20px;
  /* text-align: left; */
  font-size: 30px;
  color: white;
}

.more-btn {
  /* width: 100%; */
  height: 100%;
  margin: 20px;
  padding: 5px 20px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .search-bar {
    width: 75%;
    margin: 15px auto;
  }

  .title {
    margin: 0;
    /* text-align: center; */
    font-size: 20px;
  }

  .more-btn {
    margin: 5px 0;
    padding: 2px 5px;
  }
}
</style>
