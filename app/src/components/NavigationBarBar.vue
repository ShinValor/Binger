<template>
  <div class="navbar-nav">
    <div class="navbar-nav__item">
      <router-link to="/user">{{displayName}}</router-link>
      <button class="navbar-nav__icon" @click="onClick">
        <icon name="chevron-down" />
      </button>
    </div>
    <transition name="fade">
      <ul class="navbar-nav__dropdown" v-show="isVisible">
        <li class="navbar-nav__list-item">Account Settings</li>
        <li class="navbar-nav__list-item">Logout</li>
      </ul>
    </transition>
  </div>
</template>

<script>
  
  export default {
    name: "NavigationBarBar",
    props: {
        displayName: {
            type: String,
            default: "Jane Doe"
        }
    },
    data() {
      return {
        isVisible: false
      };
    },
    methods: {
      onClick() {
        this.isVisible = !this.isVisible;
        if (this.isVisible) {
          setTimeout(
            () => document.addEventListener("click", this.clickOutEvent),
            100
          );
        } else {
          this.close();
        }
      },
      close: function() {
        this.isVisible = false;
        document.removeEventListener("click", this.clickOutEvent);
      }
    }
  };


</script>

<style scoped lang="sass">
  .navbar-nav
    position: relative
    z-index: 10
    &__item
      display: flex
      align-items: center
      height: 40px
    &__link
      color: #fff
      font-size: 13px
      &:hover
        text-decoration: underline
    &__icon
      margin: 0 6px
      color: #fff
      font-size: 12px
      line-height: 0
      outline: none
      cursor: pointer
    &__dropdown
      font:
        size: 13px
        weight: normal
      background: #404040
      box-shadow: -2px 2px 5px 0 rgba(0, 0, 0, .75)
    &__list-item
      padding: 10px
      cursor: pointer
      &:hover
        background: #2f2f2f
    .fade-enter-active,
    .fade-leave-active
      transition: opacity .3s
    .fade-enter,
    .fade-leave-to
      opacity: 0
</style>