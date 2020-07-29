<template>
  <div>
    <div class="loading" v-if="loading">
      <Loading />
    </div>
    <div v-else>
      <div v-if="random">
        <a-button class="randBtn" @click="fetchMovies(movieUrls)">
          Randomize
        </a-button>
      </div>
      <div class="container">
        <img
          class="small-image"
          v-for="(movie, index) in movieList"
          v-bind:key="index"
          :src="loadImg(movie.poster_path)"
          :alt="movie.title"
          @click="toggleModal(movie)"
        />
      </div>
      <div v-if="random">
        <a-button class="randBtn" @click="fetchMovies(movieUrls)">
          Randomize
        </a-button>
      </div>
      <!-- <Pagination v-else /> -->
      <a-pagination
        class="pageBar"
        :total="totalItems"
        v-model="currentPage"
        @change="pageUpdate"
        :defaultPageSize="20"
        v-else
      />
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
import Loading from "@/components/Loading.vue";
// import Pagination from "@/components/Pagination.vue";

export default {
  name: "MovieGallery",
  components: {
    Loading
    // Pagination
  },
  props: {
    url: String,
    random: Boolean
  },
  data() {
    return {
      loading: false,
      modalVisible: false,
      modalId: String,
      modalTitle: String,
      modalImg: String,
      modalSummary: String,
      movieList: Array,
      movieUrls: this.url,
      currentPage: 1,
      totalItems: 0
    };
  },
  mounted() {
    this.fetchMovies(this.movieUrls);
  },
  watch: {
    $route() {
      this.fetchMovies(this.movieUrls);
    }
  },
  methods: {
    pageUpdate(page) {
      this.currentPage = page;
      this.$router.push({
        name: "MovieList",
        params: { path: this.$route.params.path },
        query: { current_page: this.currentPage }
      });
      this.fetchMovies(this.movieUrls, page);
    },
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
        if (this.random) {
          const res = await axios.get(url);
          this.movieList = res.data;
        } else {
          const res = await axios.get(url, {
            params: { page: this.$route.query.current_page }
          });
          this.totalItems = 500;
          this.movieList = res.data;
        }
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = !this.loading;
      }
    }
  }
};
</script>

<style scoped>
.container {
  margin: 20px 150px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
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

.small-image {
  margin: 20px 10px;
  width: 250px;
  height: 100%;
  object-fit: cover;
}

.small-image:hover {
  opacity: 0.7;
}

.loading {
  position: absolute;
  top: 50%;
  left: 1%;
  right: 1%;
}

.pageBar {
  margin: 20px;
}

.randBtn {
  margin: 20px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .content {
    margin: 0 auto;
    font-size: 5px;
  }
}
</style>
