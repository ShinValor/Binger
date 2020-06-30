<template>
  <nav class="navbar">
    <navbar-search />
    <NavigationBarBar />
  </nav>
</template>

<script>
  import NavbarSearch from "./NavbarSearch";
  import NavigationBar_Bar from "./NavigationBarBar.vue";

  export default {
    name: "navbar",

    components: {
      NavbarSearch,
      NavigationBarBar
    }
  };
</script>

<style scoped lang="sass">

  .navbar
    display: flex
    height: 40px
    background: $c-shark

    .navbar-search
      display: flex
      align-items: center
      margin-left: 6px

    .navbar-nav
      margin: auto 30px auto auto
</style>