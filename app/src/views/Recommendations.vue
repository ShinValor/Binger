<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation></Navigation>
    <a-input-search
      :style="{ width: '50%', margin: '25px auto' }"
      placeholder="Search Movies"
      enter-button
      @search="onSearch"
    />
    <div :style="{margin: '10px 30px'}">
      <a-menu v-model="current" mode="horizontal">
        <a-menu-item key="mail"> <a-icon type="mail" />Navigation One </a-menu-item>
        <a-menu-item key="app" disabled> <a-icon type="appstore" />Navigation Two </a-menu-item>
        <a-sub-menu>
          <span slot="title" class="submenu-title-wrapper"
            ><a-icon type="setting" />Navigation Three - Submenu</span
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
            >Navigation Four - Link</a
          >
        </a-menu-item>
      </a-menu>
    </div>
    <h1>Top Movie Pick</h1>
    <div class="movie-poster">
      <div class="poster-row">
        <div class="poster-col">
          <img src="@/imgs/aladdin.jpg" alt="Aladdin">
        </div>
        <div class="poster-col">
          <img src="@/imgs/starwar.jpg" alt="Star War">
        </div>
        <div class="poster-col">
          <img src="@/imgs/logan.jpg" alt="Logan">
        </div>
        <div class="poster-col">
          <img src="@/imgs/wonder-woman.jpg" alt="Wonder Woman">
        </div>
      </div>
      <div class="poster-row">
        <div class="poster-col">
          <img src="@/imgs/black-panther.jpg" alt="Black Panther">
        </div>
        <div class="poster-col">
          <img src="@/imgs/joker.jpg" alt="Joker">
        </div>
        <div class="poster-col">
          <img src="@/imgs/6-underground.jpg" alt="6-underground">
        </div>
        <div class="poster-col">
          <img src="@/imgs/black-widow.jpg" alt="Black Widow">
        </div>
      </div>
      <a-button type="primary" :style="{width: '100px', 'margin': '10px', float: 'right'}">
        More ...
      </a-button>
    </div>
    <div class="movie-slider">
      <Carousel></Carousel>
    </div>
    <div class="movie-swiper">
      <Swiper></Swiper>
    </div>
    <Modal></Modal>
    <Footer></Footer>
  </a-layout>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Swiper from "@/components/Swiper.vue";
import Carousel from "@/components/Carousel.vue";
import Modal from "@/components/Modal.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    Navigation,
    Swiper,
    Carousel,
    Modal,
    Footer
  },
  data() {
    return {
      current: ['mail'],
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
h1 {
  text-align: left;
  margin: 30px 0px 0px 30px;
  font-size: 30px;
}

.movie-poster {
  margin: 20px;
}

.movie-poster .poster-row {
  display: flex;
}

.movie-poster .poster-col {
  width: 25%;
  margin: 10px;
}

img {
  object-fit: cover;
  width:100%;
  height:100%;
}

.movie-slider {
  height: 500px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  h1 {
    text-align: center;
    margin: 0 auto;
  }

  .movie-poster .poster-row {
    flex-direction: column;
  }

  .movie-poster .poster-col {
    width: 100%;
    margin: 5px auto;
  }

  .movie-slider {
    height: 300px;
    width: 300px;
    margin: 0 auto;
  }
}
</style>
