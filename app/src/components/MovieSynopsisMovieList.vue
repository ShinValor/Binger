<template>
  <div class="container">
    <h1 class="title">{{ listType }}</h1>
    <Carousel :movieList="MovieList" />
    <!-- <div class="container">
      <flickity class="carousel" ref="flickity" :options="flickityOptions">
        <div
          class="carousel-cell"
          v-for="(item, index) in MovieList"
          v-bind:key="index"
        >
          <router-link :to="{ name: 'MovieSynopsis', params: { id: item.id } }">
            <img
              class="carousel-cell-image"
              :src="resolve_img_url(item.poster_path, item.title)"
            />
          </router-link>
        </div>
      </flickity>
    </div> -->
  </div>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import axios from "axios";

export default {
  name: "MovieSynopsisMovieList",
  components: {
    Carousel
  },
  data() {
    return {
      selectedMovie: Object,
      MovieList: Array,
      errors: Array
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
    let link;
    if (this.listType == "Movie Recommendations") {
      link = "http://127.0.0.1:5000/movie/recommendations/" + this.movieID;
    } else {
      link = "http://127.0.0.1:5000/movie/similar/" + this.movieID;
    }
    axios
      .get(link)
      .then(response => {
        this.MovieList = response.data;
      })
      .catch(error => {
        this.errors = error;
      });
    // .finally(() => this.$refs.flickity.rerender());
  },
  methods: {
    resolve_img_url: function(path, title) {
      console.log("https://image.tmdb.org/t/p/w342" + path, title);
      return "https://image.tmdb.org/t/p/w342" + path;
    },
    imgsLoaded() {
      // Reload flickity cells due to height change post
      // this.$refs.flickity.reloadCells();
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
