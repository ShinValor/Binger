<template>
  <a-layout>
    <SearchBar class="search-bar" :movieQuery="searchQuery" />
    <SearchResultsList
      class="search-list"
      :movieQuery="searchQuery"
      :key="searchQuery"
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
    searchQuery: function() {
      if (this.$route.query.movieQuery) {
        return this.$route.query.movieQuery;
      }
      return "";
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
