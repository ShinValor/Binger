<template>
  <div>
    <div class="draggable">
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
          v-if="showDraggable"
        >
          <p class="summary">
            {{ movie.overview }}
          </p>
          <img
            class="large-image"
            :src="'https://image.tmdb.org/t/p/w342' + this.movie['poster_path']"
            :alt="this.movie['title']"
            onerror="this.style.display='none'"
          />
        </Vue2InteractDraggable>
      </div>
    </div>
    <div class="section">
      <a-icon
        class="swiper-btn"
        type="close"
        :style="{ color: '#eb2f96' }"
        @click="dragLeft"
      />
      <a-icon
        class="swiper-btn"
        type="redo"
        :style="{ color: '#1a90ff' }"
        @click="reload"
      />
      <a-icon
        class="swiper-btn"
        type="heart"
        theme="twoTone"
        two-tone-color="#52c41a"
        @click="dragRight"
      />
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
      showDraggable: true,
      interactEventBusEvents: {
        draggedLeft: INTERACT_DRAGGED_LEFT,
        draggedRight: INTERACT_DRAGGED_RIGHT
      },
      movie: {},
      loading: false
    };
  },
  methods: {
    draggedLeft() {
      this.$store.dispatch("dislikeMovie", this.movie);
      this.hideCard();
      this.generateMovie();
    },
    draggedRight() {
      this.$store.dispatch("likeMovie", this.movie);
      this.hideCard();
      this.generateMovie();
    },
    reload() {
      this.hideCard();
      this.generateMovie();
    },
    dragLeft() {
      InteractEventBus.$emit(INTERACT_DRAGGED_LEFT);
    },
    dragRight() {
      InteractEventBus.$emit(INTERACT_DRAGGED_RIGHT);
    },
    hideCard() {
      setTimeout(() => {
        this.showDraggable = false;
      }, 200);
      setTimeout(() => {
        this.showDraggable = true;
      }, 1000);
    },
    async generateMovie() {
      try {
        this.loading = !this.loading;
        const res = await axios.get(
          "https://binger-api-testv1.azurewebsites.net/movie/random",
          { params: { size: 1 } }
        );
        this.movie = res.data[0];
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = !this.loading;
      }
    }
  },
  mounted() {
    this.generateMovie();
  }
};
</script>

<style scoped>
.draggable {
  height: 400px;
}

.card {
  height: 400px;
  width: 100%;
  padding: 15px;
  display: flex;
  justify-content: space-evenly;
  align-items: flex-start;
  background-color: #2a323d;
}

.summary {
  margin: 5px 10px 5px 5px;
}

.large-image {
  height: 300px;
  width: 200px;
  margin: 5px;
}

.section {
  display: flex;
  justify-content: center;
  margin: 20px;
}

.swiper-btn {
  margin: 0 25px;
  padding: 10px;
  border-radius: 50%;
  font-size: 30px;
  background-color: white;
}

.swiper-btn:hover {
  transform: scale(1.1);
}

.swiper-btn:active {
  background-color: #222;
}

.loading {
  margin: 0 auto;
  position: absolute;
  top: 50%;
  left: 40%;
}
</style>
