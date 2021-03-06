<template>
  <div v-if="movieList.length">
    <div v-if="loading">
      <Loading />
    </div>
    <div v-else>
      <flickity
        class="carousel"
        ref="flickity"
        :options="flickityOptions"
        @init="onInit"
      >
        <div
          class="carousel-cell"
          v-for="(movie, index) in movieList"
          v-bind:key="index"
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
              <a-icon type="like" />
              {{ movie.vote_count }} Votes
            </p>
          </div>
        </div>
      </flickity>
    </div>
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
      <a-button class="info-btn">
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
    onInit() {
      let vm = this;
      this.$refs.flickity.on("staticClick", function(
        event,
        pointer,
        cellElement,
        cellIndex
      ) {
        // console.log(event, pointer, cellElement, cellIndex);
        vm.toggleModal(cellIndex);
      });
    },
    toggleModal(cellIndex) {
      let movie = this.movieList[cellIndex];
      this.modalVisible = !this.modalVisible;
      this.modalId = movie.id;
      this.modalTitle = movie.original_title;
      this.modalImg = this.loadImg(movie.poster_path);
      this.modalSummary = movie.overview;
    },
    loadImg(path) {
      if (path != null) {
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
  width: 20%;
  height: 500px;
  margin-right: 4px;
  display: flex;
  flex-direction: column;
}

.carousel-cell-image {
  max-height: 100%;
  max-width: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.4s;
  -webkit-transition: opacity 0.4s;
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
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
}

.info-btn {
  background-color: transparent;
  color: white;
  border-color: #f3c669;
}

.info-btn:hover {
  background-color: #f3c669;
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
