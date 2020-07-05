<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <a-layout-content>
      <div :style="{ height: '450px' }">
        <img
          src="@/imgs/banner.jpg"
          alt="Binger Banner"
          :style="{ 'object-fit': 'cover', height: '100%', width: '100%' }"
        />
      </div>
      <Content msg="Welcome To Binger" />
      <div class="container2">
        <div
          :style="{
            width: '50%',
            display: 'flex',
            'flex-direction': 'column',
            'justify-content': 'center'
          }"
        >
          <h1>Optimized Movie Search Engine</h1>
          <p>
            All our illustrations come in different styles, and you can change
            the main color. Just choose the one you like the most for your
            project. Some styles allow you to select a simple background, a more
            one, or remove it altogether. Give it a try!
          </p>
        </div>
        <div :style="{ width: '50%' }">
          <img
            src="../assets/fast-loading.png"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
        </div>
      </div>
      <div class="container2">
        <div :style="{ width: '50%' }">
          <img
            src="../assets/movie-night.png"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
        </div>
        <div
          :style="{
            width: '50%',
            display: 'flex',
            'flex-direction': 'column',
            'justify-content': 'center'
          }"
        >
          <h1>Movie Nights</h1>
          <p>
            Do you want the illustrations to come to life on your website? You
            can animate them directly with our online editor! Some styles allow
            you to select a simple background, a more detailed one, or remove it
            altogether. Give it a try!
          </p>
        </div>
      </div>
      <div class="container2">
        <div
          :style="{
            width: '50%',
            display: 'flex',
            'flex-direction': 'column',
            'justify-content': 'center'
          }"
        >
          <h1>Watch With Friends</h1>
          <p>
            Some styles allow you to select a simple background, a more detailed
            one, or remove it altogether. Give it a try! Some styles allow you
            to select a simple background, a more detailed one, or remove it
            altogether. Give it a try!
          </p>
        </div>
        <div :style="{ width: '50%' }">
          <img
            src="../assets/friendship.png"
            :style="{
              'object-fit': 'cover',
              'max-height': '100%',
              'max-width': '100%'
            }"
          />
        </div>
      </div>
      <h1 :style="{ 'font-size': '40px' }">
        <strong> How It Works </strong>
      </h1>
      <div class="container">
        <div :style="{ 'grid-area': 'header' }">
          <img
            src="../assets/login.svg"
            :style="{
              'object-fit': 'cover',
              height: '100px',
              width: '100px',
              margin: '20px auto'
            }"
          />
          <h1>Sign up and Log in</h1>
        </div>
        <div :style="{ 'grid-area': 'header2' }">
          <img
            src="../assets/profile.svg"
            :style="{
              'object-fit': 'cover',
              height: '100px',
              width: '100px',
              margin: '20px auto'
            }"
          />
          <h1>Update Profile</h1>
        </div>
        <div :style="{ 'grid-area': 'advert' }">
          <img
            src="../assets/watch-movie.svg"
            :style="{
              'object-fit': 'cover',
              height: '400px',
              width: '500px'
            }"
          />
        </div>
        <div :style="{ 'grid-area': 'content' }">
          <img
            src="../assets/arrow.svg"
            :style="{
              'object-fit': 'cover',
              height: '100px',
              width: '100px',
              margin: '10px 50px'
            }"
          />
          <img
            src="../assets/movie-tape.svg"
            :style="{
              'object-fit': 'cover',
              height: '100px',
              width: '100px',
              margin: '10px 50px'
            }"
          />
          <img
            src="../assets/list.svg"
            :style="{
              'object-fit': 'cover',
              height: '100px',
              width: '100px',
              margin: '10px 50px'
            }"
          />
          <h1>Select Your Favorite Movie Genre</h1>
        </div>
        <div :style="{ 'grid-area': 'footer' }">
          <a-steps
            :style="{
              'margin-top': '25px',
              'margin-bottom': '75px',
              'margin-left': '-60px'
            }"
          >
            <a-step status="finish" title="Login">
              <a-icon slot="icon" type="user" />
            </a-step>
            <a-step
              status="finish"
              title="Select 
              Movie Genre"
            >
              <a-icon slot="icon" type="solution" />
            </a-step>
            <a-step status="process" title="Processing">
              <a-icon slot="icon" type="loading" />
            </a-step>
            <a-step status="wait" title="Done">
              <a-icon slot="icon" type="smile-o" />
            </a-step>
          </a-steps>
          <h1>Recommend Using Our Movie Recommendation Engine</h1>
        </div>
      </div>
      <h1 :style="{ 'font-size': '30px' }">Type of Services</h1>
      <div class="container2">
        <div
          :style="{
            width: '33%',
            'background-color': 'white',
            'border-radius': '5%'
          }"
        >
          <a-result
            status="success"
            title="Basic"
            sub-title="Order number: 2017182818828182881 Cloud server configuration takes 1-5 minutes, please wait."
          >
            <template #extra>
              <a-button key="console" type="primary">
                Go Console
              </a-button>
              <a-button key="buy">
                Buy Again
              </a-button>
            </template>
          </a-result>
        </div>
        <div
          :style="{
            width: '33%',
            'background-color': 'white',
            'border-radius': '5%'
          }"
        >
          <a-result
            status="success"
            title="Professional"
            sub-title="Order number: 2017182818828182881 Cloud server configuration takes 1-5 minutes, please wait."
          >
            <template #extra>
              <a-button key="console" type="primary">
                Go Console
              </a-button>
              <a-button key="buy">
                Buy Again
              </a-button>
            </template>
          </a-result>
        </div>
        <div
          :style="{
            width: '33%',
            'background-color': 'white',
            'border-radius': '5%'
          }"
        >
          <a-result
            status="success"
            title="Enterprise"
            sub-title="Order number: 2017182818828182881 Cloud server configuration takes 1-5 minutes, please wait."
          >
            <template #extra>
              <a-button key="console" type="primary">
                Go Console
              </a-button>
              <a-button key="buy">
                Buy Again
              </a-button>
            </template>
          </a-result>
        </div>
      </div>
      <h1 :style="{ 'font-size': '30px' }">Latest Premieres</h1>
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
  margin: 10px 50px 100px 50px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-gap: 10px;
  grid-template-areas:
    "header header2 advert"
    "content content advert"
    "footer footer footer";
}

.container2 {
  height: 500px;
  margin: 10px 50px 100px 50px;
  display: flex;
  justify-content: space-between;
}
</style>
