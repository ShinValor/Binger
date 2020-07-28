<template>
  <PushRotate width="250">
    <!-- <a-menu
      style="width: 256px"
      :default-selected-keys="['1']"
      :default-open-keys="['sub1']"
      mode="inline"
      :theme="theme"
      :selected-keys="[current]"
      @click="handleClick"
    >
      <a-menu-item key="1">
        <a-icon type="mail" />
        Movie Recommendations
      </a-menu-item>
      <a-menu-item key="2">
        <a-icon type="calendar" />
        Movie Summary
      </a-menu-item>
      <a-sub-menu key="sub1">
        <span slot="title"
          ><a-icon type="appstore" /><span>Movie List</span></span
        >
        <a-menu-item key="3">
          Option 3
        </a-menu-item>
        <a-sub-menu key="sub1-2" title="Submenu">
          <a-menu-item key="5">
            Option 5
          </a-menu-item>
        </a-sub-menu>
      </a-sub-menu>
      <a-sub-menu key="sub2">
        <span slot="title"
          ><a-icon type="setting" /><span>Navigation Four</span></span
        >
        <a-menu-item key="6">
          Option 6
        </a-menu-item>
      </a-sub-menu>
    </a-menu> -->
    <router-link to="/movie-recommendations">
      <span>Recommendation</span>
    </router-link>
  </PushRotate>
</template>

<script>
import { PushRotate } from "vue-burger-menu";

export default {
  name: "Menu",
  components: {
    PushRotate
  }
};
</script>

<style>
.bm-burger-button {
  top: 0 !important;
  left: 0 !important;
  width: 25px !important;
  height: 20px !important;
  margin: 25px 10px !important;
  position: relative !important;
}

.bm-burger-bars {
  background-color: white !important;
}

.line-style {
  position: absolute;
  height: 10% !important;
  left: 0;
  right: 0;
}

.cross-style {
  position: absolute;
  top: 12px;
  right: 2px;
  cursor: pointer;
}

.bm-cross {
  background: #bdc3c7;
}

.bm-cross-button {
  height: 24px;
  width: 24px;
}

.bm-menu {
  background-color: rgb(63, 63, 65, 0.85) !important;
  top: 0;
  left: 0;
  height: 100%; /* 100% Full-height */
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  z-index: 1000; /* Stay on top */
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 60px; /* Place content 60px from the top */
  transition: 0.5s; /*0.5 second transition effect to slide in the sidenav*/
}

.bm-overlay {
  background: rgba(0, 0, 0, 0.3);
}

.bm-item-list {
  color: #b8b7ad;
  /* margin-left: 5% !important; */
  margin-left: 0% !important;
  font-size: 18px !important;
}

.bm-item-list > * {
  display: flex;
  text-decoration: none;
  /* padding: 0.7em; */
  padding: 0 !important;
}

.bm-item-list > * > span {
  margin-left: 10px;
  font-weight: 700;
  color: white;
  /* color: black; */
}

@media screen and (max-width: 800px) {
  /* applies styles to any device screen sizes below 800px wide */

  .bm-burger-button {
    width: 15px !important;
    height: 10px !important;
    margin: 33px 10px !important;
  }

  .bm-item-list {
    font-size: 15px !important;
  }

  .bm-item-list > * {
    padding: 0 !important;
  }
}
</style>
