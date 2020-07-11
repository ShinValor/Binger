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
    photoUrl: String,
    avatarUrl: String
  }
};
</script>

<style scoped>
.card {
  height: 400px;
  width: 400px;
  margin: 50px;
}

.large-image {
  height: 300px;
  width: 300px;
  margin: 0 auto;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .card {
    height: 250px;
    width: 250px;
    margin: 25px auto;
  }
}
</style>
