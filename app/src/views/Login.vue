<template>
  <a-layout>
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
