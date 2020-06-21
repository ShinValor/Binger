<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <FourOFour />
  </a-layout>
</template>

<script>
import FourOFour from "@/components/FourOFour.vue";

export default {
  name: "NotFound",
  components: {
    FourOFour
  }
};
</script>
