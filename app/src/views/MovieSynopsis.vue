<template>
  <a-layout>
    <MovieOverview
      :key="this.$route.params.id + 'Synopsis'"
      :movieID="parseInt(this.$route.params.id)"
    />
    <MovieSynopsisMovieList
      listType="Movie Recommendations"
      :movieID="parseInt(this.$route.params.id)"
      :key="this.$route.params.id + 'Recommendation'"
    />
    <MovieSynopsisMovieList
      listType="Similar Movies"
      :movieID="parseInt(this.$route.params.id)"
      :key="this.$route.params.id + 'Similiar'"
    />
    <MovieSynopsisCastList
      :key="this.$route.params.id + 'CastList'"
      :movieID="parseInt(this.$route.params.id)"
    />
    <Footer :style="{ 'margin-top': '50px' }" />
  </a-layout>
</template>

<script>
import MovieSynopsisMovieList from "@/components/MovieSynopsisMovieList.vue";
import MovieSynopsisCastList from "@/components/MovieSynopsisCastList.vue";
import MovieOverview from "@/components/MovieOverview.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "MovieSynopsis",
  components: {
    MovieOverview,
    MovieSynopsisMovieList,
    MovieSynopsisCastList,
    Footer
  }
};
</script>

<style scoped></style>
