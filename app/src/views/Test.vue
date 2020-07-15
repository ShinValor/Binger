<template>
  <a-layout>
    <div class="container">
      <VueSwing
        class="section"
        @throwout="throwout"
        @throwin="throwin"
        :config="config"
      >
        <div class="card"></div>
      </VueSwing>
    </div>
  </a-layout>
</template>

<script>
// @ is an alias to /src
import VueSwing from "vue-swing";

export default {
  name: "Test",
  components: {
    VueSwing
  },
  data() {
    return {
      config: {
        allowedDirections: [
          VueSwing.Direction.LEFT,
          VueSwing.Direction.RIGHT,
          VueSwing.Direction.UP,
          VueSwing.Direction.DOWN
        ]
      }
    };
  },
  methods: {
    throwin() {
      console.log("throw in");
    },
    throwout() {
      console.log("throw out");
    }
  }
};
</script>

<style scoped>
.container {
  margin: 0 auto;
}

.section {
  background-color: white;
  width: 500px;
  height: 500px;
  border-style: solid;
  border-color: gray;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  width: 200px;
  height: 300px;
  background-color: wheat;
}
</style>
