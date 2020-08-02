<template>
  <div class="container">
    <h1 class="title">
      <b>{{ heading }}</b>
    </h1>
    <p class="desc">{{ description }}</p>
    <a-button class="desc-btn">
      <router-link to="/login">
        <b>{{ buttonDesc }}</b>
      </router-link>
    </a-button>
  </div>
</template>

<script>
export default {
  name: "Content",
  props: {
    heading: String,
    description: String,
    buttonDesc: String
  }
};
</script>

<style scoped>
.container {
  height: 350px;
  margin: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  text-align: center;
}

.title {
  margin: 0 auto;
  font-size: 35px;
  color: white;
}

.desc {
  margin: 0 auto;
  font-size: 20px;
  color: white;
}

.desc-btn {
  background-color: transparent;
  width: 300px;
  margin: 25px auto;
  /* border-color: white; */
  border-color: #f3c669;
  color: white;
}

/* .desc-btn:hover {
  border-color: gray;
  border-color: white;
} */

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    font-size: 20px;
  }

  .container {
    height: 150px;
    margin: 15px;
  }

  .desc {
    font-size: 10px;
    margin: 10px;
  }

  .desc-btn {
    width: 125px;
    margin: 0 auto;
    padding: 0px;
    font-size: 10px;
  }
}
</style>
