<template>
  <a-layout-header class="header" :style="{ padding: '0px 15px 0px 15px' }">
    <router-link class="logo" to="/"></router-link>
    <h1 class="app-name">Binger</h1>
    <a-menu theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
      <a-menu-item key="1">
        <router-link to="/login">Login</router-link>
      </a-menu-item>
      <a-menu-item key="2">
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
  /* position: fixed; */
  /* z-index: 1; */
  width: 100%;
}

.logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 28px 16px 0;
}

.app-name {
  color: white;
  margin: 0px 25px 0px 25px;
}

router-link-exact-active {
  color: #42b983;
}
</style>
