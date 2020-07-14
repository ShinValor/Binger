<template>
  <a-input-search
    class="search-bar"
    placeholder="Search Movies"
    enter-button
    @search="onSearch"
  />
</template>
<script>
export default {
  name: "SearchBar",
  data() {
    return {
      movieQuery: String
    };
  },
  methods: {
    onSearch(input) {
      this.movieQuery = input;
    }
  }
};
</script>
<style scoped>
.search-bar {
  width: 50%;
  margin: 50px auto 25px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .search-bar {
    width: 75%;
    margin: 15px auto;
  }
}
</style>
