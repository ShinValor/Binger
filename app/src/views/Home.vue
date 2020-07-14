<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div class="jumbotron">
      <h1 class="heading">
        <b>Movie Recommendation to power up your life</b>
      </h1>
      <div class="section4">
        <p class="sub-heading content">
          Hundreds of illustrated concepts to make your landing page, app, or
          presentation more attractive
        </p>
        <a-button class="sub-button">
          <router-link to="/login"><b>Learn More</b></router-link>
        </a-button>
      </div>
    </div>
    <Content
      class="content-background"
      heading="Welcome To Binger"
      description="Get started by downloading Docker Desktop, and learn how you can build, tag and share a sample image on Hub."
      buttonDesc="Get started with Binger"
    />
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
        <img class="large-image" src="../assets/svg/fast-loading-amico.svg" />
      </div>
    </div>
    <div class="container2">
      <div class="section1">
        <img class="large-image" src="../assets/svg/movie-night-amico.svg" />
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
        <img
          class="large-image"
          src="../assets/svg/ethnic-friendship-pana.svg"
        />
      </div>
    </div>
    <h1 class="title">
      <strong> How It Works </strong>
    </h1>
    <div class="container1">
      <div
        class="section3"
        :style="{
          'grid-area': 'content',
          display: 'flex',
          'justify-content': 'center',
          'margin-left': '50px',
          'margin-top': '50px'
        }"
      >
        <p class="content">
          All our illustrations come in different styles, and you can change
          main color. Just choose the one you like the most for your project.
          project. Some styles allow you to select a simple background, a more
          one, or remove it altogether. Give it a try! Some styles allow you to
          select a simple background, a more one, or remove it altogether. Give
          it a try!
        </p>
      </div>
      <div class="section3" :style="{ 'grid-area': 'header' }">
        <img class="small-image" src="../assets/svg/login-amico.svg" />
        <h2 class="sub-title">1. Sign up and Log in</h2>
      </div>
      <div class="section3" :style="{ 'grid-area': 'header2' }">
        <img
          class="small-image"
          src="../assets/svg/portfolio-update-amico.svg"
        />
        <h2 class="sub-title">2. Update Profile</h2>
      </div>
      <div class="section3" :style="{ 'grid-area': 'advert' }">
        <img class="small-image" src="../assets/svg/work-time-rafiki.svg" />
        <h2 class="sub-title">3. Wait For Recommendations</h2>
      </div>
      <div class="section3" :style="{ 'grid-area': 'footer' }">
        <img class="small-image" src="../assets/svg/movie-night-bro.svg" />
        <!-- <h2 class="sub-title">
          4. Enjoy Your Movie
        </h2> -->
      </div>
    </div>
    <!-- <h1 id="services" class="title"><b>Service Plans</b></h1>
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
    </div> -->
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
  }
};
</script>

<style scoped>
.small-image {
  height: 256px;
  width: 256px;
  margin: 0 auto;
}

.large-image {
  height: 450px;
  width: 450px;
  margin: 0 auto;
}

.jumbotron {
  height: 600px;
  width: 100%;
  background-image: url("../assets/svg/cinema-background.svg");
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
  background-color: transparent;
  width: 200px;
  margin: 20px 20px 20px 30px;
  text-align: center;
  border-color: white;
  color: white;
}

.sub-button:hover {
  border-color: gray;
}

.title {
  font-size: 35px;
  color: white;
}

.sub-title {
  color: white;
}

.content-background {
  /* background: rgb(229, 193, 233);
  background: linear-gradient(
    145deg,
    rgba(229, 193, 233, 1) 39%,
    rgba(79, 190, 252, 1) 100%
  ); */
  /* background-color: #21D4FD;
  background-image: linear-gradient(19deg, #21d4fd 0%, #b721ff 100%); */
  background-color: #8ec5fc;
  /* background-image: linear-gradient(62deg, #8ec5fc 0%, #e0c3fc 100%); */
  background-image: linear-gradient(19deg, #a18cd1 0%, #fbc2eb 100%);
}

.container1 {
  margin: 10px 50px 100px 50px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  grid-gap: 10px;
  grid-template-areas:
    "header header2 advert"
    "content content footer";
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
  /* margin: 50px; */
  color: white;
}

.progress-bar {
  margin-left: -100px;
}

@media screen and (max-width: 800px) {
  /* applies styles to any device screen sizes below 800px wide */

  .jumbotron {
    height: 250px;
  }

  .heading {
    margin: 50px 10px 10px 15px;
    width: 100px;
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
    height: 128px;
    width: 128px;
  }

  .large-image {
    height: 150px;
    width: 150px;
  }

  .progress-bar {
    margin: 50px 0px 0px 0px;
  }
}
</style>
