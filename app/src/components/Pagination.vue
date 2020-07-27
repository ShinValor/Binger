<template>
  <a-pagination
    class="pagination"
    v-model="current"
    :total="500"
    show-less-items
  />
</template>
<script>
export default {
  data() {
    return {
      current: 1
    };
  }
};
</script>

<style scoped>
.pagination {
  margin: 50px;
}
</style>
