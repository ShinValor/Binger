<template>
  <a-layout-header class="nav-bar">
    <div class="section">
      <Menu />
      <h1 class="app-name">
        <router-link to="/" :style="{ color: 'white' }">
          <img class="small-image" src="@/assets/svg/binger-logo.svg" />
          Binger <i :style="{ color: 'gray', 'font-size': '15px' }">By Lala</i>
        </router-link>
      </h1>
    </div>
    <div class="section">
      <a-menu theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
        <a-menu-item class="nav-btn">
          <router-link to="/about">About</router-link>
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
        <a-menu-item class="tab">
          <router-link to="/signup">Register</router-link>
        </a-menu-item>
      </a-menu>
      <a-dropdown :trigger="['click']" :style="{ padding: '0px 20px' }">
        <a class="ant-dropdown-link" @click="e => e.preventDefault()">
          Shinvalor <a-icon type="caret-down" /> <a-icon type="user" />
        </a>
        <a-menu theme="dark" slot="overlay">
          <a-menu-item key="0">
            <a href="http://www.alipay.com/">1st menu item</a>
          </a-menu-item>
          <a-menu-item key="1">
            <a href="http://www.taobao.com/">2nd menu item</a>
          </a-menu-item>
          <!-- <a-menu-divider /> -->
          <a-menu-item key="2">
            3rd menu item
          </a-menu-item>
        </a-menu>
      </a-dropdown>
    </div>
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
  margin: 0px;
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
