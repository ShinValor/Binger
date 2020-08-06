<template>
  <a-layout>
    <div class="jumbotron">
      <h1 class="heading">
        <b>Movie Recommendation to power up your life</b>
      </h1>
      <div class="section3">
        <p class="sub-heading content">
          Millions of Movies, TV Shows And, People To Discover. Explore Now.
        </p>
        <a-button class="sub-btn">
          <a href="/#how-it-work"><b>Learn More</b></a>
        </a-button>
      </div>
    </div>
    <Content
      heading="Welcome To Binger"
      description="Learn How You Can Find Your Favorite Movies And Shows."
      button="Get started"
    />
    <div class="container1">
      <div class="section1">
        <h1 class="title"><b>Optimized Movie Search Engine</b></h1>
        <p class="content">
          Our optimized movie search engine has millions of movies and shows to
          query from. Based on user preferences, Binger will recommend the
          movies and shows you enjoy.
        </p>
      </div>
      <div class="section1">
        <img class="large-image" src="../assets/svg/fast-loading-amico.svg" />
      </div>
    </div>
    <div class="container1">
      <div class="section1">
        <img class="large-image" src="../assets/svg/movie-night-amico.svg" />
      </div>
      <div class="section1">
        <h1 class="title"><b>Movie Nights</b></h1>
        <p class="content">
          Summer may be slipping away but it’s still the perfect time to take
          movie night outside. Public parks and rooftops offer free outdoor
          screenings across the city.
        </p>
      </div>
    </div>
    <div class="container1">
      <div class="section1">
        <h1 class="title"><b>Watch With Friends</b></h1>
        <p class="content">
          Imagine being able to watch your favorite Netflix series with your
          best friends while social distancing. With Binger you can now search
          for your favorite movies and shows.
        </p>
      </div>
      <div class="section1">
        <img
          class="large-image"
          src="../assets/svg/ethnic-friendship-pana.svg"
        />
      </div>
    </div>
    <h1 class="title" id="how-it-work">
      <strong> How It Works </strong>
    </h1>
    <div class="container2">
      <div class="section2" :style="{ 'grid-area': 'content' }">
        <p class="content">
          During quarantine, people needed to look for new movies and shows to
          binge to kill time.<br />
          Streaming services have huge libraries and it takes lots of effort to
          search for movies.<br />
          There is also no centralized movie queue across different streaming
          services.
        </p>
      </div>
      <div class="section2" :style="{ 'grid-area': 'header' }">
        <img class="small-image" src="../assets/svg/login-amico.svg" />
        <h2 class="sub-title">1. Sign up and Log in</h2>
      </div>
      <div class="section2" :style="{ 'grid-area': 'header2' }">
        <img
          class="small-image"
          src="../assets/svg/portfolio-update-amico.svg"
        />
        <h2 class="sub-title">2. Update Profile</h2>
      </div>
      <div class="section2" :style="{ 'grid-area': 'advert' }">
        <img class="small-image" src="../assets/svg/work-time-rafiki.svg" />
        <h2 class="sub-title">3. Look For Recommendations</h2>
      </div>
      <div class="section2" :style="{ 'grid-area': 'footer' }">
        <img class="small-image" src="../assets/svg/movie-night-bro.svg" />
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
  }
};
</script>

<style scoped>
.jumbotron {
  height: 600px;
  width: 100%;
  display: flex;
  flex-direction: column;
  background-image: url("../assets/svg/cinema-background.svg");
  background-repeat: no-repeat;
  background-size: cover;
}

.heading {
  color: white;
  float: left;
  margin: 320px 0px 0px 50px;
  width: 500px;
  text-align: left;
  font-size: 40px;
}

.sub-heading {
  color: white;
  width: 500px;
  text-align: left;
  margin: 30px 0px 0px 50px;
}

.sub-btn {
  background-color: transparent;
  width: 200px;
  margin: 20px 20px 20px 50px;
  text-align: center;
  border-color: #f3c669;
  color: white;
}

.sub-btn:hover {
  background-color: #f3c669;
}

.title {
  font-size: 35px;
  color: white;
}

.sub-title {
  color: white;
}

.container1 {
  margin: 10px 50px 50px 50px;
  display: flex;
  justify-content: space-between;
}

.container2 {
  margin: 10px 50px 100px 50px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  grid-gap: 10px;
  grid-template-areas:
    "header header2 advert"
    "content content footer";
}

.section1 {
  height: 500px;
  width: 50%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.section2 {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

.section3 {
  display: flex;
  flex-direction: column;
}

.content {
  font-size: 20px;
  color: white;
}

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

@media screen and (max-width: 800px) {
  /* applies styles to any device screen sizes below 800px wide */

  .jumbotron {
    height: 250px;
  }

  .heading {
    margin: 90px 15px 10px;
    width: 100px;
    font-size: 15px;
  }

  .sub-heading {
    width: 200px;
    margin: 10px 15px;
    color: white;
  }

  .sub-btn {
    width: 100px;
    margin: 10px;
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
    margin: 10px 10px 50px 15px;
  }

  .container2 {
    margin: 10px 10px 50px 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .section1 {
    height: 200px;
  }

  .section2 {
    margin: 10px auto;
  }

  .section3 {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
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
}
</style>
