<template>
  <a-layout class="container">
    <SearchBar class="search-bar" />
    <div class="recommendation-list">
      <div class="header">
        <h1 class="title">Random</h1>
        <a-button class="view-btn" @click="onMore('/random', true)">
          <font-awesome-icon :icon="['fas', 'random']" />
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/random'"
      />
      <div class="header">
        <h1 class="title">Top Rated</h1>
        <a-button class="view-btn" @click="onMore('/ratings/best', false)">
          View More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/ratings/best'"
      />
      <div class="header">
        <h1 class="title">Worst Rated</h1>
        <a-button class="view-btn" @click="onMore('/ratings/worst', false)">
          View More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/ratings/worst'"
      />
      <div class="header">
        <h1 class="title">Most Popular</h1>
        <a-button class="view-btn" @click="onMore('/popular', false)">
          View More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/popular'"
      />
      <div class="header">
        <h1 class="title">Least Popular</h1>
        <a-button class="view-btn" @click="onMore('/unpopular', false)">
          View More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/unpopular'"
      />
      <div class="header">
        <h1 class="title">Most Recent</h1>
        <a-button class="view-btn" @click="onMore('/latest', false)">
          View More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/latest'"
      />
      <div class="header">
        <h1 class="title">Oldest Movie</h1>
        <a-button class="view-btn" @click="onMore('/oldest', false)">
          View More
        </a-button>
      </div>
      <Carousel
        :url="'https://binger-api-testv1.azurewebsites.net/movie/oldest'"
      />
    </div>
    <Footer :style="{ 'margin-top': '50px' }" />
  </a-layout>
</template>

<script>
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
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.recommendation-list {
  width: 90%;
  margin: 0 auto;
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
  margin: 20px 10px;
  font-size: 30px;
  color: white;
}

.view-btn {
  width: 100px;
  height: 100%;
  margin: 20px;
  padding: 5px 10px;
  background-color: transparent;
  border-color: #f3c669;
  color: white;
}

.view-btn:hover {
  background-color: #f3c669;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .search-bar {
    width: 75%;
    margin: 25px auto;
  }

  .title {
    margin: 0;
    font-size: 20px;
  }

  .view-btn {
    width: 75px;
    margin: 5px 0;
    padding: 5px;
    font-size: 10px;
  }
}
</style>
