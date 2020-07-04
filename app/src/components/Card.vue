<template>
  <a-card class="profile-card" hoverable>
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

<style>
.profile-card {
  height: 450px;
  width: 500px;
  margin: 50px !important;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .profile-card {
    height: 400px;
    width: 300px;
    margin: 15px auto !important;
  }
}

@media screen and (max-width: 300px) {
  /* applies styles to any device screen sizes below 800px wide */

  .profile-card {
    height: 300px;
    margin: 5px auto !important;
  }
}
</style>
