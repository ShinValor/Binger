<template>
  <a-layout-header class="nav-bar">
    <div class="section">
      <Menu />
      <h1 class="app-name">
        <router-link to="/" :style="{ color: 'white' }">
          <img class="small-image" src="@/assets/logo.svg" />
          Binger <i :style="{ color: 'gray', 'font-size': '15px' }">By Lala</i>
        </router-link>
      </h1>
    </div>
    <a-menu theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
      <a-menu-item class="nav-button">
        <router-link to="/about">About</router-link>
      </a-menu-item>
      <a-menu-item class="nav-button">
        <router-link to="/">Services</router-link>
      </a-menu-item>
      <a-menu-item class="nav-button">
        <router-link to="/">Contact</router-link>
      </a-menu-item>
      <a-menu-item class="nav-button">
        <router-link to="/login">Login</router-link>
      </a-menu-item>
      <!-- <a-menu-item class="tab">
        <router-link to="/signup">Register</router-link>
      </a-menu-item> -->
    </a-menu>
  </a-layout-header>
</template>

<script>
import Menu from "@/components/Menu.vue";

export default {
  name: "Navigation",
  components: {
    Menu
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
  margin: 5px 0px;
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

.nav-button {
  width: 100px;
}

.ant-menu-item > a {
  color: white !important;
}

.ant-menu-item-selected {
  background-color: transparent !important;
}

.ant-menu-item-selected > a {
  color: white !important;
}

.ant-menu-item > a:hover {
  color: lightpink !important;
}

/* .ant-menu-item:hover {
  background-color: #1890ff !important;
} */

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */
  .app-name {
    font-size: 15px;
  }

  .small-image {
    height: 16px;
    width: 16px;
  }

  .nav-button {
    width: 100%;
  }
}
</style>
