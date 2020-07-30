import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { auth } from "./firebase";
import "./assets/css/main.css";

import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faRandom } from "@fortawesome/free-solid-svg-icons";

Vue.config.productionTip = false;

Vue.use(Antd);

library.add(faRandom);
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
    store.dispatch("fetchUserProfile", user);
  }
});
