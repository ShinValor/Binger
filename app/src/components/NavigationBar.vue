<template>
  <a-layout-header class="header" :style="{ padding: '0' }">
    <h1 class="app-name">
      <router-link to="/" :style="{ color: 'white' }">
        <img src="../assets/logo32.png" />
        Binger
      </router-link>
    </h1>
    <div class="searchBox">
      <a-input-search placeholder="search" class="search" size="large" style="width: 200px; height: 50px" />
    </div>
    <div class="name-menu">
    <a-dropdown>
      <a class="ant-dropdown-link" @click="e => e.preventDefault()">
        {{displayName}}
        <a-icon type="down" />
      </a>
      <a-menu slot="overlay" @click="onClick">
        <a-menu-item key="1">Account Settings</a-menu-item>
        <a-menu-item key="2">Logout</a-menu-item>
      </a-menu>
    </a-dropdown>
    </div>
  </a-layout-header>
</template>

<script>
export default {
  name: "navbar",
  props: {
    displayName: {
      type: String,
      default: "Jane Doe"
    }
  }
};
</script>

<style>
.header {
  display: flex;
  justify-content: space-between;
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
.name-menu {
  float:right
}

.search {
  /* border: 10px dotted #d1d1d1;
  padding: 20px; */
  transform: scale(0.775);
  transform-origin: left;
  /* float: right; */
}

.ant-dropdown-link {
  margin: 10px 28px 10px 10px;
}

.searchBox {
  margin: 1px 0px;
  float: right
  /* padding: 5px; */
}

.ant-menu-item-selected {
  background-color: transparent !important;
}

.ant-menu-item:hover {
  background-color: #1890ff !important;
}
</style>
