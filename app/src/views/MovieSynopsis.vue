<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <h1>Movie Synopsis Page</h1>
    <Movie_Synopsis />
    <MovieSynopsisMovieList />
    <MovieSynopsisMovieList listType="Similar Movies" />
    <MovieSynopsisList />
  </a-layout>
</template>

<script scoped>
import Movie_Synopsis from "@/components/MovieSynopsis.vue";
import MovieSynopsisMovieList from "@/components/MovieSynopsisMovieList.vue";
import MovieSynopsisList from "@/components/MovieSynopsisList.vue";
export default {
  name: "MovieSynopsis",
  components: {
    Movie_Synopsis,
    MovieSynopsisMovieList,
    MovieSynopsisList
  }
};
</script>
