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
import axios from "axios";
export default {
  name: "SearchBar",
  data() {
    return {
      movieQuery: "",
      searchResults: Array
    };
  },
  methods: {
    onSearch() {
      console.log(this.movieQuery);
      this.results();
    },
    results() {
      axios
        .get("http://127.0.0.1:5000/movie/search", {
          params: { query: this.movieQuery, page: 1 }
        })
        .then(res => {
          console.log(res.data);
          this.searchResults = res.data;
        })
        .catch(err => {
          console.log(err);
        });
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
