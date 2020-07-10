<template>
  <a-layout-header class="header" :style="{ padding: '0' }">
    <h1 class="app-name">
      <router-link to="/" :style="{ color: 'white' }">
        <img src="../assets/logo32.png" />
        Binger
      </router-link>
      <vsSidebar
        parent="body"
        default-index="1"
        color="primary"
        class="sidebarx"
        spacer
        v-model="active"
      >
        <div class="header-sidebar" slot="header">
          <a-avatar :size="70" src="https://randomuser.me/api/portraits/women/57.jpg" />
          <h4>{{ displayName }}</h4>
        </div>
        <vs-sidebar-item index="1">Home</vs-sidebar-item>
        <vs-sidebar-item index="2">Recommendations</vs-sidebar-item>
        <vs-sidebar-item index="3">Favorites</vs-sidebar-item>
        <vs-divider></vs-divider>
        <vs-sidebar-item index="4">Configurations</vs-sidebar-item>
        <vs-sidebar-item index="5">Profile</vs-sidebar-item>

        <div class="footer-sidebar" slot="footer">
          <vs-button color="danger" type="border">log out</vs-button>
          <vs-button color="primary" type="border">Settings</vs-button>
        </div>
      </vsSidebar>
      <div class="main-menu" style="padding: 0px 10px 0px 0px;">
        <a-dropdown>
          <a class="ant-dropdown-link" @click="active = !active">
            <a-icon type="menu" />
            <!-- <span>Menu</span> -->
            <!-- <a-icon type="down" /> -->
          </a>
        </a-dropdown>
      </div>
    </h1>
    <div class="name-menu">
      <a-dropdown>
        <a class="ant-dropdown-user-menu" @click="e => e.preventDefault()">
          {{ displayName }}
          <a-icon type="down" />
        </a>
        <a-menu slot="overlay">
          <a-menu-item key="1">Account Settings</a-menu-item>
          <a-menu-item key="2">Logout</a-menu-item>
        </a-menu>
      </a-dropdown>
    </div>
  </a-layout-header>
</template>

<script>
import Vue from "vue";
import { vsSideBar } from "vuesax";
import "vuesax/dist/vuesax.css";

Vue.use(vsSideBar);

export default {
  name: "NavigationBar",
  data: () => ({
    active: false
  }),
  props: {
    displayName: {
      type: String,
      default: "Jane Doe"
    }
  }
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
}
.app-name {
  color: white;
  margin: 0px 25px;
}
.name-menu {
  margin: 0px 25px;
}
.search {
  /* border: 10px dotted #d1d1d1;
  padding: 20px; */
  transform: scale(0.775);
  transform-origin: left;
  /* float: right; */
}
.ant-dropdown-user-menus {
  margin: 10px 28px 10px 10px;
}
.searchBox {
  margin: 1px 0px;
  float: right;
  /* padding: 5px; */
}
.main-menu {
  float: left;
}
.header-sidebar {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;
}
.header-sidebar h4 {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}
.header-sidebar h4 > button {
  margin-left: 10px;
}
.footer-sidebar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.footer-sidebar > button {
  border: 0px solid rgba(0, 0, 0, 0) !important;
  border-left: 1px solid rgba(0, 0, 0, 0.07) !important;
  border-right: 1px solid rgba(0, 0, 0, 0.07) !important;
  border-radius: 0px !important;
}
</style>
