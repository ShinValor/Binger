<template>
  <a-layout>
    <h1 class="team">The Binger Team</h1>
    <div class="container">
      <div class="row">
        <Card
          class="about"
          name="John"
          desc="I am a computer science major. I have experience with full stack development and Amazon web services. Beside work and school, I like to travel and hike."
        />
        <Card
          class="about"
          name="Jun"
          desc="CS major interested in system architecture and database management. I enjoy reading web novels on my break time."
        />
      </div>
      <div class="row">
        <Card
          class="about"
          name="Ferdi"
          desc="I am computer science and biochem major. I enjoy learning new things about different areas in computer science. I enjoy playing tennis and running."
        />
        <Card
          class="about"
          name="Tarik"
          desc="I am a CS major and I am interested in cyber security. I enjoy solving problems using code as my instrument. I enjoy hanging out with friends and listening to Lo-Fi."
        />
      </div>
    </div>
    <Footer class="footer" />
  </a-layout>
</template>

<script>
// @ is an alias to /src
import Card from "@/components/Card.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "About",
  components: {
    Card,
    Footer
  }
};
</script>

<style scoped>
.team {
  margin: 25px 0 0;
  font-size: 2.5em;
  color: white;
}

.container {
  margin: 0 100px 50px;
  display: flex;
  flex-direction: column;
  align-items: space-evenly;
}

.row {
  margin: 25px 0;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

.about {
  height: 500px;
  width: 450px;
}

.footer {
  margin-top: 50px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .container {
    margin: 10px;
  }

  .row {
    margin: 0px;
    flex-direction: column;
  }

  .about {
    height: 350px;
    width: 300px;
  }
}
</style>
