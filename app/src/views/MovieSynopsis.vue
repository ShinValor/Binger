<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Movie_Synopsis />
    <MovieSynopsisMovieList />
    <MovieSynopsisMovieList listType="Similar Movies" />
    <MovieSynopsisCastList />
  </a-layout>
</template>

<script scoped>
import Movie_Synopsis from "@/components/MovieSynopsis.vue";
import MovieSynopsisMovieList from "@/components/MovieSynopsisMovieList.vue";
import MovieSynopsisCastList from "@/components/MovieSynopsisCastList.vue";
export default {
  name: "MovieSynopsis",
  components: {
    Movie_Synopsis,
    MovieSynopsisMovieList,
    MovieSynopsisCastList
  }
};
</script>
<style scoped></style>
