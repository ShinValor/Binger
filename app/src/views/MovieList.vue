<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <MovieGallery
      :random="this.$route.params.random"
      :url="
        'https://binger-api-testv1.azurewebsites.net/movie/' + this.$route.params.path"
    />
  </a-layout>
</template>

<script>
import MovieGallery from "@/components/MovieGallery.vue";
// import Pagination from "@/components/Pagination.vue";

export default {
  name: "MovieList",
  components: {
    MovieGallery
    // Pagination
  }
};
</script>

<style scoped></style>
