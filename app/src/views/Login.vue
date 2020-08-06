<template>
  <a-layout>
    <LoginForm class="login-form" />
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

<style scoped>
.login-form {
  width: 500px;
  margin: 200px auto;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .login-form {
    margin: 150px auto;
    width: 250px;
  }
}
</style>
