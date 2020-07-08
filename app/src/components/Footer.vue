<template>
  <a-layout-footer>
    <div class="footer">
      <div class="section1">
        <div class="item1">
          <h1 class="title">Features</h1>
          <p class="content">Cool stuff</p>
          <p class="content">Random feature</p>
          <p class="content">Team feature</p>
          <p class="content">Stuff for developers</p>
          <p class="content">Another one</p>
          <p class="content">Last time</p>
        </div>
        <div class="item1">
          <h1 class="title">Resources</h1>
          <p class="content">Resource</p>
          <p class="content">Resource name</p>
          <p class="content">Another resource</p>
          <p class="content">Final resource</p>
        </div>
        <div class="item1">
          <h1 class="title">About</h1>
          <p class="content">Team</p>
          <p class="content">Location</p>
          <p class="content">Privacy</p>
          <p class="content">Terms</p>
        </div>
        <div class="item1">
          <h1 class="title">Help</h1>
          <p class="content">Support</p>
          <p class="content">Help Center</p>
          <p class="content">Contact Us</p>
        </div>
      </div>
      <div class="section2">
        <div class="item2">
          <h1 class="title">Stay Connected</h1>
          <p class="content">
            <a><a-icon type="facebook" /> Facebook</a>
          </p>
          <p class="content">
            <a><a-icon type="twitter" /> Twitter</a>
          </p>
          <p class="content">
            <a><a-icon type="google-plus" /> Google +</a>
          </p>
        </div>
      </div>
    </div>
    <div class="section3">
      Binger ©2020 Created by The Binger Team
      <img class="small-image" src="../assets/cinema.png" alt="Movie Icon" />
    </div>
  </a-layout-footer>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
.footer {
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
}

.content {
  font-size: 12px;
  line-height: 80%;
}

.small-image {
  margin: 5px 10px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */
  .footer {
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
