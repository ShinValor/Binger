<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <NavBar />
    <LoginForm />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "Login",
  components: {
    NavBar,
    LoginForm
  }
};
</script>

<style></style>
