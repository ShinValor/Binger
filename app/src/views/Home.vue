<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <Navigation />
    <a-layout-content>
      <div class="banner">
        <h1 class="heading">
          <b>Movie Recommendation to power up your life</b>
        </h1>
        <p class="sub-heading">
          Hundreds of illustrated concepts to make your landing page, app, or
          presentation more attractive
        </p>
        <a-button class="heading-button" type="primary">
          <b>Learn More</b>
        </a-button>
        <!-- <img src="@/imgs/banner.jpg" alt="Binger Banner" /> -->
      </div>
      <Content msg="Welcome To Binger" />
      <div class="container2">
        <div class="section1">
          <h1>Optimized Movie Search Engine</h1>
          <p>
            All our illustrations come in different styles, and you can change
            the main color. Just choose the one you like the most for your
            project. Some styles allow you to select a simple background, a more
            one, or remove it altogether. Give it a try!
          </p>
        </div>
        <div class="section1">
          <img src="../assets/fast-loading.png" />
        </div>
      </div>
      <div class="container2">
        <div class="section1">
          <img src="../assets/movie-night.png" />
        </div>
        <div class="section1">
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
        <div class="section1">
          <h1>Watch With Friends</h1>
          <p>
            Some styles allow you to select a simple background, a more detailed
            one, or remove it altogether. Give it a try! Some styles allow you
            to select a simple background, a more detailed one, or remove it
            altogether. Give it a try!
          </p>
        </div>
        <div class="section1">
          <img src="../assets/friendship.png" />
        </div>
      </div>
      <h1>
        <strong> How It Works </strong>
      </h1>
      <div class="container1">
        <div class="section3" :style="{ 'grid-area': 'content' }">
          <p>
            All our illustrations come in different styles, and you can change
            the main color. Just choose the one you like the most for your
            project. Some styles allow you to select a simple background, a more
            one, or remove it altogether. Give it a try!
          </p>
        </div>
        <div class="section3" :style="{ 'grid-area': 'header' }">
          <img class="steps" src="../assets/login.png" />
          <h2>1. Sign up and Log in</h2>
        </div>
        <div class="section3" :style="{ 'grid-area': 'header2' }">
          <img class="steps" src="../assets/profile.png" />
          <h2>2. Update Profile</h2>
        </div>
        <div class="section3" :style="{ 'grid-area': 'footer' }">
          <img class="steps" src="../assets/stopwatch.png" />
          <h2>3. Wait For Recommendations</h2>
          <a-steps :current="1" class="progress-bar">
            <a-step title="Finished" description="You can hover on the dot." />
            <a-step
              title="In Progress"
              description="You can hover on the dot."
            />
            <a-step title="Waiting" description="You can hover on the dot." />
            <a-step title="Waiting" description="You can hover on the dot." />
          </a-steps>
        </div>
        <div class="section3" :style="{ 'grid-area': 'advert' }">
          <img class="watch-movie" src="../assets/watch-movie.svg" />
        </div>
      </div>
      <h1 class="margin-top">Service Plans</h1>
      <div class="container3">
        <div class="section2">
          <h2>Basic</h2>
        </div>
        <div class="section2">
          <h2>Professional</h2>
        </div>
        <div class="section2">
          <h2>Enterprise</h2>
        </div>
      </div>
      <h1 class="margin-top">Latest Premieres</h1>
      <flickity class="carousel" ref="flickity" :options="flickityOptions">
        <div class="carousel-cell">
          <img src="../imgs/wonder-woman.jpg" />
          <!-- <img
            class="carousel-cell-image"
            data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/tulip.jpg"
            alt="tulip"
          /> -->
        </div>
        <div class="carousel-cell">
          <img src="../imgs/terminator.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/logan.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/6-underground.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/joker.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/black-panther.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/black-widow.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/starwar.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/aladdin.jpg" />
        </div>
      </flickity>
      <h1 class="margin-top">Most Popular</h1>
      <flickity class="carousel" ref="flickity" :options="flickityOptions">
        <div class="carousel-cell">
          <img src="../imgs/wonder-woman.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/terminator.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/logan.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/6-underground.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/joker.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/black-panther.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/black-widow.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/starwar.jpg" />
        </div>
        <div class="carousel-cell">
          <img src="../imgs/aladdin.jpg" />
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
h1 {
  font-size: 40px;
}

p {
  font-size: 20px;
}

img {
  object-fit: cover;
  max-height: 100%;
  max-width: 100%;
}

.banner {
  height: 600px;
  width: 100%;
  background-image: url("../imgs/banner.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  flex-direction: column;
}

.heading {
  color: white;
  float: left;
  margin: 320px 0px 0px 30px;
  width: 500px;
  text-align: left;
}

.sub-heading {
  color: white;
  width: 500px;
  text-align: left;
  margin: 30px 0px 0px 30px;
}

.heading-button {
  width: 200px;
  margin: 10px 20px 20px 30px;
  background-color: transparent;
  text-align: center;
}

.carousel {
  /* background: #fafafa; */
  height: 500px;
  margin: 25px;
}

.carousel-cell {
  height: 500px;
  width: 33%;
  margin: 0px 15px;
  background: #333;
  display: flex;
  justify-content: center;
}

.carousel-cell-image {
  display: block;
  max-height: 100%;
  max-width: 100%;
  margin: 0 auto;
  opacity: 0;
  transition: opacity 0.4s;
  -webkit-transition: opacity 0.4s;
}

.carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
}

.container1 {
  margin: 10px 50px 100px 50px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-gap: 10px;
  grid-template-areas:
    "header header2 advert advert"
    "content content advert advert"
    "footer footer footer footer";
}

.container2 {
  margin: 10px 50px 100px 50px;
  display: flex;
  justify-content: space-between;
}

.container3 {
  margin: 10px 50px 100px 50px;
  display: flex;
  justify-content: space-between;
}

.section1 {
  height: 500px;
  width: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 0 auto;
}

.section2 {
  height: 500px;
  width: 33%;
  background-color: white;
  border-radius: 2%;
  margin: 10px;
}

.section3 {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

.steps {
  height: 128px;
  width: 128px;
}

.progress-bar {
  margin-left: -100px;
}

.watch-movie {
  height: 500px;
  width: 500px;
}

.margin-top {
  margin-top: 150px;
}

@media screen and (max-width: 800px) {
  /* applies styles to any device screen sizes below 800px wide */
  h1 {
    font-size: 20px;
  }

  h2 {
    font-size: 15px;
    margin: 5px;
  }

  p {
    font-size: 10px;
  }

  .banner {
    height: 250px;
  }

  .heading {
    margin: 40px 10px 10px 10px;
    width: 100px;
    color: white;
    font-size: 15px;
  }

  .sub-heading {
    width: 200px;
    margin: 10px 10px 5px 10px;
    color: white;
  }

  .heading-button {
    width: 100px;
    margin: 5px 10px;
    padding: 0;
  }

  .carousel {
    height: 150px;
    margin: 5px;
  }

  .carousel-cell {
    height: 150px;
    margin: 0px 5px;
  }

  .container1 {
    margin: 10px 10px 50px 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .container2 {
    margin: 10px 10px 50px 10px;
  }

  .container3 {
    margin: 20px;
    flex-direction: column;
    align-items: center;
  }

  .section1 {
    height: 200px;
  }

  .section2 {
    height: 300px;
    width: 250px;
  }

  .section3 {
    margin: 25px auto;
  }

  .steps {
    height: 64px;
    width: 64px;
  }

  .progress-bar {
    margin: 50px 0px;
  }

  .watch-movie {
    margin-top: -100px;
    height: 250px;
    width: 250px;
  }

  .margin-top {
    margin-top: 50px;
  }
}
</style>
