<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <SignupForm />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Navigation from "@/components/Navigation.vue";
import SignupForm from "@/components/SignupForm.vue";

export default {
  name: "Signup",
  components: {
    Navigation,
    SignupForm
  }
};
</script>

<style scoped></style>
