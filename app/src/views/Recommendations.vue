<template>
  <a-layout
    :style="{
      minHeight: '100%',
      overflow: 'auto',
      display: 'flex',
      'flex-direction': 'column',
      'justify-content': 'space-between'
    }"
  >
    <div>
      <a-input-search
        :style="{ width: '50%', margin: '50px auto 25px' }"
        placeholder="Search Movies"
        enter-button
        @search="onSearch"
      />
      <a-tabs>
        <a-tab-pane key="1" tab="Random">
          <h1 class="title">Movies You Might Like</h1>
          <Carousel />
          <h1 class="title">Movies Other Liked</h1>
          <Carousel />
        </a-tab-pane>
        <a-tab-pane key="2" tab="Top Rated">
          Top Rated
          <!-- <a-checkable-tag v-model="action" @change="handleChange">
            Action
          </a-checkable-tag>
          <a-checkable-tag v-model="drama" @change="handleChange">
            Drama
          </a-checkable-tag>
          <a-checkable-tag v-model="comedy" @change="handleChange">
            Comedy
          </a-checkable-tag>
          <a-checkable-tag v-model="thriller" @change="handleChange" color="pink">
            Thriller
          </a-checkable-tag>
          <a-checkable-tag v-model="romance" @change="handleChange">
            Romance
          </a-checkable-tag>
          <a-checkable-tag v-model="adventure" @change="handleChange">
            Adventure
          </a-checkable-tag>
          <a-checkable-tag v-model="crime" @change="handleChange">
            Crime Film
          </a-checkable-tag> -->
        </a-tab-pane>
        <a-tab-pane key="3" tab="Most Popular">
          <h1 class="title">Popular Movies</h1>
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
        </a-tab-pane>
        <a-tab-pane key="4" tab="Most Recent">
          Most Recent
        </a-tab-pane>
        <a-tab-pane key="5" tab="Least Popular">
          Least Popular
        </a-tab-pane>
        <a-tab-pane key="6" tab="Oldest">
          Oldest
        </a-tab-pane>
      </a-tabs>
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
    <Footer></Footer>
  </a-layout>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Recommendations",
  components: {
    Carousel,
    Footer
  },
  data() {
    return {
      action: false,
      drama: false,
      comedy: false,
      thriller: false,
      romance: false,
      adventure: false,
      crime: false,
      visible: false
    };
  },
  methods: {
    onSearch(value) {
      console.log(value);
    },
    showModal() {
      this.visible = true;
    },
    onClick() {
      console.log("More");
    },
    handleChange(checked) {
      console.log(checked);
    }
  }
};
</script>

<style scoped>
.title {
  margin: 20px;
  text-align: left;
  font-size: 30px;
}

.small-image {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.container {
  margin: 10px;
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

.small-image:hover {
  opacity: 0.7;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .title {
    text-align: center;
    margin: 0 auto;
  }
}
</style>
