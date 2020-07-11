<template>
  <div class="column">
    <h2>Videoes</h2>

    <flickity class="carousel" ref="flickity" :options="flickityOptions">
      <div class="carousel-cell" v-for="(item,index) in trailers" v-bind:key="index">
        <img class="carousel-cell-image" :src="resolve_img_url(item.key)" @click="showModal(index)" />
      </div>
    </flickity>s
    <a-modal v-model="visible" title="Movie Trailer" :width="750" :footer="null">
      <div class="trailer-body">
        <iframe
          allowfullscreen
          frameborder="0"
          height="400"
          :src="resolve_video_url()"
          style="min-width: 600px"
        />
      </div>
      <a-button @click="onClick">More</a-button>
    </a-modal>
  </div>
</template>
<script>
import Flickity from "vue-flickity";

export default {
  name: "MovieTrailerCarousel",
  components: {
    Flickity
  },
  props: {
    trailers: {
      type: Array,
      default: function() {
        let x = JSON.parse(`[{
	"id": 1,
	"key": "QWbMckU3AOQ"
}, {
	"id": 2,
	"key": "1-q8C_c-nlM"
}, {
	"id": 3,
	"key": "Im4odVLNxqo"
}, {
	"id": 4,
	"key": "IqflOkaT5bI"
}]`);
        return x;
      }
    }
  },
  methods: {
    resolve_img_url: function(path) {
      //   console.log("https://img.youtube.com/vi/" + path + "/sddefault.jpg");
      return "https://img.youtube.com/vi/" + path + "/sddefault.jpg";
    },
    resolve_video_url: function() {
      console.log(
        "https://www.youtube.com/embed/" +
          this.trailers[this.activeTraile] +
          "?autoplay=1&modestbranding=1"
      );
      return (
        "https://www.youtube.com/embed/" +
        this.trailers[this.activeTraile] +
        "?autoplay=1&modestbranding=1"
      );
    },
    showModal(id) {
      this.visible = true;
      this.activeTraile = id;
    },
    onClick() {
      console.log("More");
      console.log(this.trailers);
    }
  },
  data() {
    return {
      flickityOptions: {
        initialIndex: 0,
        autoPlay: 3000,
        groupCells: 3,
        freeScroll: true
        // prevNextButtons: false
      },
      visible: false,
      activeTraile: 0
    };
  }
};
</script>
<style scoped>
.carousel {
  margin: 50px 30px;
}
.carousel-cell {
  height: 120px;
  width: 40%;
  margin: 1px;
  display: flex;
  justify-content: center;
}
.carousel-cell-image {
  max-height: 100%;
  max-width: 100%;
  margin: 0 auto;
  display: block;
  object-fit: cover;
}
.carousel-cell-image:hover {
  opacity: 0.7;
}
.container {
  display: flex;
}
.column {
  background-color: gray;
  margin: 1.5em;
}
</style>