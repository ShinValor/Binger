<template>
  <a-layout>
    <MovieGallery
      class="movie-gallery"
      :random="this.$route.params.random"
      :url="
        'https://binger-api-testv1.azurewebsites.net/movie/' +
          // eslint-disable-next-line prettier/prettier
          this.$route.params.path"/>
    <Footer class="footer" />
    <BackToTop />
  </a-layout>
</template>

<script>
import MovieGallery from "@/components/MovieGallery.vue";
import BackToTop from "@/components/BackToTop.vue";
// import Pagination from "@/components/Pagination.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "MovieList",
  components: {
    MovieGallery,
    BackToTop,
    // Pagination
    Footer
  }
};
</script>

<style scoped>
.movie-gallery {
  margin: 50px auto;
}

.footer {
  margin-top: 50px;
}
</style>
