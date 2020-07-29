<template>
  <div>
    <div v-if="loading">
      <Loading />
    </div>
    <flickity class="carousel" ref="flickity" :options="flickityOptions" v-else>
      <div
        class="carousel-cell"
        v-for="(movie, index) in movieList"
        v-bind:key="index"
        @click="toggleModal(movie)"
      >
        <img
          class="carousel-cell-image"
          :data-flickity-lazyload="loadImg(movie.poster_path)"
          :alt="movie.title"
          onerror="this.style.display='none'"
        />
        <div class="carousel-cell-desc">
          <h1 class="title">{{ movie.title }}</h1>
          <p class="content" :style="{ color: 'gray' }">
            <a-icon type="like" /> {{ movie.vote_count }} Votes
          </p>
        </div>
      </div>
    </flickity>
    <a-modal
      v-model="modalVisible"
      :title="modalTitle"
      :width="750"
      :footer="null"
    >
      <div :style="{ display: 'flex' }">
        <p class="content">{{ this.modalSummary }}</p>
        <img
          class="large-image"
          :src="modalImg"
          :alt="modalTitle"
          onerror="this.style.display='none'"
        />
      </div>
      <a-button>
        <router-link
          :to="{ name: 'MovieSynopsis', params: { id: this.modalId } }"
        >
          More Info
        </router-link>
      </a-button>
    </a-modal>
  </div>
</template>

<script>
import axios from "axios";
import Flickity from "vue-flickity";
import Loading from "@/components/Loading.vue";

export default {
  name: "Carousel",
  components: {
    Flickity,
    Loading
  },
  props: {
    url: String
  },
  data() {
    return {
      loading: false,
      flickityOptions: {
        initialIndex: 0,
        groupCells: 5,
        freeScroll: true,
        lazyLoad: 2
        // autoPlay: 3000,
      },
      modalVisible: false,
      modalId: String,
      modalTitle: String,
      modalImg: String,
      modalSummary: String,
      movieList: Array,
      movieUrls: this.url
    };
  },
  mounted() {
    this.fetchMovies(this.movieUrls);
  },
  methods: {
    toggleModal(movie) {
      this.modalVisible = !this.modalVisible;
      this.modalId = movie.id;
      this.modalTitle = movie.original_title;
      this.modalImg = this.loadImg(movie.poster_path);
      this.modalSummary = movie.overview;
    },
    loadImg(path) {
      if (path !== null || path !== undefined) {
        return "https://image.tmdb.org/t/p/w342" + path;
      }
    },
    async fetchMovies(url) {
      try {
        this.loading = !this.loading;
        const res = await axios.get(url);
        this.movieList = res.data;
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = !this.loading;
        this.$refs.flickity.rerender();
      }
    }
  }
};
</script>

<style scoped>
.carousel {
  margin: 10px 10px 50px;
}

.carousel-cell {
  /* background-color: #222; */
  height: 500px;
  width: 20%;
  display: flex;
  flex-direction: column;
  /* justify-content: flex-start; */
  margin-right: 4px;
  /* padding: 0 2px; */
}

.carousel-cell-image {
  max-height: 100%;
  max-width: 100%;
  /* margin: 0 auto; */
  /* display: block; */
  object-fit: cover;
  opacity: 0;
  -webkit-transition: opacity 0.4s;
  transition: opacity 0.4s;
}

.carousel-cell:hover {
  opacity: 0.7;
}

.carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
}

.carousel-cell-desc {
  background-color: #001528;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.title {
  margin: 5px;
  font-size: 20px;
  color: white;
}

.content {
  width: 66%;
  margin: 5px auto;
  font-size: 15px;
  /* color: white; */
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
    margin: 0px 0px 50px;
  }

  .carousel-cell {
    height: 150px;
    margin-right: 0px;
  }

  .title {
    margin: 0px;
    font-size: 8px;
  }

  .content {
    margin: 0 auto;
    font-size: 5px;
  }
}
</style>
