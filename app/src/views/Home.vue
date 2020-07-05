<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <a-layout-content>
      <div :style="{ height: '450px', 'margin-top': '64px' }">
        <img
          src="@/imgs/banner.jpg"
          alt="Binger Banner"
          :style="{ 'object-fit': 'cover', height: '100%', width: '100%' }"
        />
      </div>
      <Content msg="Welcome To Binger" />
      <div class="container">
        <div class="item1">header</div>
        <div class="item2">header 2</div>
        <div class="item3">advert</div>
        <div class="item4">content</div>
        <div class="item5">footer</div>
      </div>
      <div class="container2">
        <div class="item6">header</div>
        <div class="item7">advert</div>
        <div class="item8">content</div>
      </div>
      <flickity class="carousel" ref="flickity" :options="flickityOptions">
        <div class="carousel-cell">
          <img
            src="../imgs/wonder-woman.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/tulip.jpg"
            alt="tulip"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/terminator.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/grapes.jpg"
            alt="grapes"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/logan.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/raspberries.jpg"
            alt="raspberries"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/6-underground.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/wolf.jpg"
            alt="wolf"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/joker.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/leaf-droplets.jpg"
            alt="leaf droplets"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/black-panther.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/leaf-droplets.jpg"
            alt="leaf droplets"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/black-widow.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/wolf.jpg"
            alt="wolf"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/starwar.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/leaf-droplets.jpg"
            alt="leaf droplets"
          /> -->
        </div>
        <div class="carousel-cell">
          <img
            src="../imgs/aladdin.jpg"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/leaf-droplets.jpg"
            alt="leaf droplets"
          /> -->
        </div>
      </flickity>
    </a-layout-content>
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
        initialIndex: 0,
        // lazyLoad: true,
        autoPlay: 3000,
        groupCells: 3,
        freeScroll: true
      }
    };
  }
};
</script>

<style scoped>
.carousel {
  background: #fafafa;
  margin: 25px;
  height: 500px;
}

.carousel-cell {
  width: 33%;
  height: 500px;
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

.container {
  height: 700px;
  margin: 50px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-gap: 10px;
  grid-template-areas:
    "header header2 advert"
    "content content advert"
    "footer footer footer";
}

.item1 {
  background: LightSkyBlue;
  grid-area: header;
}

.item2 {
  background: LightSkyBlue;
  grid-area: header2;
}

.item3 {
  background: LightSalmon;
  grid-area: advert;
}

.item4 {
  background: PaleTurquoise;
  grid-area: content;
}

.item5 {
  background: lightpink;
  grid-area: footer;
}

.container2 {
  height: 500px;
  margin: 50px;
  display: flex;
  justify-content: space-between;
}

.item6 {
  background: lightgreen;
  width: 33%;
}

.item7 {
  background: lightsteelblue;
  width: 33%;
}

.item8 {
  background: lightgoldenrodyellow;
  width: 33%;
}
</style>
