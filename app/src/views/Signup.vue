<template>
  <a-layout>
    <SignupForm class="signup-form" />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import SignupForm from "@/components/SignupForm.vue";

export default {
  name: "Signup",
  components: {
    SignupForm
  }
};
</script>

<style scoped>
.signup-form {
  width: 500px;
  margin: 200px auto;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .signup-form {
    margin: 150px auto;
    width: 250px;
  }
}
</style>
