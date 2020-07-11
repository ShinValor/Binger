<template>
  <div class="card">
    <dic class="image">
      <img
        class="poster"
        src="https://image.tmdb.org/t/p/w300/s1cVTQEZYn4nSjZLnFbzLP0j8y2.jpg"
        alt="Girl in a jacket"
        style="vertical-align:top
        "
      />
    </dic>
    <div class="trailer-body">
      <iframe
        allowfullscreen
        frameborder="0"
        height="376"
        src="https://www.youtube.com/embed/QWbMckU3AOQ?autoplay=1&modestbranding=1"
        style="width: 60%; min-width: 536px"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieSynopsisTrailer"
};
</script>

<style scoped>
.card {
  margin: 1.5em;
  background: #1e1d1d;
}
.poster,
.trailer-body {
  display: inline;
}
</style>