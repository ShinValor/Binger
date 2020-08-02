<template>
  <PushRotate width="250">
    <div class="sidebar">
      <header class="sidebar-header" v-if="this.$store.state.loggedIn">
        <a-avatar :size="64" icon="user" class="ant-icon" />
        <span class="username">{{ username }}</span>
      </header>
      <header class="sidebar-header" v-else>
        <a-avatar :size="64" icon="user" class="ant-icon" />
        <span class="username">Not Sign In</span>
      </header>
      <!-- <div class="break"></div> -->
      <div class="sidebar-list">
        <div
          :class="activeRoute('Home') ? 'current-route' : ''"
          class="sidebar-item"
        >
          <router-link class="link" to="/">
            <span>Home</span>
          </router-link>
        </div>
        <div
          :class="activeRoute('About') ? 'current-route' : ''"
          class="sidebar-item"
        >
          <router-link class="link" to="/about">
            <span>About</span>
          </router-link>
        </div>
        <div
          :class="activeRoute('Recommendations') ? 'current-route' : ''"
          class="sidebar-item"
          v-if="this.$store.state.loggedIn"
        >
          <router-link class="link" to="/movie-recommendations">
            <span>Search Movies</span>
          </router-link>
        </div>
        <div
          :class="activeRoute('Favorites') ? 'current-route' : ''"
          class="sidebar-item"
          v-if="this.$store.state.loggedIn"
        >
          <router-link class="link" to="/favorite-movies">
            <span>My Favorites</span>
          </router-link>
        </div>
        <div
          :class="activeRoute('Login') ? 'current-route' : ''"
          class="sidebar-item"
          v-if="!this.$store.state.loggedIn"
        >
          <router-link class="link" to="/login">
            <span>Login</span>
          </router-link>
        </div>
      </div>
    </div>
  </PushRotate>
</template>

<script>
import { PushRotate } from "vue-burger-menu";

export default {
  name: "Menu",
  components: {
    PushRotate
  },
  methods: {
    activeRoute(check) {
      return this.$route.name === check ? true : false;
    }
  },
  computed: {
    username() {
      return this.$store.state.userProfile["name"];
    }
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

.bm-burger-button:hover {
  transform: scale(1.1);
  -webkit-transform: scale(1.1);
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
  background-color: rgb(44, 62, 80, 0.85) !important;
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

  .ant-icon {
    display: block;
  }
}

.sidebar {
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 10px 5px;
  border-bottom: 1px solid white;
  display: flex;
  align-content: center;
  align-items: center;
  flex-direction: column;
}

.sidebar-list {
  padding: 10px 0;
  /* overflow-y: auto; */
  display: block;
}

.sidebar-item {
  text-align: left;
  margin: 0;
  padding: 0;
  -webkit-transition: all 0.25s ease;
  transition: all 0.25s ease;
  box-sizing: border-box;
  /* display: inline; */
  /* width: 100%;
  height: 40px; */
  width: auto;
  height: auto;
  padding: 10px;
  /* display: inline-block; */
  line-height: 1.5;
  /* color: #faa5de; */
}
.username {
  color: white;
  font-weight: 600;
}

.break {
  flex-basis: 100%;
  height: 0;
}

.current-route {
  border-right: 3px solid#f3c669 !important;
  color: #f3c669;
  font-weight: 900;
  pointer-events: none;
}

.link {
  color: inherit;
}

.link:active,
.link:hover {
  color: #f3c669;
}
</style>
