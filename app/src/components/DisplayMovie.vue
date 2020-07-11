<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/aladdin.jpg"
            alt="Aladdin"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/joker.jpg"
            alt="The Joker"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/starwar.jpg"
            alt="Star War"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/logan.jpg"
            alt="Logan"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/wonder-woman.jpg"
            alt="Wonder Woman"
            @click="showModal"
          />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/black-panther.jpg"
            alt="Black Panther"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/joker.jpg"
            alt="The Joker"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/6-underground.jpg"
            alt="6-underground"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/joker.jpg"
            alt="The Joker"
            @click="showModal"
          />
        </div>
        <div class="col">
          <img
            class="small-image"
            src="@/imgs/black-widow.jpg"
            alt="Black Widow"
            @click="showModal"
          />
        </div>
      </div>
    </div>
    <a-modal
      v-model="visible"
      title="Movie Summary"
      :width="750"
      :footer="null"
    >
      <div :style="{ display: 'flex' }">
        <p class="content">
          All our illustrations come in different styles, and you can change
          main color. Just choose the one you like the most for your project.
          Some styles allow you to select a simple background, a more one, or
          one, or remove it altogether. Give it a try!
        </p>
        <p class="content">
          All our illustrations come in different styles, and you can change
          main color. Just choose the one you like the most for your project.
          Some styles allow you to select a simple background, a more one, or
          one, or remove it altogether. Give it a try!
        </p>
        <img class="large-image" src="../imgs/black-widow.jpg" />
      </div>
      <a-button @click="onClick">More</a-button>
    </a-modal>
  </div>
</template>

<script>
export default {
  name: "DisplayMovie",
  data() {
    return {
      visible: false
    };
  },
  methods: {
    showModal() {
      this.visible = true;
    },
    onClick() {
      console.log("More");
    }
  }
};
</script>

<style scoped>
.container {
  margin: 10px;
  display: flex;
  flex-direction: column;
}

.container .row {
  display: flex;
}
.container .row .col {
  width: 20%;
  margin: 10px;
}

.content {
  width: 66%;
  margin: 5px;
  font-size: 15px;
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
}

.small-image {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.small-image:hover {
  opacity: 0.7;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .container .row .col {
    margin: 1px;
  }
}
</style>
