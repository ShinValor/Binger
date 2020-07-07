<template>
  <div class="favorites">
    <h1>Favorites</h1>
    <FavoriteMovieList />
  </div>
</template>

<script>
import FavoriteMovieList from "@/components/FavoriteMovieList.vue";

export default {
  name: "Favorites",
  components: {
    FavoriteMovieList
  }
};
</script>

<style scoped>
h1 {
  font-size: 30px;
}
</style>
