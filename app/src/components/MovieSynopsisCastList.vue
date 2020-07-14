<template>
  <div class="container">
    <h1 class="title">Cast List</h1>
    <div>
      <MovieSynopsisCast class="list-item" v-for="item in castList" :key="item.order" :cast="item" />
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
      .get("/api/movie/cast/" + this.movieID)
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
.container {
  margin: 2em;
}

.title {
  margin: 20px;
  text-align: left;
  font-size: 30px;
}

.list-item {
  display: inline-block;
  margin: 10px;
  padding: 2px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    margin: 0 auto;
    text-align: center;
    font-size: 20px;
  }
}
</style>
