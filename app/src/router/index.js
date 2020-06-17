import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Movie_Synopsis from "../views/MovieSynopsis.vue";

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
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
