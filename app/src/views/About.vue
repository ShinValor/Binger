<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <div class="about">
      <Card class="about-card" name="John" desc="I am a student." />
      <Card class="about-card" name="Jun" desc="I am a student." />
      <Card class="about-card" name="Ferdi" desc="I am a student." />
      <Card class="about-card" name="Tarik" desc="I am a student." />
    </div>
    <Footer />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Navigation from "@/components/Navigation.vue";
import Card from "@/components/Card.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "About",
  components: {
    Navigation,
    Card,
    Footer
  }
};
</script>

<style scoped>
.about {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin: 50px;
}

.about-card {
  height: 400px;
  width: 400px;
  margin: 20px 50px !important;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .about-card {
    width: 300px;
    height: 250px;
    margin: 10px auto !important;
  }
}
</style>
