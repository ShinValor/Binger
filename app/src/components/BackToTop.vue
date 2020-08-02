<template>
  <button id="btn" @click="topFunction" :style="{ color: 'black' }">
    <a-icon type="up" />
  </button>
</template>

<script>
export default {
  name: "BackToTop",
  methods: {
    topFunction() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
  },
  mounted() {
    window.onscroll = function() {
      scrollFunction();
    };

    const scrollFunction = function() {
      const mybutton = document.getElementById("btn");
      if (
        document.body.scrollTop > 20 ||
        document.documentElement.scrollTop > 20
      ) {
        mybutton.style.display = "block";
      } else {
        mybutton.style.display = "none";
      }
    };
  },
  destroyed() {
    window.onscroll = function() {};
  }
};
</script>

<style scoped>
#btn {
  position: fixed;
  left: 95%;
  bottom: 10px;
  width: 50px;
  height: 50px;
  padding: 0.5px;
  background-color: #f3c669;
  border-color: black;
  border-radius: 50%;
}
</style>
