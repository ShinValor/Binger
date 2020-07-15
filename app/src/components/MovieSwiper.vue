<template>
  <div class="container">
    <div class="section1">
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
      </Vue2InteractDraggable>
    </div>
    <h1>Swipe</h1>
    <div class="section2">
      <a-icon type="arrow-left" class="swipe-btn" @click="dragLeft" />
      <a-icon type="arrow-right" class="swipe-btn" @click="dragRight" />
    </div>
  </div>
</template>

<script>
import { Vue2InteractDraggable, InteractEventBus } from "vue2-interact";

const INTERACT_DRAGGED_LEFT = "INTERACT_DRAGGED_LEFT";
const INTERACT_DRAGGED_RIGHT = "INTERACT_DRAGGED_RIGHT";

export default {
  name: "MovieSwiper",
  components: {
    Vue2InteractDraggable
  },
  data() {
    return {
      isShowing: true,
      interactEventBusEvents: {
        draggedLeft: INTERACT_DRAGGED_LEFT,
        draggedRight: INTERACT_DRAGGED_RIGHT
      }
    };
  },
  methods: {
    draggedLeft() {
      this.hideCard();
    },
    draggedRight() {
      this.hideCard();
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
    }
  }
};
</script>

<style scoped>
.section1 {
  display: flex;
  margin: 0 auto;
}

.section2 {
  display: flex;
  justify-content: center;
  margin: 20px;
}

.card {
  height: 600px;
  width: 400px;
  margin: 50px auto;
  background-image: url("../imgs/aladdin.jpg");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.swipe-btn {
  border: 2px solid skyblue;
  border-radius: 50%;
  padding: 10px;
  font-size: 30px;
  margin: 0 75px;
}
</style>
