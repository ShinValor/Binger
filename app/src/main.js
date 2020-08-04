import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { auth } from "./firebase";
import "./assets/css/main.css";

/* Ant Design */
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";

/* Font Awesome Icon */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faUser,
  faRandom,
  faAngleDoubleUp
} from "@fortawesome/free-solid-svg-icons";
// import {
//   faFacebookSquare,
//   faTwitterSquare,
//   faGooglePlusSquare,
//   faGithubSquare,
//   faVuejs
// } from "@fortawesome/free-brands-svg-icons";

Vue.config.productionTip = false;

Vue.use(Antd);

library.add(
  faUser,
  faRandom,
  faAngleDoubleUp
  // faFacebookSquare,
  // faTwitterSquare,
  // faGooglePlusSquare,
  // faGithubSquare,
  // faVuejs
);

// USAGE https://github.com/FortAwesome/vue-fontawesome#usage
/*
<font-awesome-icon :icon="['fas', 'random']" />
<font-awesome-icon :icon="['fab', 'facebook-square']" />
*/

Vue.component("font-awesome-icon", FontAwesomeIcon);

// new Vue({
//   router,
//   store,
//   render: h => h(App)
// }).$mount("#app");

let app;
auth.onAuthStateChanged(user => {
  if (!app) {
    app = new Vue({
      router,
      store,
      render: h => h(App)
    }).$mount("#app");
  }

  if (user) {
    store.commit("setAuthentication", true);
    store.dispatch("fetchUserProfile", user.uid);
    store.dispatch("fetchUserImage", user.uid);
    store.dispatch("fetchGenres", user.uid);
    store.dispatch("fetchLikedMovies", user.uid);
    store.dispatch("fetchDislikedMovies", user.uid);
  } else {
    store.commit("setAuthentication", false);
  }
});
