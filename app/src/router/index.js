import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Movie_Synopsis from "../views/MovieSynopsis.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import User from "../views/User.vue";
import Favorites from "../views/Favorites.vue";
import Recommendations from "../views/Recommendations.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/movie_synopsis",
    name: "MovieSynopsis",
    component: Movie_Synopsis
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup
  },
  {
    path: "/user",
    name: "User",
    component: User
  },
  {
    path: "/favorites",
    name: "Favorites",
    component: Favorites
  },
  {
    path: "/recommendations",
    name: "Recommendations",
    component: Recommendations
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
