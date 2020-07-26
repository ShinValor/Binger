<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <!-- <FavoriteMovieList /> -->
    <MovieGallery />
    <MovieGallery />
    <MovieGallery />
    <Pagination />
  </a-layout>
</template>

<script>
// import FavoriteMovieList from "@/components/FavoriteMovieList.vue";
import MovieGallery from "@/components/MovieGallery.vue";
import Pagination from "@/components/Pagination.vue";

export default {
  name: "MovieList",
  components: {
    // FavoriteMovieList,
    MovieGallery,
    Pagination
  }
};
</script>

<style scoped></style>
