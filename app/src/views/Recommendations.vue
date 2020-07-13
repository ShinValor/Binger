<template>
  <a-layout class="container">
    <a-input-search
      class="search-bar"
      placeholder="Search Movies"
      enter-button
      @search="onSearch"
    />
    <a-tabs class="tabs">
      <a-tab-pane key="1" tab="Random">
        <h1 class="title">Movies You Might Like</h1>
        <Carousel />
        <!-- <DisplayMovie /> -->
        <h1 class="title">Movies Other Liked</h1>
        <Carousel />
        <!-- <DisplayMovie /> -->
      </a-tab-pane>
      <a-tab-pane key="2" tab="Top Rated">
        <h1 class="title">Action Movies</h1>
        <DisplayMovie />
        <h1 class="title">Comedy Movies</h1>
        <DisplayMovie />
      </a-tab-pane>
      <a-tab-pane key="3" tab="Most Popular">
        <h1 class="title">Action Movies</h1>
        <DisplayMovie />
        <h1 class="title">Comedy Movies</h1>
        <DisplayMovie />
      </a-tab-pane>
      <a-tab-pane key="4" tab="Most Recent">
        <h1 class="title">Action Movies</h1>
        <DisplayMovie />
        <h1 class="title">Comedy Movies</h1>
        <DisplayMovie />
      </a-tab-pane>
      <a-tab-pane key="5" tab="Least Popular">
        <h1 class="title">Action Movies</h1>
        <DisplayMovie />
        <h1 class="title">Comedy Movies</h1>
        <DisplayMovie />
      </a-tab-pane>
      <a-tab-pane key="6" tab="Oldest">
        <h1 class="title">Action Movies</h1>
        <DisplayMovie />
        <h1 class="title">Comedy Movies</h1>
        <DisplayMovie />
      </a-tab-pane>
    </a-tabs>
    <Footer></Footer>
  </a-layout>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import DisplayMovie from "@/components/DisplayMovie.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    Carousel,
    DisplayMovie,
    Footer
  },
  data() {
    return {
      query: String
    };
  },
  methods: {
    onSearch(value) {
      this.query = value;
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
    font-size: 15px;
  }
}
</style>
