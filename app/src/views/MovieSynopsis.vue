<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <h1>Movie Synopsis Page</h1>
    <Movie_Synopsis />
    <MovieSynopsisCast />
    <MovieTrailerCarousel />
    <MovieSynopsisMovie />
    <MovieSynopsisMovie listType="Similar Movies" />
  </a-layout>
</template>

<script scoped>
import Movie_Synopsis from "@/components/MovieSynopsis.vue";
import MovieTrailerCarousel from "@/components/MovieTrailerCarousel.vue";
import MovieSynopsisMovie from "@/components/MovieSynopsisMovie.vue";
import MovieSynopsisCast from "@/components/MovieSynopsisCast.vue";
export default {
  name: "MovieSynopsis",
  components: {
    Movie_Synopsis,
    MovieTrailerCarousel,
    MovieSynopsisMovie,
    MovieSynopsisCast
  }
};
</script>
