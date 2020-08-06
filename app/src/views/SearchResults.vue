<template>
  <a-layout>
    <SearchBar class="search-bar" :movieQuery="searchQuery" />
    <SearchResultsList
      class="searchList"
      :movieQuery="searchTitleQuery"
      :genreQuery="searchGenreQuery"
      :key="searchResultListKey"
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
      if (this.$route.query.with_genres) {
        return this.$route.query.with_genres;
      }
      return "";
    },
    searchResultListKey: function() {
      return this.searchGenreQuery + this.searchTitleQuery;
    }
  }
};
</script>

<style scoped>
.search-bar {
  width: 50%;
  margin: 50px auto 25px;
}

.search-list {
  margin: 25px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .search-bar {
    width: 75%;
    margin: 15px auto;
  }

  .search-list {
    margin: 15px 10px;
  }
}
</style>
