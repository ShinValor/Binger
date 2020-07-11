<template>
  <div>
    <h2>Cast List</h2>
    <a-list item-layout="vertical" size="large" :pagination="pagination" :data-source="listData">
      <a-list-item slot="renderItem" key="item.title" slot-scope="item">
        <MovieSynopsisCast :cast="item" />
      </a-list-item>
    </a-list>
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
  name: "MovieSynopsisList",
  components: {
    MovieSynopsisCast
  },
  data() {
    return {
      listData,
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 5
      }
    };
  }
};
</script>
<style></style>
