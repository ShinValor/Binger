<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation></Navigation>
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
    <Swiper></Swiper>
    <Footer></Footer>
  </a-layout>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Swiper from "@/components/Swiper.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    Navigation,
    Swiper,
    Footer
  }
};
</script>

<style>
.movie-poster {
  margin: 50px;
}

.row {
  display: flex;
}

.col {
  background: gray;
  height: 400px;
  width: 25%;
  margin: 10px;
}
</style>
