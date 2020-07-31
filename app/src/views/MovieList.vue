<template>
  <a-layout
    :style="{ minHeight: '100%', overflow: 'auto', position: 'relative' }"
  >
    <MovieGallery
      :random="this.$route.params.random"
      :url="
        'https://binger-api-testv1.azurewebsites.net/movie/' +
          // eslint-disable-next-line prettier/prettier
          this.$route.params.path"/>
    <Footer class="footer" />
  </a-layout>
</template>

<script>
import MovieGallery from "@/components/MovieGallery.vue";
// import Pagination from "@/components/Pagination.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "MovieList",
  components: {
    MovieGallery,
    // Pagination
    Footer
  }
};
</script>

<style scoped>
.footer {
  margin-top: 50px;
}
</style>
