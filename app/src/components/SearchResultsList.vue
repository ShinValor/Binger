<template>
  <div>
    <ul class="movie-list">
      <SearchResultsCell
        class="movie-cell"
        v-for="item in list"
        :key="item.title"
        :item="item"
        @click.native="toggleModal(item)"
      />
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
    </ul>
    <a-pagination
      class="pagination"
      :total="totalItems"
      v-model="currentPage"
      @change="pageUpdate"
      :defaultPageSize="20"
    />
  </div>
</template>

<script>
import SearchResultsCell from "./SearchResultsCell.vue";
import axios from "axios";

export default {
  components: {
    SearchResultsCell
  },
  props: {
    movieQuery: {
      type: String,
      default: ""
    },
    genreQuery: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      loading: true,
      list: Array,
      errors: [],

      currentPage: 1,
      totalItems: 0,

      modalVisible: false,
      modalId: String,
      modalTitle: String,
      modalImg: String,
      modalSummary: String
    };
  },
  methods: {
    pageUpdate(page) {
      this.currentPage = page;
      this.fetchResults();
    },
    fetchResults() {
      let queryParams, link;
      // console.log(
      //   "moviequery: " + this.movieQuery + "genrequery: " + this.genreQuery
      // );
      if (this.movieQuery || this.movieQuery !== "") {
        queryParams = { query: this.movieQuery, page: this.currentPage };
        link = "https://binger-api-testv1.azurewebsites.net/movie/search";
        // link = "http://127.0.0.1:5000/movie/search";
      } else if (this.genreQuery || this.genreQuery !== "") {
        // console.log("going to the else");
        queryParams = { with_genres: this.genreQuery, page: this.currentPage };
        link = "https://binger-api-testv1.azurewebsites.net/movie/search/genre";
        // link = "http://127.0.0.1:5000/movie/search/genre";
      }
      axios
        .get(link, { params: queryParams })
        .then(res => {
          // console.log("data", res);
          this.list = res.data.results;
          this.totalItems = res.data.total_results;
        })
        .catch(err => {
          // console.log("error " + err);
          this.error = err;
        });
    },
    toggleModal(movie) {
      this.modalVisible = !this.modalVisible;
      this.modalId = movie.id;
      this.modalTitle = movie.original_title;
      this.modalImg = this.resolve_img_url(movie.poster_path);
      this.modalSummary = movie.overview;
    },
    resolve_img_url(path) {
      if (path !== null) {
        return "https://image.tmdb.org/t/p/w342" + path;
      }
      return "https://storage.cloud.google.com/image-api-phot-bucket/default_poster.jpg";
    }
  },
  computed: {
    overview: function() {
      return this.item.overview.length < 200
        ? this.item.overview
        : this.item.overview.substring(0, 200) + "...";
    },
    releaseDate: function() {
      const msec = Date.parse(this.item.release_date);
      const date = new Date(msec);
      return date.toLocaleString("default", {
        year: "numeric",
        month: "long",
        day: "numeric"
      });
    }
  },
  created() {
    this.fetchResults();
  }
};
</script>

<style scoped>
.errors {
  padding: 0;
  color: red;
}

.movie-list {
  padding: 0;
}

.movie-cell {
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  transform: perspective(1px) translateZ(0);
  -webkit-transform: perspective(1px) translateZ(0);
  transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  transition-property: transform;
  -webkit-transition-property: transform;
  transition-timing-function: ease-out;
  -webkit-transition-timing-function: ease-out;
}

.movie-cell:hover {
  transform: scale(1.01);
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

.info-btn {
  background-color: transparent;
  color: white;
  border-color: #f3c669;
}

.info-btn:hover {
  background-color: #f3c669;
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
}

.pagination {
  margin: 20px auto;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    margin: 0px;
    font-size: 8px;
  }

  .content {
    margin: 0 auto;
    font-size: 5px;
  }

  .pagination {
    width: 100%;
  }
}
</style>
