<template>
  <div>
    <ul class="list">
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
        <a-button>
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
      axios
        .get("https://binger-api-testv1.azurewebsites.net//movie/search", {
          params: { query: this.movieQuery, page: this.currentPage }
        })
        .then(res => {
          this.list = res.data.results;
          this.totalItems = res.data.total_results;
        })
        .catch(err => {
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
    genres: function() {
      var _genres = [];
      this.item.genres.forEach(function(genre) {
        _genres.push(genre);
      });
      return _genres.join(", ");
    },
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
.list {
  padding: 0;
  /* border-radius: 4px; */
  /* border: 1px solid #e0e0e0; */
  /* border: 1px solid black; */
}

.errors {
  padding: 0;
  color: red;
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

.pagination {
  margin: 20px;
}

.movie-cell {
  /* display: inline-block; */
  /* vertical-align: middle; */
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: transform;
  transition-property: transform;
  -webkit-transition-timing-function: ease-out;
  transition-timing-function: ease-out;
}

.movie-cell:hover {
  transform: scale(1.01);
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
}
</style>
