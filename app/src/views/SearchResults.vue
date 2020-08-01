<template>
  <a-layout class="container">
    <SearchBar class="searchBar" :movieQuery="searchQuery" />
    <SearchResultsList
      class="searchList"
      :movieQuery="searchTitleQuery"
      :genreQuery="searchGenreQuery"
      :key="searchTitleQuery + searchGenreQuery"
    />
    <Footer />
  </a-layout>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";
import SearchResultsList from "@/components/SearchResultsList.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "SearchResults",
  components: {
    SearchBar,
    SearchResultsList,
    Footer
  },
  computed: {
    searchTitleQuery: function() {
      if (this.$route.query.movieQuery) {
        return this.$route.query.movieQuery;
      }
      return "";
    },
    searchGenreQuery: function() {
      console.log(this.$route.query.with_genres)
      if (this.$route.query.with_genres) {
        return this.$route.query.with_genres;
      }
      return "";
    },
  }
};
</script>

<style scoped>
.container {
  min-height: 100%;
  overflow: auto;
}

.searchBar {
  width: 50%;
  margin: 50px auto 25px;
}

.searchList {
  margin: 25px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .searchBar {
    width: 75%;
    margin: 15px auto;
  }

  .searchList {
    margin: 15px 10px;
  }
}
</style>
