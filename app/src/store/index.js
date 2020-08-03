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
    userImage: "",
    loggedIn: Boolean,
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
    },
    setGenres(state, val) {
      state.genres[val.genre].value = val.value;
    },
    setAuthentication(state, val) {
      state.loggedIn = val;
    },
    setUserImage(state, val) {
      // state.userProfile["imageUrl"] = val;
      state.userImage = val;
    }
    // setPerformingRequest(state, val) {
    //   state.performingRequest = val;
    // },
    // setPosts(state, val) {
    //   state.posts = val;
    // }
  },
  actions: {
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
    async login({ dispatch, commit }, form) {
      // Sign user in
      const { user } = await fb.auth.signInWithEmailAndPassword(
        form.email,
        form.password
      );

      // Fetch user profile and set in state
      dispatch("fetchUserProfile", user);
      commit("setAuthentication", true);

      router.push("/");
    },
    async logout({ commit }) {
      // Log user out
      await fb.auth.signOut();

      // Clear user data from state
      commit("setUserProfile", {});
      commit("setAuthentication", false);

      // Redirect to login view
      router.push("/login");
    },
    async fetchUserProfile({ commit }, user) {
      // Fetch user profile
      const userProfile = await fb.usersCollection.doc(user.uid).get();

      // Set user profile in state
      commit("setUserProfile", userProfile.data());
    },
    async fetchUserImage({ commit }, user) {
      // Fetch user image
      let imageUrl;
      const storageRef = await fb.storage.ref().child(user.uid);

      // Get the download URL
      await storageRef
        .getDownloadURL()
        .then(function(url) {
          imageUrl = url;
        })
        .catch(function(error) {
          console.log(error.message);
        });

      // Set user profile in state
      commit("setUserImage", imageUrl);
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
    async updateProfile({ dispatch }, user) {
      const userId = fb.auth.currentUser.uid;

      // update user info
      await fb.usersCollection.doc(userId).update({
        name: user.name,
        description: user.description
      });

      dispatch("fetchUserProfile", { uid: userId });
    },
    async updateProfileImage({ dispatch }, image) {
      const userId = fb.auth.currentUser.uid;

      await fb.storage.ref(userId).put(image);

      dispatch("fetchUserImage", { uid: userId });
    },
    async likeMovie({ dispatch }, movie) {
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
    },
    async dislikeMovie({ dispatch }, movie) {
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
    },
    async updateGenres({ commit }, genre) {
      commit("setGenres", genre);
    }
  }
});

export default store;
