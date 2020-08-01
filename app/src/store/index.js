import Vue from "vue";
import Vuex from "vuex";
import * as fb from "../firebase";
import router from "../router/index";

Vue.use(Vuex);

// realtime firebase
// fb.postsCollection.orderBy("createdOn", "desc").onSnapshot(snapshot => {
//   let postsArray = [];

//   snapshot.forEach(doc => {
//     let post = doc.data();
//     post.id = doc.id;

//     postsArray.push(post);
//   });

//   store.commit("setPosts", postsArray);
// });

const store = new Vuex.Store({
  state: {
    userProfile: {},
    likedMovies: [],
    dislikedMovies: [],
    genres: [
      { name: "Adventure", value: 0 },
      { name: "Fantasy", value: 0 },
      { name: "Animation", value: 0 },
      { name: "Drama", value: 0 },
      { name: "Horror", value: 0 },
      { name: "Comedy", value: 0 },
      { name: "History", value: 0 },
      { name: "Western", value: 0 },
      { name: "Thriller", value: 0 },
      { name: "Crime", value: 0 },
      { name: "Documentary", value: 0 },
      { name: "Science Fiction", value: 0 },
      { name: "Mystery", value: 0 },
      { name: "Music", value: 0 },
      { name: "Romance", value: 0 },
      { name: "Family", value: 0 },
      { name: "War", value: 0 },
      { name: "Action & Adventure", value: 0 },
      { name: "News", value: 0 },
      { name: "Reality", value: 0 },
      { name: "Sci-Fi & Fantasy", value: 0 },
      { name: "Soaps", value: 0 },
      { name: "Talk", value: 0 },
      { name: "War & Politics", value: 0 },
      { name: "TV Movie", value: 0 }
    ]
    // posts: [],
  },
  mutations: {
    setUserProfile(state, val) {
      state.userProfile = val;
    },
    setLikedMovies(state, val) {
      state.likedMovies = val;
    },
    setDislikedMovies(state, val) {
      state.dislikedMovies = val;
    }
    // setPerformingRequest(state, val) {
    //   state.performingRequest = val;
    // },
    // setPosts(state, val) {
    //   state.posts = val;
    // }
  },
  actions: {
    async login({ dispatch }, form) {
      // Sign user in
      const { user } = await fb.auth.signInWithEmailAndPassword(
        form.email,
        form.password
      );

      // Fetch user profile and set in state
      dispatch("fetchUserProfile", user);

      router.push("/");
    },
    async signup({ dispatch }, form) {
      // Sign user up
      const { user } = await fb.auth.createUserWithEmailAndPassword(
        form.email,
        form.password
      );

      // Create user object in userCollections
      await fb.usersCollection.doc(user.uid).set({
        name: form.name,
        description: "Add a bio"
      });

      // Fetch user profile and set in state
      dispatch("fetchUserProfile", user);

      router.push("/");
    },
    async logout({ commit }) {
      // Log user out
      await fb.auth.signOut();

      // Clear user data from state
      commit("setUserProfile", {});

      // Redirect to login view
      router.push("/login");
    },
    async fetchUserProfile({ commit }, user) {
      // Fetch user profile
      const userProfile = await fb.usersCollection.doc(user.uid).get();

      // Set user profile in state
      commit("setUserProfile", userProfile.data());

      // Change route
      // if (
      //   router.currentRoute.path === "/login" ||
      //   router.currentRoute.path === "/signup"
      // ) {
      //   router.push("/");
      // }
    },
    async fetchLikedMovies({ commit }, userId) {
      // Fetch user movie list
      const movieList = await fb.likesCollection.doc(userId).get();

      // Set user movie list in state
      commit("setLikedMovies", movieList.data().movies);
    },
    async fetchDislikedMovies({ commit }, userId) {
      // Fetch user movie list
      const movieList = await fb.dislikesCollection.doc(userId).get();

      // Set user movie list in state
      commit("setDislikedMovies", movieList.data().movies);
    },
    // eslint-disable-next-line no-unused-vars
    async likeMovie({ dispatch }, movie) {
      // const movieId = movie.id.toString();
      const userId = fb.auth.currentUser.uid;

      const likedMovies = await fb.likesCollection.doc(userId).get();
      const dislikedMovies = await fb.dislikesCollection.doc(userId).get();

      if (likedMovies.exists) {
        await fb.likesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayUnion(movie)
        });
      }

      if (dislikedMovies.exists) {
        await fb.dislikesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayRemove(movie)
        });
      }

      if (!likedMovies.exists) {
        await fb.likesCollection.doc(userId).set({
          movies: [movie]
        });
      }

      // Fetch likedMovies and set in state
      dispatch("fetchLikedMovies", userId);

      // const movieId = movie.id.toString();

      // const userId = fb.auth.currentUser.uid;
      // const docId = `${userId}_${movieId}`;

      // // Check if user has liked movie
      // const likedoc = await fb.likesCollection.doc(docId).get();
      // const dislikedoc = await fb.dislikesCollection.doc(docId).get();

      // // If user already disliked this movie
      // if (dislikedoc.exists) {
      //   await fb.dislikesCollection.doc(docId).delete();
      // }

      // // If user already liked this movie
      // if (likedoc.exists) {
      //   // console.log("You Already liked This Movie");
      //   await fb.likesCollection.doc(docId).delete();
      //   return;
      // }

      // // Like movie
      // await fb.likesCollection.doc(docId).set({
      //   movieId: movieId,
      //   userId: userId
      // });

      // update post likes count
      // fb.postsCollection.likedoc(movieId).update({
      //   likes: movie.likesCount + 1
      // });
    },
    // eslint-disable-next-line no-unused-vars
    async dislikeMovie({ dispatch }, movie) {
      // const movieId = movie.id.toString();
      const userId = fb.auth.currentUser.uid;

      const likedMovies = await fb.likesCollection.doc(userId).get();
      const dislikedMovies = await fb.dislikesCollection.doc(userId).get();

      if (dislikedMovies.exists) {
        await fb.dislikesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayUnion(movie)
        });
      }

      if (likedMovies.exists) {
        await fb.likesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayRemove(movie)
        });
      }

      if (!dislikedMovies.exists) {
        await fb.dislikesCollection.doc(userId).set({
          movies: [movie]
        });
      }

      // Fetch dislikedMovies and set in state
      dispatch("fetchDislikedMovies", userId);

      // const movieId = movie.id.toString();

      // const userId = fb.auth.currentUser.uid;
      // const docId = `${userId}_${movieId}`;

      // // Check if user disliked movie
      // const likedoc = await fb.likesCollection.doc(docId).get();
      // const dislikedoc = await fb.dislikesCollection.doc(docId).get();

      // // If user already liked this movie
      // if (likedoc.exists) {
      //   await fb.likesCollection.doc(docId).delete();
      // }

      // // If user already disliked this movie
      // if (dislikedoc.exists) {
      //   await fb.dislikesCollection.doc(docId).delete();
      //   return;
      // }

      // // Dislike movie
      // await fb.dislikesCollection.doc(docId).set({
      //   movieId: movieId,
      //   userId: userId
      // });

      // update post dislikes count
      // fb.postsCollection.dislikedoc(movieId).update({
      //   dislikes: movie.dislikesCount + 1
      // });
    },
    // async createPost({ state }, post) {
    //   // create post in firebase
    //   await fb.postsCollection.add({
    //     createdOn: new Date(),
    //     content: post.content,
    //     userId: fb.auth.currentUser.uid,
    //     userName: state.userProfile.name,
    //     comments: 0,
    //     likes: 0
    //   });
    // },
    // async updateProfile({ dispatch }, user) {
    //   const userId = fb.auth.currentUser.uid;
    //   // update user object
    //   await fb.usersCollection.doc(userId).update({
    //     name: user.name,
    //     title: user.title
    //   });

    //   dispatch("fetchUserProfile", { uid: userId });

    //   // update all posts by user
    //   const postDocs = await fb.postsCollection
    //     .where("userId", "==", userId)
    //     .get();
    //   postDocs.forEach(doc => {
    //     fb.postsCollection.doc(doc.id).update({
    //       userName: user.name
    //     });
    //   });

    //   // update all comments by user
    //   const commentDocs = await fb.commentsCollection
    //     .where("userId", "==", userId)
    //     .get();
    //   commentDocs.forEach(doc => {
    //     fb.commentsCollection.doc(doc.id).update({
    //       userName: user.name
    //     });
    //   });
    // }
    async updateProfile({ dispatch }, user) {
      const userId = fb.auth.currentUser.uid;

      console.log(user);

      // update user object
      await fb.usersCollection.doc(userId).update({
        name: user.name,
        description: user.description
      });

      dispatch("fetchUserProfile", { uid: userId });
    }
  }
});

export default store;
