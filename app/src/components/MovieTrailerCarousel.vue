<template>
  <div>
    <flickity
      class="carousel"
      ref="flickity"
      :options="flickityOptions"
      v-for="(todo, index) in todos"
    >
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/wonder-woman.jpg" @click="showModal" />
      </div>
    </flickity>
    <a-modal v-model="visible" title="Movie Summary" :width="750" :footer="null">
      <div class="container">
        <img class="large-image" src="../imgs/black-widow.jpg" />
      </div>
      <a-button @click="onClick">More</a-button>
    </a-modal>
  </div>
</template>
<script>
import Flickity from "vue-flickity";

export default {
  name: "Carousel",
  components: {
    Flickity
  },
  props: {},
  data() {
    return {
      flickityOptions: {
        initialIndex: 0,
        autoPlay: 3000,
        groupCells: 5,
        freeScroll: true
        // prevNextButtons: false
      },
      visible: false
    };
  },
  methods: {
    showModal() {
      this.visible = true;
    },
    onClick() {
      console.log("More");
    }
  }
};
</script>
<style scoped>
.carousel {
  margin: 50px 20px;
}

.carousel-cell {
  height: 400px;
  width: 20%;
  margin: 0px;
  display: flex;
  justify-content: center;
}

.carousel-cell-image {
  max-height: 100%;
  max-width: 100%;
  margin: 0 auto;
  display: block;
  object-fit: cover;
}

.carousel-cell-image:hover {
  opacity: 0.7;
}

/* .carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
} */

.container {
  display: flex;
}

.content {
  width: 66%;
  margin: 5px;
  font-size: 15px;
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */
  .carousel {
    margin: 5px;
  }

  .carousel-cell {
    height: 100px;
    margin: 0px 5px;
  }
}
</style>