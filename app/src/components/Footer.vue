<template>
  <a-layout-footer>
    <div class="footer">
      <div class="section1">
        <div class="item1">
          <h1>Features</h1>
          <p>Cool stuff</p>
          <p>Random feature</p>
          <p>Team feature</p>
          <p>Stuff for developers</p>
          <p>Another one</p>
          <p>Last time</p>
        </div>
        <div class="item2">
          <h1>Resources</h1>
          <p>Resource</p>
          <p>Resource name</p>
          <p>Another resource</p>
          <p>Final resource</p>
        </div>
        <div class="item3">
          <h1>About</h1>
          <p>Team</p>
          <p>Location</p>
          <p>Privacy</p>
          <p>Terms</p>
        </div>
        <div class="item4">
          <h1>Help</h1>
          <p>Support</p>
          <p>Help Center</p>
          <p>Contact Us</p>
        </div>
      </div>
      <div class="section2">
        <div class="item5">
          <h1>Stay Connected</h1>
          <p>
            <a><a-icon type="facebook" /> Facebook</a>
          </p>
          <p>
            <a><a-icon type="twitter" /> Twitter</a>
          </p>
          <p>
            <a><a-icon type="google-plus" /> Google +</a>
          </p>
        </div>
      </div>
    </div>
    Binger ©2020 Created by The Binger Team
    <img
      src="../assets/cinema.png"
      alt="Movie Icon"
      :style="{ margin: '5px 10px' }"
    />
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
  margin-top: 100px;
  display: flex;
  justify-content: space-between;
}

.section1 {
  display: flex;
  justify-content: space-evenly;
  width: 70%;
}

.section2 {
  display: flex;
  width: 30%;
}

.item1 {
  width: 25%;
}

.item2 {
  width: 25%;
}

.item3 {
  width: 25%;
}

.item4 {
  width: 25%;
}

.item5 {
  width: 100%;
}
</style>
