<template>
  <div>
    <flickity class="carousel" ref="flickity" :options="flickityOptions">
      <div class="carousel-cell">
        <!-- <img
          class="carousel-cell-image"
          data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/tulip.jpg"
          alt="tulip"
        /> -->
        <img
          class="carousel-cell-image"
          src="../imgs/wonder-woman.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/terminator.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/logan.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/6-underground.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/joker.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/black-panther.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/black-widow.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/starwar.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/aladdin.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/black-widow.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/black-panther.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/black-widow.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/logan.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/6-underground.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/logan.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/6-underground.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/6-underground.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/6-underground.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/6-underground.jpg"
          @click="showModal"
        />
      </div>
      <div class="carousel-cell">
        <img
          class="carousel-cell-image"
          src="../imgs/6-underground.jpg"
          @click="showModal"
        />
      </div>
    </flickity>
    <a-modal
      v-model="visible"
      title="Movie Summary"
      :width="750"
      :footer="null"
    >
      <div class="container">
        <p class="content">
          All our illustrations come in different styles, and you can change
          main color. Just choose the one you like the most for your project.
          Some styles allow you to select a simple background, a more one, or
          one, or remove it altogether. Give it a try!
        </p>
        <p class="content">
          All our illustrations come in different styles, and you can change
          main color. Just choose the one you like the most for your project.
          Some styles allow you to select a simple background, a more one, or
          one, or remove it altogether. Give it a try!
        </p>
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
