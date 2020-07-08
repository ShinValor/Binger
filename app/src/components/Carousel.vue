<template>
  <flickity class="carousel" ref="flickity" :options="flickityOptions">
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/wonder-woman.jpg" />
      <!-- <img
        class="carousel-cell-image"
        data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/tulip.jpg"
        alt="tulip"
      /> -->
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/terminator.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/logan.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/joker.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/black-panther.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/black-widow.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/starwar.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/aladdin.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/black-widow.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/black-panther.jpg" />
    </div>
    <div class="carousel-cell">
      <img class="carousel-cell-image" src="../imgs/black-widow.jpg" />
    </div>
  </flickity>
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
        // lazyLoad: true,
        autoPlay: 3000,
        groupCells: 4,
        freeScroll: true
      }
    };
  }
};
</script>
<style scoped>
.carousel {
  /* background: #fafafa; */
  /* height: 400px; */
  margin: 20px;
}

.carousel-cell {
  height: 400px;
  width: 25%;
  margin: 0px 10px;
  /* background: #333; */
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

.carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
}

@media screen and (max-width: 800px) {
  /* applies styles to any device screen sizes below 800px wide */
  .carousel {
    height: 150px;
    margin: 5px;
  }

  .carousel-cell {
    height: 150px;
    margin: 0px 5px;
  }
}
</style>
