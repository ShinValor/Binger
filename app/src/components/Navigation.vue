<template>
  <a-layout-header class="nav-bar">
    <div class="section">
      <Menu />
      <h1 class="app-name">
        <router-link to="/" class="app-link">
          <img class="small-image" src="@/assets/svg/binger-logo.svg" />
          Binger <i :style="{ color: 'gray', 'font-size': '15px' }">By Lala</i>
        </router-link>
      </h1>
    </div>
    <div class="section">
      <a-menu
        theme="dark"
        mode="horizontal"
        :style="{ lineHeight: '64px' }"
        v-if="!loggedIn"
      >
        <a-menu-item class="nav-btn">
          <router-link to="/about">About Us</router-link>
        </a-menu-item>
        <a-menu-item class="nav-btn">
          <router-link to="/#services">Services</router-link>
        </a-menu-item>
        <a-menu-item class="nav-btn">
          <a href="https://github.com/ShinValor/Binger">Contact</a>
        </a-menu-item>
        <a-menu-item class="nav-btn">
          <router-link to="/login">Login</router-link>
        </a-menu-item>
      </a-menu>
      <a-dropdown :trigger="['click']" :style="{ padding: '0px 20px' }" v-else>
        <a class="ant-dropdown-link" @click.prevent>
          {{ username }}
          <a-icon type="caret-down" /> <a-icon type="user" />
          <!-- <font-awesome-icon :icon="['fas', 'user']" /> -->
        </a>
        <a-menu theme="dark" slot="overlay">
          <a-menu-item key="0">
            <router-link to="/favorite-movies">My Dashboard</router-link>
          </a-menu-item>
          <a-menu-item key="1">
            <router-link to="/user">Account Setting</router-link>
          </a-menu-item>
          <!-- <a-menu-divider /> -->
          <a-menu-item key="2" @click="logout">
            <router-link to="/">Log out</router-link>
          </a-menu-item>
        </a-menu>
      </a-dropdown>
    </div>
  </a-layout-header>
</template>

<script>
import firebase from "firebase";
import Menu from "@/components/Menu.vue";

export default {
  name: "Navigation",
  components: {
    Menu
  },
  data() {
    return {
      loggedIn: false
      // username: null
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
    }
  },
  computed: {
    username() {
      return this.$store.state.userProfile["name"];
    }
  },
  created() {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        // this.username = user.displayName;
        this.loggedIn = true;
      } else {
        this.loggedIn = false;
      }
    });
  }
};
</script>

<style scoped>
.nav-bar {
  width: 100%;
  padding: 0px;
  display: flex;
  justify-content: space-between;
}

.app-name {
  margin: 0px;
}

.app-link {
  color: white;
}

.app-link:hover {
  color: pink;
}

.section {
  display: flex;
  justify-content: center;
  align-items: center;
}

.small-image {
  height: 32px;
  width: 32px;
}

.nav-btn {
  width: 100px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */
  .app-name {
    font-size: 15px;
  }

  .small-image {
    height: 16px;
    width: 16px;
  }

  .nav-btn {
    width: 100%;
  }
}
</style>
