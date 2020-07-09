<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
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
import Card from "@/components/Card.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "About",
  components: {
    Card,
    Footer
  }
};
</script>

<style scoped>
.about {
  margin: 50px;
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .about {
    margin: 25px 0px 0px 0px;
    flex-direction: column;
    flex-wrap: nowrap;
  }
}
</style>
