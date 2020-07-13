<template>
  <div>
    <flickity class="carousel" ref="flickity" :options="flickityOptions">
      <div
        class="carousel-cell"
        v-for="(movie, index) in MovieList"
        v-bind:key="index"
        @click="toggleModal(movie)"
      >
        <img
          class="carousel-cell-image"
          :data-flickity-lazyload="movie.url"
          :alt="movie.title"
        />
        <div class="carousel-cell-desc">
          <h1 class="title">{{ movie.title }}</h1>
          <p class="content" :style="{ color: 'gray' }">
            <a-icon type="eye" /> 15234 Views
          </p>
        </div>
      </div>
    </flickity>
    <a-modal
      v-model="modalVisible"
      :title="modalTitle"
      :width="750"
      :footer="null"
    >
      <div :style="{ display: 'flex' }">
        <p class="content">
          {{ this.modalSummary }}
        </p>
        <img class="large-image" :src="modalImg" />
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
        groupCells: 5,
        freeScroll: true,
        lazyLoad: 2
        // autoPlay: 3000,
      },
      modalVisible: false,
      modalTitle: "",
      modalImg: "",
      modalSummary: "",
      MovieList: [
        {
          title: "Shazam",
          url: "https://image.tmdb.org/t/p/w342/xnopI5Xtky18MPhK40cZAGAOVeV.jpg"
        },
        {
          title: "Star War",
          url: "https://image.tmdb.org/t/p/w342/db32LaOibwEliAmSL2jjDF6oDdj.jpg"
        },
        {
          title: "Fantastic Beast",
          url: "https://image.tmdb.org/t/p/w342/fMMrl8fD9gRCFJvsx0SuFwkEOop.jpg"
        },
        {
          title: "Aladdin",
          url: "https://image.tmdb.org/t/p/w342/ykUEbfpkf8d0w49pHh0AD2KrT52.jpg"
        },
        {
          title: "HellBoy",
          url: "https://image.tmdb.org/t/p/w342/bk8LyaMqUtaQ9hUShuvFznQYQKR.jpg"
        },
        {
          title: "Godzilla",
          url: "https://image.tmdb.org/t/p/w342/pU3bnutJU91u3b4IeRPQTOP8jhV.jpg"
        },
        {
          title: "Spiderman",
          url: "https://image.tmdb.org/t/p/w342/4q2NNj4S5dG2RLF9CpXsej7yXl.jpg"
        },
        {
          title: "Men In Black",
          url: "https://image.tmdb.org/t/p/w342/dPrUPFcgLfNbmDL8V69vcrTyEfb.jpg"
        },
        {
          title: "Captain Marvel",
          url: "https://image.tmdb.org/t/p/w342/AtsgWhDnHTq68L0lLsUrCnM7TjG.jpg"
        }
      ]
    };
  },
  methods: {
    toggleModal(movie) {
      this.modalVisible = !this.modalVisible;
      this.modalTitle = movie.title;
      this.modalImg = movie.url;
      this.modalSummary =
        "All our illustrations come in different styles, and you can change main color. Just choose the one you like the most for your project. Some styles allow you to select a simple background, a more one, or one, or remove it altogether. Give it a try! All our illustrations come in different styles, and you can change main color. Just choose the one you like the most for your project. Some styles allow you to select a simple background, a more one, or one, or remove it altogether. Give it a try!";
    },
    onClick() {
      this.$router.push("/movie-synopsis");
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
  margin-right: 4px;
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

.carousel-cell:hover {
  opacity: 0.7;
}

.carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
}

.carousel-cell-desc {
  background-color: #001528;
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

.content {
  width: 66%;
  margin: 5px auto;
  font-size: 15px;
  /* color: white; */
}

.large-image {
  width: 33%;
  height: 100%;
  margin: 5px;
  object-fit: cover;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .carousel {
    margin: 0px 0px 50px;
  }

  .carousel-cell {
    height: 150px;
    margin-right: 0px;
  }

  .title {
    margin: 0px;
    font-size: 8px;
  }

  .content {
    margin: 0 auto;
    font-size: 5px;
  }
}
</style>
