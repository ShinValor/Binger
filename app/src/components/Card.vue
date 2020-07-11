<template>
  <a-card class="card" hoverable>
    <img
      class="large-image"
      slot="cover"
      alt="example"
      src="../assets/ethnic-friendship-pana.svg"
    />
    <a-card-meta :title="name" :description="desc" />
  </a-card>
</template>

<script>
export default {
  name: "Card",
  props: {
    name: String,
    desc: String,
    avatarUrl: String
  }
};
</script>

<style scoped>
.card {
  margin: 25px;
}

.large-image {
  height: 300px;
  width: 300px;
  margin: 0 auto;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .card {
    margin: 25px auto;
  }

  .large-image {
    height: 200px;
    width: 200px;
  }
}
</style>

<style>
.ant-card-body {
  margin: 5px !important;
  padding: 0px !important;
}
</style>
