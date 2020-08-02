<template>
  <div>
    <ul v-show="errors.length > 0" class="errors">
      <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
    </ul>
    <div v-show="!errors.length">
      <!-- <p v-show="loading">Loading...</p> -->
      <ul class="movie-list">
        <FavoriteMovieCell
          class="movie-cell"
          v-for="item in movieList"
          :key="item.title"
          :item="item"
        />
      </ul>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import FavoriteMovieCell from "./FavoriteMovieCell.vue";
export default {
  components: {
    FavoriteMovieCell
  },
  props: {
    movieList: {}
  },
  data() {
    return {
      loading: true,
      errors: []
    };
  }
};
</script>

<style scoped>
.movie-list {
  padding: 1px;
  /* border: 1px solid white; */
  /* border-radius: 4px; */
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

.errors {
  padding: 0;
  color: red;
}
</style>
