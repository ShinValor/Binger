<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <LoginForm />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Navigation from "@/components/Navigation.vue";
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "Login",
  components: {
    Navigation,
    LoginForm
  }
};
</script>

<style scoped></style>
