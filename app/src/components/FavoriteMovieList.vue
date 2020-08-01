<template>
  <div>
    <ul v-show="errors.length > 0" class="errors">
      <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
    </ul>
    <div v-show="!errors.length">
      <!-- <p v-show="loading">Loading...</p> -->
      <ul class="movie-list">
        <FavoriteMovieCell
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
  border-radius: 4px;
  border: 1px solid white;
  /* border: 1px solid black; */
}

.errors {
  padding: 0;
  color: red;
}
</style>
