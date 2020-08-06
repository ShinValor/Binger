<template>
  <a-layout>
    <a-result
      class="not-found"
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

<style scoped>
.not-found {
  margin: 100px auto;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .not-found {
    margin: 10px auto;
  }
}
</style>
