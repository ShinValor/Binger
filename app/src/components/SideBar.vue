<template>
  <a-layout id="components-sidebar">
    <a-layout-sider
      v-model="collapsed"
      :trigger="null"
      collapsible
      :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0 }"
    >
      <div class="logo" />
      <a-menu theme="dark" mode="inline" :default-selected-keys="['1']">
        <a-menu-item key="1">
          <a-icon type="user" />
          <span class="nav-text">Profile</span>
        </a-menu-item>
        <a-menu-item key="2">
          <a-icon type="appstore" />
          <span class="nav-text">Explore</span>
        </a-menu-item>
        <a-menu-item key="3">
          <a-icon type="upload" />
          <span class="nav-text">Reccomendations</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
  </a-layout>
</template>

<script>
export default {
  name: "SideBar",
  data() {
    return {
      collapsed: false
    };
  },
};
</script>

<style>
#components-layout-sidebar .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
</style>