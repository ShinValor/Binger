<template>
  <!-- <a-layout-content :style="{ padding: '0 50px' }"> -->
  <div class="center">
    <h1>{{ msg }}</h1>
  </div>
  <!-- </a-layout-content> -->
</template>

<script>
export default {
  name: "Content",
  props: {
    msg: String
  }
};
</script>

<style scoped>
.center {
  background: #fff;
  height: 500px;
  margin: 30px 30px 100px 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .center {
    height: 200px;
    margin: 15px;
  }
}
</style>
