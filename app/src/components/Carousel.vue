<template>
  <div>
    <flickity class="carousel" ref="flickity" :options="flickityOptions">
      <div class="carousel-cell">
        <!-- <img
          class="carousel-cell-image"
          data-flickity-lazyload="https://s3-us-west-2.amazonaws.com/s.cdpn.io/82/tulip.jpg"
          alt="tulip"
        /> -->
        <img class="carousel-cell-image" src="../imgs/wonder-woman.jpg" />
        <h1 class="title">Wonder Woman</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/terminator.jpg" />
        <h1 class="title">Terminator</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/logan.jpg" />
        <h1 class="title">Logan</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
        <h1 class="title">6 Underground</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/joker.jpg" />
        <h1 class="title">Joker</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/black-panther.jpg" />
        <h1 class="title">Black Panther</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/black-widow.jpg" />
        <h1 class="title">Black Widow</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/starwar.jpg" />
        <h1 class="title">Star War</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/aladdin.jpg" />
        <h1 class="title">Aladdin</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/black-widow.jpg" />
        <h1 class="title">Black Widow</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/black-panther.jpg" />
        <h1 class="title">Black Panther</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/black-widow.jpg" />
        <h1 class="title">Black Widow</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/logan.jpg" />
        <h1 class="title">Logan</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
        <h1 class="title">6 Underground</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/logan.jpg" />
        <h1 class="title">Logan</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
        <h1 class="title">6 Underground</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
        <h1 class="title">6 Underground</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
        <h1 class="title">6 Underground</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
        <h1 class="title">6 Underground</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
      </div>
      <div class="carousel-cell">
        <img class="carousel-cell-image" src="../imgs/6-underground.jpg" />
        <h1 class="title">6 Underground</h1>
        <a-button class="btn-desc" @click="showModal">More</a-button>
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
        <img class="large-image" src="../imgs/black-widow.jpg" />
      </div>
      <a-button @click="onClick">More</a-button>
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
        freeScroll: true
        // prevNextButtons: false
      },
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
.carousel {
  margin: 10px 10px 50px;
}

.carousel-cell {
  /* background-color: #222; */
  height: 400px;
  width: 20%;
  /* margin: 0px; */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.carousel-cell:hover {
  opacity: 0.7;
}

.carousel-cell-image {
  max-height: 80%;
  max-width: 100%;
  margin: 0 auto;
  /* display: block; */
  object-fit: cover;
}

.carousel-cell-image.flickity-lazyloaded,
.carousel-cell-image.flickity-lazyerror {
  opacity: 1;
}

.title {
  margin: 5px;
  font-size: 20px;
}

.btn-desc {
  background: transparent;
  width: 225px;
  margin: 0 auto;
  text-align: center;
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
  .carousel {
    margin: 10px 10px 55px;
  }

  .carousel-cell {
    height: 125px;
    /* margin: 0px; */
  }

  .carousel-cell-image {
    max-height: 100%;
    margin: 0px;
  }

  .title {
    margin: 0px;
    font-size: 8px;
  }

  .btn-desc {
    padding: 0;
    width: 50px;
  }
}
</style>
