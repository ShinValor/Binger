import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
import * as firebase from "firebase";

Vue.config.productionTip = false;

Vue.use(Antd);

const firebaseConfig = {
  apiKey: "AIzaSyDHOUq-c694Z3-0uHuxPutfR7Erd6u-lOg",
  authDomain: "binger-2910d.firebaseapp.com",
  databaseURL: "https://binger-2910d.firebaseio.com",
  projectId: "binger-2910d",
  storageBucket: "binger-2910d.appspot.com",
  messagingSenderId: "393236901641",
  appId: "1:393236901641:web:fb2594c6fb95687a716dd8",
  measurementId: "G-66C9TKWWSX"
};

firebase.initializeApp(firebaseConfig);
firebase.analytics();

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
