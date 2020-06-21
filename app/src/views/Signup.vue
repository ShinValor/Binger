<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <NavBar />
    <SignupForm />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import SignupForm from "@/components/SignupForm.vue";

export default {
  name: "Signup",
  components: {
    NavBar,
    SignupForm
  }
};
</script>

<style></style>
