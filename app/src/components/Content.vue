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
  margin: 30px;
  line-height: 500px;
  text-align: center;
}

/* If the text has multiple lines, add the following: */
.center h1 {
  display: inline-block;
  vertical-align: middle;
}
</style>
