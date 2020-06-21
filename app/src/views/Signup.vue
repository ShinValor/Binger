<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <NavBar />
    <a-layout-content>
      <Content msg="This is sign up page" />
    </a-layout-content>
  </a-layout>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import Content from "@/components/Content.vue";

export default {
  name: "Signup",
  components: {
    NavBar,
    Content
  }
};
</script>

<style></style>
