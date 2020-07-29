<template>
  <div>
    <div class="draggable-container">
      <div v-if="loading">
        <Loading class="loading" />
      </div>
      <div v-else>
        <Vue2InteractDraggable
          class="card"
          @draggedLeft="draggedLeft"
          @draggedRight="draggedRight"
          :interact-max-rotation="15"
          :interact-out-of-sight-x-coordinate="500"
          :interact-x-threshold="200"
          :interact-event-bus-events="interactEventBusEvents"
          :interact-lock-y-axis="true"
          v-if="isShowing"
        >
          <img height="400" weight="300" :src="moviePoster" />
        </Vue2InteractDraggable>
      </div>
    </div>
    <div class="buttons">
      <a-icon type="arrow-left" class="event-button" @click="dragLeft" />
      <a-icon type="arrow-right" class="event-button" @click="dragRight" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Vue2InteractDraggable, InteractEventBus } from "vue2-interact";
import Loading from "@/components/Loading.vue";

const INTERACT_DRAGGED_LEFT = "INTERACT_DRAGGED_LEFT";
const INTERACT_DRAGGED_RIGHT = "INTERACT_DRAGGED_RIGHT";

export default {
  name: "MovieSwiper",
  components: {
    Vue2InteractDraggable,
    Loading
  },
  data() {
    return {
      isShowing: true,
      interactEventBusEvents: {
        draggedLeft: INTERACT_DRAGGED_LEFT,
        draggedRight: INTERACT_DRAGGED_RIGHT
      },
      moviePoster: String,
      loading: false
    };
  },
  methods: {
    draggedLeft() {
      this.hideCard();
      console.log("You hate this movie");
      this.generateImage();
    },
    draggedRight() {
      this.hideCard();
      console.log("You love this movie");
      this.generateImage();
    },
    hideCard() {
      setTimeout(() => {
        this.isShowing = false;
      }, 200);
      setTimeout(() => {
        this.isShowing = true;
      }, 1000);
    },
    dragLeft() {
      InteractEventBus.$emit(INTERACT_DRAGGED_LEFT);
    },
    dragRight() {
      InteractEventBus.$emit(INTERACT_DRAGGED_RIGHT);
    },
    async generateImage() {
      try {
        this.loading = !this.loading;
        const res = await axios.get(
          "https://binger-api-testv1.azurewebsites.net/movie/random"
        );
        this.moviePoster = `https://image.tmdb.org/t/p/w342${res.data[0]["poster_path"]}`;
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = !this.loading;
      }
    }
  },
  mounted() {
    this.generateImage();
  }
};
</script>

<style scoped>
.draggable-container {
  height: 400px;
  width: 300px;
  margin: 0 auto;
}

.card {
  height: 400px;
  width: 300px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  /* background-image: url("https://picsum.photos/200/300");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center; */
}

.buttons {
  display: flex;
  justify-content: center;
  margin: 20px;
}

.event-button {
  border: 2px solid skyblue;
  border-radius: 50%;
  padding: 10px;
  font-size: 30px;
  margin: 0 75px;
}

.loading {
  margin: 0 auto;
  position: absolute;
  top: 50%;
  left: 42%;
  /* right: 1%; */
}
</style>
