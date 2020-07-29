import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ "../views/Home.vue")
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue")
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue")
  },
  {
    path: "/signup",
    name: "Signup",
    component: () => import("../views/Signup.vue")
  },
  {
    path: "/movie-synopsis/:id",
    name: "MovieSynopsis",
    component: () => import("../views/MovieSynopsis.vue")
  },
  {
    path: "/user",
    name: "User",
    component: () => import("../views/User.vue")
  },
  {
    path: "/favorite-movies",
    name: "Favorites",
    component: () => import("../views/Favorites.vue")
  },
  {
    path: "/movie-recommendations",
    name: "Recommendations",
    component: () => import("../views/Recommendations.vue")
  },
  {
    path: "/movie-list/:path",
    name: "MovieList",
    component: () => import("../views/MovieList.vue")
  },
  {
    path: "/search-results",
    name: "Search",
    component: () => import("../views/SearchResults.vue")
  },
  {
    path: "**",
    name: "PageNotFound",
    component: () => import("../views/PageNotFound.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 };
  }
});

export default router;
