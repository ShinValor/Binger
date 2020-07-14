<template>
  <div class="container">
    <h1 class="title">
      <b>{{ heading }}</b>
    </h1>
    <p class="description">{{ description }}</p>
    <a-button class="btn-desc"
      ><b>{{ buttonDesc }}</b></a-button
    >
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

.description {
  margin: 0 auto;
  font-size: 15px;
  color: gray;
}

.btn-desc {
  background-color: transparent;
  width: 300px;
  margin: 50px auto;
  border-color: white;
  color: white;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    font-size: 20px;
  }

  .container {
    height: 150px;
    margin: 15px;
  }

  .description {
    font-size: 10px;
    margin: 10px;
  }

  .btn-desc {
    width: 125px;
    margin: 0 auto;
    padding: 0px;
    font-size: 10px;
  }
}
</style>
