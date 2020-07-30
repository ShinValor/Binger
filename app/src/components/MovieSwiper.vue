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
          v-if="showDraggable"
        >
          <img
            height="400"
            weight="300"
            :src="'https://image.tmdb.org/t/p/w342' + this.movie['poster_path']"
            :alt="this.movie['title']"
            onerror="this.style.display='none'"
          />
        </Vue2InteractDraggable>
      </div>
    </div>
    <div class="btn-container">
      <a-icon
        class="btn"
        type="close"
        :style="{ color: '#eb2f96' }"
        @click="dragLeft"
      />
      <a-icon
        class="btn"
        type="redo"
        :style="{ color: '#1a90ff' }"
        @click="reload"
      />
      <a-icon
        class="btn"
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
      // posterUrl: String,
      loading: false
    };
  },
  methods: {
    draggedLeft() {
      const movie = this.movie;
      this.$store.dispatch("dislikeMovie", movie);
      this.hideCard();
      this.generateMovie();
    },
    draggedRight() {
      const movie = this.movie;
      this.$store.dispatch("likeMovie", movie);
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
          "https://binger-api-testv1.azurewebsites.net/movie/random"
        );
        this.movie = res.data[0];
        // this.posterUrl = `https://image.tmdb.org/t/p/w342${this.movie["poster_path"]}`;
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

.btn-container {
  display: flex;
  justify-content: center;
  margin: 20px;
}

.btn {
  /* border: 2px solid #222831; */
  border-radius: 50%;
  margin: 0 25px;
  padding: 10px;
  font-size: 30px;
  /* color: white; */
  background-color: white;
}

.btn:hover {
  transform: scale(1.1);
}

.btn:active {
  background-color: #222;
}

.loading {
  margin: 0 auto;
  position: absolute;
  top: 50%;
  left: 42%;
  /* right: 1%; */
}
</style>
