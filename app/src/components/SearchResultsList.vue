<template>
  <div>
    <h3>Results</h3>
    <ul class="list">
      <SearchResultsCell v-for="item in list" :key="item.title" :item="item" />
    </ul>
  </div>
</template>

<script>
import SearchResultsCell from "./SearchResultsCell.vue";
import axios from "axios";

export default {
  components: {
    SearchResultsCell
  },
  props: {
    movieQuery: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      loading: true,
      list: Array,
      errors: []
    };
  },
  methods: {
    fetchResults() {
      axios
        .get("http://127.0.0.1:5000/movie/search", {
          params: { query: this.movieQuery, page: 1 }
        })
        .then(res => {
          console.log(res.data);
          this.list = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  created() {
    this.fetchResults();
  }
};
</script>

<style scoped>
.list {
  padding: 0;
  border-radius: 4px;
  /* border: 1px solid #e0e0e0; */
  border: 1px solid black;
}

.errors {
  padding: 0;
  color: red;
}
</style>
