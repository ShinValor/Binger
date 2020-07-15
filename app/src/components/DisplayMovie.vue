<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col" v-for="(movie, index) in MovieList" v-bind:key="index">
          <img
            class="small-image"
            :src="movie.url"
            :alt="movie.title"
            @click="showModal"
          />
        </div>
      </div>
      <div class="row">
        <div class="col" v-for="(movie, index) in MovieList" v-bind:key="index">
          <img
            class="small-image"
            :src="movie.url"
            :alt="movie.title"
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
        <img
          class="large-image"
          src="https://image.tmdb.org/t/p/w342/xnopI5Xtky18MPhK40cZAGAOVeV.jpg"
        />
      </div>
      <a-button @click="onClick">More Info</a-button>
    </a-modal>
  </div>
</template>

<script>
export default {
  name: "DisplayMovie",
  data() {
    return {
      visible: false,
      MovieList: [
        {
          title: "Wonder Woman",
          url: "https://image.tmdb.org/t/p/w342/xnopI5Xtky18MPhK40cZAGAOVeV.jpg"
        },
        {
          title: "Terminator",
          url: "https://image.tmdb.org/t/p/w342/db32LaOibwEliAmSL2jjDF6oDdj.jpg"
        },
        {
          title: "Logan",
          url: "https://image.tmdb.org/t/p/w342/fMMrl8fD9gRCFJvsx0SuFwkEOop.jpg"
        },
        {
          title: "Terminator",
          url: "https://image.tmdb.org/t/p/w342/pU3bnutJU91u3b4IeRPQTOP8jhV.jpg"
        },
        {
          title: "Logan",
          url: "https://image.tmdb.org/t/p/w342/4q2NNj4S5dG2RLF9CpXsej7yXl.jpg"
        }
      ]
    };
  },
  methods: {
    showModal() {
      this.visible = true;
    },
    onClick() {
      // console.log("More");
    }
  }
};
</script>

<style scoped>
.container {
  margin: 10px;
  /* display: flex; */
  /* flex-direction: column; */
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
