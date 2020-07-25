<template>
  <a-layout class="container">
    <SearchBar :movieQuery="searchQuery" />
    <Footer></Footer>
  </a-layout>
</template>


<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: "SearchResults",
  components: {
    SearchBar
  },
  computed: {
    searchQuery: function() {
      if ($route.query.movieQuery) {
        return $route.query.movieQuery;
      }
      return "";
    }
  }
};
</script>

<style scoped></style>
