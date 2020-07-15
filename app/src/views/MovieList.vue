<template>
  <a-layout>
    <FavoriteMovieList />
    <FavoriteMovieList />
    <FavoriteMovieList />
  </a-layout>
</template>

<script scoped>
import FavoriteMovieList from "@/components/FavoriteMovieList.vue";

export default {
  name: "MovieList",
  components: {
    FavoriteMovieList
  }
};
</script>

<style scoped></style>
