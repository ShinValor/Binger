<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <a-result
      status="404"
      title="404"
      sub-title="Sorry, the page you visited does not exist."
    >
      <template #extra>
        <a-button type="primary">
          <router-link to="/">Back Home</router-link>
        </a-button>
      </template>
    </a-result>
  </a-layout>
</template>

<script>
export default {
  name: "PageNotFound"
};
</script>
<style scoped></style>
