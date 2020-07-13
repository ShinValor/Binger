<template>
  <div class="card">
    <h2 class="carousel-type-text">{{ listType }}</h2>
    <flickity class="carousel" ref="flickity" :options="flickityOptions">
      >
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
  </div>
</template>

<script>
import Flickity from "vue-flickity";
import axios from "axios";
export default {
  name: "MovieSynopsisMovieList",
  components: {
    Flickity
  },
  data() {
    return {
      selectedMovie: Object,
      MovieList: Array,
      errors: Array,
      flickityOptions: {
        initialIndex: 0,
        autoPlay: 3000,
        groupCells: 5,
        freeScroll: true
        // prevNextButtons: false
      },
      visible: false
    };
  },
  props: {
    movieID: {
      type: Number,
      required: true
    },
    listType: {
      type: String,
      default: "Movie Reccomendations"
    }
  },
  created() {
    let link;
    if (this.listType == "Movie Reccomendations") {
      link = "http://127.0.0.1:5000/movie/recommendations/" + this.movieID;
    } else {
      link = "http://127.0.0.1:5000/movie/similar/" + this.movieID;
    }

    axios
      .get(link)
      .then(response => {
        if (response && response.status === 200) {
          this.MovieList = response.data;
        }
      })
      .catch(error => {
        this.errors = error;
      })
      .finally(() => this.$refs.flickity.rerender());
  },
  methods: {
    resolve_img_url: function(path, title) {
      console.log("https://image.tmdb.org/t/p/w342" + path, title);
      return "https://image.tmdb.org/t/p/w342" + path;
    },
    onClick() {
      // console.log("More");
    },
    imgsLoaded() {
      // Reload flickity cells due to height change post
      let flickityInstance = this.$refs.flickity;
      flickityInstance.reloadCells();
    }
  }
};
</script>
<style scoped>
.carousel {
  margin: 10px 20px;
}

.carousel-cell {
  height: 400px;
  width: 20%;
  margin: 0px;
  display: flex;
  justify-content: center;
}

.carousel-cell-image {
  max-height: 100%;
  max-width: 100%;
  margin: 0 auto;
  display: block;
  object-fit: cover;
}

.carousel-cell-image:hover {
  opacity: 0.7;
}

/* .carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
} */

.container {
  display: flex;
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
  .carousel {
    margin: 5px;
  }

  .carousel-cell {
    height: 100px;
    margin: 0px 5px;
  }
}
.card {
  margin: 2.5em;
}
.carousel-type-text {
  text-align: left;
  font-size: 2em;
  margin-bottom: 0%;
  margin-top: 1rem;
}
</style>
