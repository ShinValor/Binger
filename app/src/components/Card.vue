<template>
  <a-card class="card" hoverable>
    <div class="container">
      <img
        class="large-image"
        slot="cover"
        alt="Profile Picture"
        src="../assets/svg/profile-pic.svg"
      />
    </div>
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
  background-color: #2a323d;
  margin: 10px;
  /* border-color: #f3c669; */
}

.container {
  /* background-color: white; */
  margin: 5px;
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
