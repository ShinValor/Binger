<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <h1>Movie Synopsis Page</h1>
    <Movie_Synopsis />
  </a-layout>
</template>

<script scoped>
import Movie_Synopsis from "@/components/MovieSynopsis.vue";
export default {
  name: "MovieSynopsis",
  components: {
    Movie_Synopsis
  }
};
</script>
