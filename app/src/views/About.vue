<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <div class="grid">
      <Card class="about-card" name="John" desc="I am a student." />
      <Card class="about-card" name="Jun" desc="I am a student." />
      <Card class="about-card" name="Ferdi" desc="I am a student." />
      <Card class="about-card" name="Tarik" desc="I am a student." />
    </div>
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Navigation from "@/components/Navigation.vue";
import Card from "@/components/Card.vue";

export default {
  name: "About",
  components: {
    Navigation,
    Card
  }
};
</script>

<style>
.grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin: 50px;
}

.about-card {
  height: 450px;
  width: 500px;
  margin: 50px !important;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .about-card {
    height: 400px;
    width: 300px;
    margin: 15px auto !important;
  }
}

@media screen and (max-width: 300px) {
  /* applies styles to any device screen sizes below 800px wide */

  .about-card {
    height: 300px;
    margin: 5px auto !important;
  }
}
</style>
