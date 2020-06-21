<template>
  <a-layout-header class="header" :style="{ padding: '0' }">
    <h1 class="app-name">
      <router-link to="/" :style="{ color: 'white' }">Binger</router-link>
    </h1>
    <a-menu theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
      <a-menu-item key="1" :style="{ width: '100px' }">
        <router-link to="/login">Login</router-link>
      </a-menu-item>
      <a-menu-item key="2" :style="{ width: '100px' }">
        <router-link to="/signup">Register</router-link>
      </a-menu-item>
    </a-menu>
  </a-layout-header>
</template>

<script>
export default {
  name: "NavBar"
};
</script>

<style>
.header {
  display: flex;
  justify-content: space-between;
  /* position: fixed;
  z-index: 1; */
}

.logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 28px 16px 0;
}

.app-name {
  color: white;
  margin: 0px 25px;
}

.ant-menu-item-selected {
  background-color: transparent !important;
}

.ant-menu-item:hover {
  background-color: #1890ff !important;
}
</style>
