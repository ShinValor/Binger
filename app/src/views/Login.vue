<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <LoginForm />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "Login",
  components: {
    LoginForm
  }
};
</script>

<style scoped></style>
