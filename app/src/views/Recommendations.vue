<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation></Navigation>
    <a-input-search
      :style="{ width: '50%', margin: '25px auto' }"
      placeholder="input search text"
      enter-button
      @search="onSearch"
    />

    <div class="movie-poster">
      <div class="row">
        <div class="col"></div>
        <div class="col"></div>
        <div class="col"></div>
        <div class="col"></div>
      </div>
      <div class="row">
        <div class="col"></div>
        <div class="col"></div>
        <div class="col"></div>
        <div class="col"></div>
      </div>
    </div>
    <div class="movie-slider">
      <Carousel></Carousel>
    </div>
    <div class="movie-swiper">
      <Swiper></Swiper>
    </div>
    <Footer></Footer>
  </a-layout>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Swiper from "@/components/Swiper.vue";
import Carousel from "@/components/Carousel.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    Navigation,
    Swiper,
    Carousel,
    Footer
  },
  methods: {
    onSearch(value) {
      console.log(value);
    }
  }
};
</script>

<style>
.movie-poster {
  margin: 25px;
}

.movie-poster .row {
  display: flex;
}

.movie-poster .col {
  background: gray;
  height: 400px;
  width: 25%;
  margin: 10px;
}

.movie-slider {
  height: 500px;
}

@media screen and (max-width: 1000px) {
  /* applies styles to any device screen sizes below 800px wide */

  .movie-poster .col {
    height: 300px;
    margin: 5px;
  }
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .movie-poster {
    margin: 5px;
  }

  .movie-poster .col {
    height: 100px;
    margin: 5px;
  }

  .movie-slider {
    height: 300px;
    width: 300px;
    margin: 0 auto;
  }

  /* .movie-swiper {
    height: 300px;
    width: 300px;
    margin: 0 auto;
  } */
}
</style>
