<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <!-- <FavoriteMovieList />
    <FavoriteMovieList />
    <FavoriteMovieList /> -->
    <MovieGallery />
  </a-layout>
</template>

<script>
// import FavoriteMovieList from "@/components/FavoriteMovieList.vue";
import MovieGallery from "@/components/MovieGallery.vue";

export default {
  name: "MovieList",
  components: {
    // FavoriteMovieList,
    MovieGallery
  }
};
</script>

<style scoped></style>
