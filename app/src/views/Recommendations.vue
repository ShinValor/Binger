<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation></Navigation>
    <a-input-search
      :style="{ width: '50%', margin: '25px auto' }"
      placeholder="Search Movies"
      enter-button
      @search="onSearch"
    />
    <div :style="{ margin: '10px auto', width: '75%' }">
      <a-menu v-model="current" mode="horizontal">
        <a-menu-item key="mail"> <a-icon type="mail" />Tags</a-menu-item>
        <a-menu-item key="app" disabled>
          <a-icon type="appstore" />Top Rated
        </a-menu-item>
        <a-sub-menu>
          <span slot="title" class="submenu-title-wrapper"
            ><a-icon type="setting" />Most Viewed</span
          >
          <a-menu-item-group title="Item 1">
            <a-menu-item key="setting:1">
              Option 1
            </a-menu-item>
            <a-menu-item key="setting:2">
              Option 2
            </a-menu-item>
          </a-menu-item-group>
          <a-menu-item-group title="Item 2">
            <a-menu-item key="setting:3">
              Option 3
            </a-menu-item>
            <a-menu-item key="setting:4">
              Option 4
            </a-menu-item>
          </a-menu-item-group>
        </a-sub-menu>
        <a-menu-item key="alipay">
          <a href="https://antdv.com" target="_blank" rel="noopener noreferrer"
            >Your Favorite</a
          >
        </a-menu-item>
      </a-menu>
    </div>
    <h1 class="title">Top Movie Pick</h1>
    <div class="container">
      <div class="row">
        <div class="col">
          <img class="small-image" src="@/imgs/aladdin.jpg" alt="Aladdin" />
        </div>
        <div class="col">
          <img class="small-image" src="@/imgs/starwar.jpg" alt="Star War" />
        </div>
        <div class="col">
          <img class="small-image" src="@/imgs/logan.jpg" alt="Logan" />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/wonder-woman.jpg"
            alt="Wonder Woman"
          />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/black-panther.jpg"
            alt="Black Panther"
          />
        </div>
        <div class="col">
          <img class="small-image" src="@/imgs/joker.jpg" alt="The Joker" />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/6-underground.jpg"
            alt="6-underground"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/black-widow.jpg"
            alt="Black Widow"
          />
        </div>
      </div>
      <a-button
        type="primary"
        :style="{ width: '100px', margin: '10px', float: 'right' }"
      >
        More ...
      </a-button>
    </div>
    <Carousel></Carousel>
    <Swiper></Swiper>
    <Modal></Modal>
    <Footer></Footer>
  </a-layout>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Carousel from "@/components/Carousel.vue";
import Swiper from "@/components/Swiper.vue";
import Modal from "@/components/Modal.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    Navigation,
    Carousel,
    Swiper,
    Modal,
    Footer
  },
  data() {
    return {
      current: ["mail"]
    };
  },
  methods: {
    onSearch(value) {
      console.log(value);
    }
  }
};
</script>

<style scoped>
.title {
  margin: 30px 0px 0px 30px;
  text-align: left;
  font-size: 30px;
}

.small-image {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.container {
  margin: 20px;
}

.container .row {
  display: flex;
}

.container .row .col {
  width: 25%;
  margin: 10px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    text-align: center;
    margin: 0 auto;
  }

  .container .row {
    flex-direction: column;
  }

  .container .row .col {
    width: 100%;
    margin: 5px auto;
  }
}
</style>
