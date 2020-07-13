<template>
  <div class="container">
    <h1 class="title">Cast List</h1>
    <div>
      <MovieSynopsisCast class="list-item" />
      <MovieSynopsisCast class="list-item" />
      <MovieSynopsisCast class="list-item" />
      <MovieSynopsisCast class="list-item" />
      <MovieSynopsisCast class="list-item" />
    </div>
  </div>
</template>

<script>
import MovieSynopsisCast from "@/components/MovieSynopsisCast.vue";
const listData = [];
for (let i = 0; i < 10; i++) {
  listData.push({
    cast_id: 4,
    character: "The Big Narrator",
    credit_id: "52fe4250c3a36847f80149f3",
    gender: 2,
    id: 819,
    name: "Edward Norton",
    order: 0,
    profile_path: "/eIkFHNlfretLS1spAcIoihKUS62.jpg"
  });
}

export default {
  name: "MovieSynopsisCastList",
  components: {
    MovieSynopsisCast
  },
  data() {
    return {
      listData,
      currentPage: String,
      pagination: {
        onChange: page => {
          // console.log(page);
          this.currentPage = page;
        },
        pageSize: 5
      }
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

.list-item:hover {
  color: blue;
  background-color: lightblue;
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
