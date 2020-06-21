<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <a-layout-content>
      <Content msg="This is home page" />
    </a-layout-content>
    <Footer />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Navigation from "@/components/Navigation.vue";
import Content from "@/components/Content.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Home",
  components: {
    Navigation,
    Content,
    Footer
  }
};
</script>

<style></style>
