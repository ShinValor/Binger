<template>
  <a-card class="card" hoverable>
    <div class="container">
      <img
        class="large-image"
        slot="cover"
        alt="Profile Picture"
        :src="img"
        v-if="img"
      />
      <img
        class="large-image"
        slot="cover"
        alt="Profile Picture"
        src="../assets/svg/profile-pic.svg"
        v-else
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
    img: String
  },
  mounted() {
    console.log(this.img);
  }
};
</script>

<style scoped>
.card {
  margin: 10px;
  background-color: #2a323d;
}

.container {
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
