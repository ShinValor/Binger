<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <navbar />
    <div class="grid">
      <Card name="John" desc="I am a student." />
      <Card name="Jun" desc="I am a student." />
      <Card name="Ferdi" desc="I am a student." />
      <Card name="Tarik" desc="I am a student." />
    </div>
  </a-layout>
</template>

<script>
// @ is an alias to /src
import navbar from "@/components/NavigationBar.vue";
import Card from "@/components/Card.vue";

export default {
  name: "About",
  components: {
    navbar,
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
</style>
