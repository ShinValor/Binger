<template>
  <a-layout-footer>
    <div class="container">
      <div class="section1">
        <div class="item1">
          <h1 class="title">Design</h1>
            <p class="content">
              <a href="https://vuejs.org/">Vue.js</a>
            </p>
            <p class="content">
              <a href="https://ant.design/">Ant Design</a>
            </p>
        </div>
        <div class="item1">
          <h1 class="title">Resources</h1>
          <p class="content">
            <a href="https://github.com/ShinValor/Binger">Github</a>
          </p>
          <p class="content">
            <a href="https://developers.themoviedb.org/3/getting-started/introduction">TMDB API</a>
          </p>
          <p class="content">
            <a href="https://github.com/ShinValor/Binger/tree/dev/api">API</a>
          </p>
          <p class="content">
            <a href="https://firebase.google.com/">Firebase</a>
          </p>
        </div>
        <div class="item1">
          <h1 class="title">About</h1>
          <p class="content">
            <a href="https://github.com/ShinValor/Binger#contributors">Contributors</a>
          </p>
          <p class="content">
            <a href="https://binger.vercel.app/about">About Us</a>
          </p>
        </div>
        <div class="item1">
          <h1 class="title">Support</h1>
          <p class="content">
            <a href="https://github.com/junqili259">Contact Us</a>
          </p>
          <p class="content"><a href="https://github.com/ShinValor/Binger/issues">Issues</a></p>
        </div>
      </div>
    </div>
    <div class="section3" :style="{ color: 'white' }">
      Binger ©2020 Created by The Binger Team
      <img
        class="small-image"
        src="../assets/svg/binger-logo.svg"
        alt="Movie Icon"
      />
    </div>
  </a-layout-footer>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
.container {
  height: 100%;
  margin-top: 50px;
  display: flex;
  justify-content: space-between;
}

.section1 {
  width: 70%;
  margin: 0 auto;
  display: flex;
  justify-content: space-evenly;
}

.section2 {
  width: 30%;
  margin: 0 auto;
  display: flex;
}

.section3 {
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.item1 {
  width: 25%;
}

.item2 {
  width: 100%;
}

.title {
  font-size: 20px;
  color: white;
}

.content {
  font-size: 12px;
  line-height: 80%;
  color: white;
}

.small-image {
  height: 32px;
  width: 32px;
  margin: 5px 10px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */
  .container {
    flex-direction: column;
  }

  .section1 {
    width: 100%;
    flex-direction: column;
  }

  .section2 {
    width: 100%;
    flex-direction: column;
  }

  .item1 {
    width: 100%;
    margin-bottom: 20px;
    text-align: center;
  }

  .item2 {
    width: 100%;
    margin-bottom: 20px;
    text-align: center;
  }
}
</style>
