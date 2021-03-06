import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";
import "firebase/storage";

// firebase config
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

// firebase init
firebase.initializeApp(firebaseConfig);
// firebase.analytics();

// utils
const db = firebase.firestore;
const auth = firebase.auth();
const storage = firebase.storage();

// collection references
const usersCollection = db().collection("users");
const genreCollection = db().collection("genres");
const likesCollection = db().collection("likes");
const dislikesCollection = db().collection("dislikes");

// export utils
export {
  db,
  auth,
  storage,
  usersCollection,
  genreCollection,
  likesCollection,
  dislikesCollection
};
