<template>
  <a-layout class="container">
    <SearchBar :movieQuery="searchQuery" />
    <SearchResultsList :movieQuery="searchQuery" />
    <Footer></Footer>
  </a-layout>
</template>


<script>
import SearchBar from "@/components/SearchBar.vue";
import SearchResultsList from "@/components/SearchResultsList.vue";

export default {
  name: "SearchResults",
  components: {
    SearchBar,
    SearchResultsList
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

<style scoped></style>
