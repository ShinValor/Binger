<template>
  <a-input-search
    class="search-bar"
    placeholder="Search Movies"
    v-model="movieQuery"
    enter-button
    @search="onSearch"
  />
</template>
<script>
export default {
  name: "SearchBar",
  props: {
    movieQuery: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      searchResults: Array
    };
  },
  methods: {
    onSearch() {
      console.log(this.movieQuery);
      this.$router.push({
        name: "Search",
        query: { movieQuery: this.movieQuery }
      });
    }
  }
};
</script>
<style scoped>
/* .search-bar {
  width: 50%;
  margin: 50px auto 25px;
} */

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  /* .search-bar {
    width: 75%;
    margin: 15px auto;
  } */
}
</style>
