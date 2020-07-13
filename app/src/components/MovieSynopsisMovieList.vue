<template>
  <div class="container">
    <h1 class="title">{{ listType }}</h1>
    <Carousel />
  </div>
</template>
<script>
import Carousel from "@/components/Carousel.vue";

export default {
  name: "MovieSynopsisMovieList",
  components: {
    Carousel
  },
  props: {
    listType: {
      type: String,
      default: "No Title"
    }
  }
};
</script>
<style scoped>
.container {
  margin: 2.5em;
}

.title {
  margin: 20px;
  text-align: left;
  font-size: 30px;
}

.content {
  width: 66%;
  margin: 5px;
  font-size: 15px;
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    margin: 0 auto;
    text-align: center;
    font-size: 20px;
  }
}
</style>
