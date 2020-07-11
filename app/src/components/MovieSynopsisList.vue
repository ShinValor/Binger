<template>
  <a-list item-layout="horizontal" :data-source="data">
    <a-list-item slot="renderItem" slot-scope="item, index">
      <a-list-item-meta
        description="Ant Design, a design language for background applications, is refined by Ant UED Team"
      >
        <a slot="title" href="https://www.antdv.com/">{{ item.title }}</a>
        <a-avatar
          slot="avatar"
          src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
        />
      </a-list-item-meta>
    </a-list-item>
  </a-list>
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
<style scoped>
.card {
  background: gray;
  margin: 1.5em;
}
</style>
