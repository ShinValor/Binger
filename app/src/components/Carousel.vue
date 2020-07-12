<template>
  <div>
    <flickity class="carousel" ref="flickity" :options="flickityOptions">
      <div
        class="carousel-cell"
        v-for="(movie, index) in MovieList"
        v-bind:key="index"
      >
        <img
          class="carousel-cell-image"
          :data-flickity-lazyload="movie.url"
          :alt="movie.title"
        />
        <!-- <img class="carousel-cell-image" :src="movie.url" /> -->
        <div class="carousel-cell-desc">
          <h1 class="title">{{ movie.title }}</h1>
          <a-button class="modal-btn" @click="showModal">Synopsis</a-button>
        </div>
      </div>
    </flickity>
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
          src="https://image.tmdb.org/t/p/w342//xnopI5Xtky18MPhK40cZAGAOVeV.jpg"
        />
      </div>
      <a-button @click="onClick">More Info</a-button>
    </a-modal>
  </div>
</template>
<script>
import Flickity from "vue-flickity";

export default {
  name: "Carousel",
  components: {
    Flickity
  },
  data() {
    return {
      flickityOptions: {
        initialIndex: 0,
        autoPlay: 3000,
        groupCells: 5,
        freeScroll: true,
        // prevNextButtons: false
        lazyLoad: 2
      },
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
          title: "6 Underground",
          url: "https://image.tmdb.org/t/p/w342/ykUEbfpkf8d0w49pHh0AD2KrT52.jpg"
        },
        {
          title: "Joker",
          url: "https://image.tmdb.org/t/p/w342/bk8LyaMqUtaQ9hUShuvFznQYQKR.jpg"
        },
        {
          title: "Black Panther",
          url: "https://image.tmdb.org/t/p/w342/pU3bnutJU91u3b4IeRPQTOP8jhV.jpg"
        },
        {
          title: "Black Widow",
          url: "https://image.tmdb.org/t/p/w342/4q2NNj4S5dG2RLF9CpXsej7yXl.jpg"
        },
        {
          title: "Star War",
          url: "https://image.tmdb.org/t/p/w342/dPrUPFcgLfNbmDL8V69vcrTyEfb.jpg"
        },
        {
          title: "Aladdin",
          url: "https://image.tmdb.org/t/p/w342/AtsgWhDnHTq68L0lLsUrCnM7TjG.jpg"
        }
      ]
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
.carousel {
  margin: 10px 10px 50px;
}

.carousel-cell {
  /* background-color: #222; */
  height: 500px;
  width: 20%;
  display: flex;
  flex-direction: column;
  /* justify-content: flex-start; */
  /* border: 1px solid black; */
  margin-right: 0px;
  /* padding: 0 2px; */
}

.carousel-cell-image {
  max-height: 100%;
  max-width: 100%;
  /* margin: 0 auto; */
  /* display: block; */
  object-fit: cover;
  opacity: 0;
  -webkit-transition: opacity 0.4s;
  transition: opacity 0.4s;
}

.carousel-cell-image:hover {
  opacity: 0.7;
}

.carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
}

.carousel-cell-desc {
  background-color: #424242;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.title {
  margin: 5px;
  font-size: 20px;
  color: white;
}

.modal-btn {
  background: transparent;
  height: 30px;
  width: 200px;
  margin: 10px auto;
  text-align: center;
  color: white;
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

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .carousel-cell {
    height: 150px;
    margin-right: 0px;
  }

  .title {
    margin: 0px;
    font-size: 8px;
  }

  .modal-btn {
    height: 15px;
    width: 50px;
    margin: 5px auto;
    padding: 0;
    font-size: 8px;
  }
}
</style>
