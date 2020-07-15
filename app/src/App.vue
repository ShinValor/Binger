<template>
  <div id="app">
    <Navigation />
    <router-view id="page-wrap" />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";

export default {
  components: {
    Navigation
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  background-color: #222831;
}

/* Change Selection Text Color When Highlighting */
#app ::-moz-selection {
  background-color: #9ea5f1;
  color: #fff;
}

#app ::selection {
  background-color: #9ea5f1;
  color: #fff;
}
</style>
