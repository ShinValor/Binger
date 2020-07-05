<template>
  <a-layout-header class="navigation-bar">
    <div>
      <Menu />
      <h1 class="logo">
        <router-link to="/" :style="{ color: 'white' }">
          <img src="@/assets/logo32.png" />
          Binger
        </router-link>
      </h1>
    </div>
    <a-menu theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
      <a-menu-item class="tab">
        <router-link to="/about">About</router-link>
      </a-menu-item>
      <a-menu-item class="tab">
        <router-link to="/">Services</router-link>
      </a-menu-item>
      <a-menu-item class="tab">
        <router-link to="/">Contact</router-link>
      </a-menu-item>
      <a-menu-item class="tab">
        <router-link to="/login">Login</router-link>
      </a-menu-item>
      <a-menu-item class="tab">
        <router-link to="/signup">Register</router-link>
      </a-menu-item>
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

<style>
.navigation-bar {
  width: 100%;
  padding: 0px;
  display: flex;
  justify-content: space-between;
  position: fixed;
  z-index: 1;
}

.logo {
  width: 120px;
  height: 30px;
}

.tab {
  width: 100px;
}

.ant-menu-item > a{
  color: white !important;
}

.ant-menu-item-selected {
  background-color: transparent !important;
}

.ant-menu-item-selected > a {
  /* color: rgba(255, 255, 255, 0.65) !important; */
  color: white !important;
}

/* .ant-menu-item:hover {
  background-color: #1890ff !important;
} */
</style>
