<template>
  <a-input-search
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
      this.$router.push({
        name: "Search",
        query: { movieQuery: this.movieQuery }
      });
    }
  }
};
</script>

<style scoped></style>
