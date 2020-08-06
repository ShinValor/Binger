<template>
  <button id="btn" @click="topFunction">
    <font-awesome-icon :icon="['fas', 'angle-double-up']" />
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
  bottom: 2%;
  width: 50px;
  height: 50px;
  padding: 0.5px;
  background-color: #2a323d;
  border: 1px solid #f3c669;
  border-radius: 50%;
  outline: none;
  color: white;
  display: inline-block;
  vertical-align: middle;
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  transform: perspective(1px) translateZ(0);
  -webkit-transform: perspective(1px) translateZ(0);
  transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  transition-property: transform;
  -webkit-transition-property: transform;
  transition-timing-function: ease-out;
  -webkit-transition-timing-function: ease-out;
}

#btn:hover {
  transform: scale(1.2);
  background-color: #f3c669;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  #btn {
    left: 85%;
  }
}
</style>
