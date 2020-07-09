<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div class="banner">
      <h1 class="heading">
        <b>Movie Recommendation to power up your life</b>
      </h1>
      <div class="section4">
        <p class="sub-heading content">
          Hundreds of illustrated concepts to make your landing page, app, or
          presentation more attractive
        </p>
        <a-button class="sub-button" type="primary">
          <router-link to="/login"><b>Learn More</b></router-link>
        </a-button>
      </div>
      <!-- <img src="@/imgs/banner.jpg" alt="Binger Banner" /> -->
    </div>
    <Content msg="Welcome To Binger" />
    <div class="container2">
      <div class="section1">
        <h1 class="title"><b>Optimized Movie Search Engine</b></h1>
        <p class="content">
          All our illustrations come in different styles, and you can change
          main color. Just choose the one you like the most for your project.
          project. Some styles allow you to select a simple background, a more
          one, or remove it altogether. Give it a try!
        </p>
      </div>
      <div class="section1">
        <img class="large-image" src="../assets/fast-loading.png" />
      </div>
    </div>
    <div class="container2">
      <div class="section1">
        <img class="large-image" src="../assets/movie-night.png" />
      </div>
      <div class="section1">
        <h1 class="title"><b>Movie Nights</b></h1>
        <p class="content">
          Do you want the illustrations to come to life on your website? You
          animate them directly with our online editor! Some styles allow you to
          you to select a simple background, a more detailed one, or remove it
          altogether. Give it a try!
        </p>
      </div>
    </div>
    <div class="container2">
      <div class="section1">
        <h1 class="title"><b>Watch With Friends</b></h1>
        <p class="content">
          Some styles allow you to select a simple background, a more detailed
          one, or remove it altogether. Give it a try! Some styles allow you
          select a simple background, a more detailed one, or remove it
          altogether. Give it a try!
        </p>
      </div>
      <div class="section1">
        <img class="large-image" src="../assets/friendship.png" />
      </div>
    </div>
    <h1 class="title">
      <strong> How It Works </strong>
    </h1>
    <div class="container1">
      <div class="section3" :style="{ 'grid-area': 'content' }">
        <p class="content">
          All our illustrations come in different styles, and you can change
          main color. Just choose the one you like the most for your project.
          project. Some styles allow you to select a simple background, a more
          one, or remove it altogether. Give it a try!
        </p>
      </div>
      <div class="section3" :style="{ 'grid-area': 'header' }">
        <img class="small-image" src="../assets/login.png" />
        <h2 class="sub-title">1. Sign up and Log in</h2>
      </div>
      <div class="section3" :style="{ 'grid-area': 'header2' }">
        <img class="small-image" src="../assets/profile.png" />
        <h2 class="sub-title">2. Update Profile</h2>
      </div>
      <div class="section3" :style="{ 'grid-area': 'footer' }">
        <img class="small-image" src="../assets/stopwatch.png" />
        <h2 class="sub-title">3. Wait For Recommendations</h2>
        <a-steps :current="1" class="progress-bar">
          <a-step title="Finished" description="Logged In" />
          <a-step title="In Progress" description="Updating Profile" />
          <a-step title="Waiting" description="Select Favorite Movie Genre" />
          <a-step title="Waiting" description="Search Movie . . ." />
        </a-steps>
      </div>
      <div class="section3" :style="{ 'grid-area': 'advert' }">
        <img class="large-image" src="../assets/watch-movie.svg" />
        <h2 class="sub-title">4. Enjoy Your Movie</h2>
      </div>
    </div>
    <h1 id="services" class="title"><b>Service Plans</b></h1>
    <div class="container3">
      <div class="section2">
        <h2 class="sub-title">Basic</h2>
      </div>
      <div class="section2">
        <h2 class="sub-title">Professional</h2>
      </div>
      <div class="section2">
        <h2 class="sub-title">Enterprise</h2>
      </div>
    </div>
    <Footer />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Content from "@/components/Content.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Home",
  components: {
    Content,
    Footer
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
.small-image {
  height: 128px;
  width: 128px;
}

.large-image {
  height: 500px;
  width: 500px;
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
  font-size: 40px;
}

.sub-heading {
  color: white;
  width: 500px;
  text-align: left;
  margin: 30px 0px 0px 30px;
}

.sub-button {
  width: 200px;
  margin: 10px 20px 20px 30px;
  background-color: transparent;
  text-align: center;
}

.title {
  font-size: 35px;
}

/* .sub-title {
} */

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
  margin: 10px 50px 50px 50px;
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

.section4 {
  display: flex;
  flex-direction: column;
}

.content {
  font-size: 20px;
}

.progress-bar {
  margin-left: -100px;
}

@media screen and (max-width: 800px) {
  /* applies styles to any device screen sizes below 800px wide */

  .banner {
    height: 250px;
  }

  .heading {
    margin: 50px 10px 10px 15px;
    width: 100px;
    color: white;
    font-size: 15px;
  }

  .sub-heading {
    width: 200px;
    margin: 10px 10px 5px 15px;
    color: white;
  }

  .sub-button {
    width: 100px;
    margin: 20px 10px 10px 10px;
    padding: 0;
  }

  .title {
    font-size: 20px;
  }

  .sub-title {
    font-size: 15px;
    margin: 5px;
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
    margin: 10px auto;
  }

  .section4 {
    margin-top: 15px;
    flex-direction: row;
    justify-content: space-between;
  }

  .content {
    font-size: 10px;
  }

  .small-image {
    height: 64px;
    width: 64px;
  }

  .large-image {
    height: 250px;
    width: 250px;
  }

  .progress-bar {
    margin: 50px 0px 0px 0px;
  }
}
</style>
