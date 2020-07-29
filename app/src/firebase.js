import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";

// firebase init
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

// utils
const db = firebase.firestore();
const auth = firebase.auth();

// collection references
const usersCollection = db.collection("users");
const postsCollection = db.collection("posts");
const commentsCollection = db.collection("comments");
const likesCollection = db.collection("likes");

// export utils/refs
export {
  db,
  auth,
  usersCollection,
  postsCollection,
  commentsCollection,
  likesCollection
};
