<template>
  <div class="card">
    <h2 class="list-type-text">Cast List</h2>
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
.list-item {
  display: inline-block;
  margin: 10px;
  padding: 2px;
}
.list-item:hover {
  color: blue;
  background-color: lightblue;
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
