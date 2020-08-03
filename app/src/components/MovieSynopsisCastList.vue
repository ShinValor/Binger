<template>
  <div class="cast-list">
    <h1 class="title">Cast List</h1>
    <div>
      <MovieSynopsisCast
        class="movie-cast"
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
      .get(
        "https://binger-api-testv1.azurewebsites.net/movie/cast/" + this.movieID
      )
      .then(res => {
        this.castList = res.data;
      })
      .catch(err => {
        this.error = err;
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
.title {
  margin: 20px;
  text-align: center;
  font-size: 30px;
  color: white;
}

.cast-list {
  margin: 2em;
}

.movie-cast {
  display: inline-block;
  margin: 10px;
  padding: 2px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    margin: 0 auto;
    font-size: 20px;
  }
}
</style>
