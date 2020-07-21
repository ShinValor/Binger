<template>
  <div class="container">
    <h1 class="title">{{ listType }}</h1>
    <Carousel :url="moviesUrl" />
  </div>
</template>

<script>
import Carousel from "@/components/Carousel.vue";

export default {
  name: "MovieSynopsisMovieList",
  components: {
    Carousel
  },
  data() {
    return {
      movieList: Array,
      moviesUrl: String
    };
  },
  props: {
    movieID: {
      type: Number,
      required: true
    },
    listType: {
      type: String,
      default: "Movie Recommendations"
    }
  },
  created() {
    if (this.listType == "Movie Recommendations") {
      this.moviesUrl =
        "/api/movie/recommendations/" + this.movieID;
    } else {
      this.moviesUrl = "/api/movie/similar/" + this.movieID;
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
  color: white;
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
