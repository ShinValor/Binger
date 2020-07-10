<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <a-layout>
      <a-layout-content>
        <Content msg="This is home page" />
        <flickity class="carousel" ref="flickity" :options="flickityOptions">
          <div class="carousel-cell">
            <img
              class="carousel-cell-image"
              data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/tulip.jpg"
              alt="tulip"
            />
          </div>
          <div class="carousel-cell">
            <img
              class="carousel-cell-image"
              data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/grapes.jpg"
              alt="grapes"
            />
          </div>
          <div class="carousel-cell">
            <img
              class="carousel-cell-image"
              data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/raspberries.jpg"
              alt="raspberries"
            />
          </div>
          <div class="carousel-cell">
            <img
              class="carousel-cell-image"
              data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/wolf.jpg"
              alt="wolf"
            />
          </div>
          <div class="carousel-cell">
            <img
              class="carousel-cell-image"
              data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/leaf-droplets.jpg"
              alt="leaf droplets"
            />
          </div>
        </flickity>
      </a-layout-content>
    </a-layout>
    <Footer />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Navigation from "@/components/Navigation.vue";
import Content from "@/components/Content.vue";
import Footer from "@/components/Footer.vue";
import Flickity from "vue-flickity";

export default {
  name: "Home",
  components: {
    Navigation,
    Content,
    Footer,
    Flickity
  },
  data() {
    return {
      flickityOptions: {
        initialIndex: 2,
        lazyLoad: true
      }
    };
  }
};
</script>

<style>
.carousel {
  background: #fafafa;
  margin: 25px;
}

.carousel-cell {
  width: 66%;
  height: 300px;
  margin-right: 10px;
  background: #333;
}

.carousel-cell-image {
  display: block;
  max-height: 100%;
  margin: 0 auto;
  max-width: 100%;
  opacity: 0;
  -webkit-transition: opacity 0.4s;
  transition: opacity 0.4s;
}

.carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
}
</style>
