<template>
  <div class="content">
    <h1 class="title">
      <b>{{ heading }}</b>
    </h1>
    <div class="section">
      <p class="description"></p>
      <a-button class="description-btn">
        <router-link to="/login">
          <b>{{ button }}</b>
        </router-link>
      </a-button>
    </div>
  </div>
</template>

<script>
import typer from "typer-js";

export default {
  name: "Content",
  props: {
    heading: String,
    description: String,
    button: String
  },
  mounted() {
    typer(".description", { min: 20, max: 60 })
      .cursor({ block: true, blink: "soft", color: "#f3c669" })
      .line(this.description)
      .line("Subscribe To Movie Recommendations.")
      .line("Enjoy Movies With Friends.")
      .pause(3000)
      .back("all")
      .repeat(Infinity, true);
  }
};
</script>

<style scoped>
@import "https://unpkg.com/typer-js/typer.css";

.content {
  height: 350px;
  margin: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: #323b49;
  /* background: rgb(229, 193, 233); */
  /* background: linear-gradient(
    145deg,
    rgba(229, 193, 233, 1) 39%,
    rgba(79, 190, 252, 1) 100%
  ); */
  /* background-image: linear-gradient(19deg, #21d4fd 0%, #b721ff 100%); */
  /* background-image: linear-gradient(62deg, #8ec5fc 0%, #e0c3fc 100%); */
  /* background-image: linear-gradient(19deg, #a18cd1 0%, #fbc2eb 100%); */
}

.title {
  margin: 5px auto;
  font-size: 35px;
  color: white;
}

.section {
  padding: 10px;
}

.description {
  height: 100px;
  margin: 20px auto;
  font-size: 20px;
  color: white;
}

.description-btn {
  width: 200px;
  margin: 5px auto;
  padding: 0px;
  background-color: transparent;
  border-color: #f3c669;
  color: white;
}

.description-btn:hover {
  background-color: #f3c669;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    margin: 5px auto;
    font-size: 20px;
  }

  .content {
    height: 200px;
    margin: 15px;
  }

  .description {
    height: 80px;
    margin: 5px auto;
    font-size: 1em;
  }

  .description-btn {
    width: 100px;
  }
}
</style>
