<template>
  <div class="card">
    <h2 class="list-type-text">The important Cast</h2>
    <div>
      <MovieSynopsisCast
        class="list-item"
        v-for="item in castList"
        :key="item.order"
        :cast="item"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieSynopsisCast from "@/components/MovieSynopsisCast.vue";

export default {
  name: "MovieSynopsisCastList",
  components: {
    MovieSynopsisCast
  },
  props: {
    movieID: {
      type: Number,
      required: true
    }
  },
  created() {
    axios
      .get("http://127.0.0.1:5000/movie/cast/" + this.movieID)
      .then(response => {
        if (response && response.status === 200) {
          console.log(response);
          this.castList = response.data;
        }
      })
      .catch(error => {
        this.errors = error;
        console.log(error);
      });
  },
  data() {
    return {
      castList: Array

    };
  }
};
</script>
<style scoped>
.list-item {
  display: inline-block;
  margin: 10px;
  padding: 2px;
}
.card {
  margin: 2em;
}
.list-type-text {
  text-align: left;
  font-size: 2em;
  margin-bottom: 0%;
  margin-top: 1rem;
}
</style>
