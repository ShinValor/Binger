import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./assets/css/main.css";
import * as firebase from "firebase";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";

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

const db = firebase.firestore();

// db.collection("users")
//   .add({
//     first: "Ada",
//     last: "Lovelace",
//     born: 1815
//   })
//   .then(function(docRef) {
//     console.log("Document written with ID: ", docRef.id);
//   })
//   .catch(function(error) {
//     console.error("Error adding document: ", error);
//   });

new Vue({
  router,
  store,
  db,
  render: h => h(App)
}).$mount("#app");
