<template>
  <a-card class="card" hoverable>
    <img
      slot="cover"
      alt="example"
      src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png"
    />
    <a-card-meta :title="name" :description="desc">
      <a-avatar
        slot="avatar"
        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
      />
    </a-card-meta>
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
  margin: 50px !important;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .card {
    height: 250px;
    width: 250px;
    margin: 25px auto !important;
  }
}
</style>
