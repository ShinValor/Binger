<template>
  <a-layout-header class="navigation-bar">
    <div :style="{ display: 'flex', 'justify-content': 'center' }">
      <Menu />
      <h1 class="binger">
        <router-link to="/" :style="{ color: 'white' }">
          <img class="logo" src="@/assets/logo.svg" />
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
}

.logo {
  height: 32px;
  width: 32px;
}

.tab {
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
  .binger {
    font-size: 5px;
  }

  .logo {
    height: 16px;
    width: 16px;
  }

  .tab {
    font-size: 5px;
    width: 50px;
    padding: 0px;
  }
}
</style>
