<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <SignupForm />
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

<style scoped></style>
