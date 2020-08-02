<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div class="jumbotron">
      <h1 class="heading">
        <b>Movie Recommendation to power up your life</b>
      </h1>
      <div class="section3">
        <p class="sub-heading content">
          Millions of movies, TV shows and people to discover. Explore now.
        </p>
        <a-button class="sub-button">
          <a href="/#how-it-work"><b>Learn More</b></a>
        </a-button>
      </div>
    </div>
    <Content
      class="content-background"
      heading="Welcome To Binger"
      description="Get started by signing up Binger, and learn how you can find movies and shows you like."
      buttonDesc="Get started with Binger"
    />
    <div class="container2">
      <div class="section1">
        <h1 class="title"><b>Optimized Movie Search Engine</b></h1>
        <p class="content">
          Our optimized movie search engine has millions of movies and shows to
          query from. Movies and shows are added to a weighted queue, duplicates
          increase weight. Based on user decisions the weight will increase
          likes and decrease on dislikes.
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
          Summer may be slipping away but it’s still the perfect time to take
          movie night outside. Public parks and rooftops offer free and ticketed
          outdoor screenings across the city. Prepare your picnic blanket to
          watch your favorite films under the stars.
        </p>
      </div>
    </div>
    <div class="container2">
      <div class="section1">
        <h1 class="title"><b>Watch With Friends</b></h1>
        <p class="content">
          Imagine being able to watch your favorite Netflix web series or movies
          with your best friends while social distancing. Using Binger you can
          now search for your favorite movies and shows.
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
    <div class="container1">
      <div
        class="section2"
        :style="{
          'grid-area': 'content',
          display: 'flex',
          'justify-content': 'center'
        }"
      >
        <p class="content">
          During the quarantine, people have watched all the movies and shows on
          their movie queues and are left looking for something new to watch.
          Streaming services have huge libraries and it takes effort and time to
          find a show. There is no centralized movie queue across different
          streaming services.
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
        <h2 class="sub-title">3. Wait For Recommendations</h2>
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
  /* border-color: white; */
  border-color: #f3c669;
  color: white;
}

/* .sub-button:hover {
  border-color: gray;
  border-color: white;
} */

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
  /* background-color: #21D4FD; */
  /* background-image: linear-gradient(19deg, #21d4fd 0%, #b721ff 100%); */
  /* background-color: #8ec5fc; */
  /* background-image: linear-gradient(62deg, #8ec5fc 0%, #e0c3fc 100%); */
  /* background-color: #323b49; */
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
  margin: 10px 50px 50px 50px;
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
    margin: 10px auto;
  }

  .section3 {
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
