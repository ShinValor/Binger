<template>
  <!-- <a-layout-content :style="{ padding: '0 50px' }"> -->
  <div :style="{ background: '#fff', margin: '24px', minHeight: '380px' }">
    {{ msg }}
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

<style></style>
