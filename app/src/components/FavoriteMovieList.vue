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
.errors {
  padding: 0;
  color: red;
}

.movie-list {
  padding: 1px;
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
</style>
