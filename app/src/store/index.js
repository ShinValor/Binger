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
    genres: [],
    likedMovies: [],
    dislikedMovies: []
    // posts: [],
  },
  mutations: {
    setUserProfile(state, val) {
      state.userProfile = val;
    },
    setUserImage(state, val) {
      state.userImage = val;
    },
    setAuthentication(state, val) {
      state.loggedIn = val;
    },
    setGenres(state, val) {
      state.genres = val;
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
    async login({ dispatch }, form) {
      // Sign user in
      const { user } = await fb.auth.signInWithEmailAndPassword(
        form.email,
        form.password
      );

      // Fetch user profile and set in state
      dispatch("fetchUserProfile", user.uid);

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
    async fetchUserProfile({ commit }, userId) {
      // Fetch user profile
      const userProfile = await fb.usersCollection.doc(userId).get();

      // Set user profile in state
      commit("setUserProfile", userProfile.data());
    },
    async fetchUserImage({ commit }, userId) {
      // Fetch user image
      const storageRef = await fb.storage.ref().child(userId);

      // Get the download URL
      await storageRef
        .getDownloadURL()
        .then(url => {
          // Set user profile in state
          commit("setUserImage", url);
        })
        .catch(error => {
          console.log(error.message);
        });
    },
    async fetchGenres({ commit }, userId) {
      // Fetch genre
      const genres = await fb.genreCollection.doc(userId).get();
      // console.log("LALA", genres.data().genres);

      // Set user genre in state
      commit("setGenres", genres.data().genres);
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

      dispatch("fetchUserProfile", userId);
    },
    async updateProfileImage({ dispatch }, image) {
      const userId = fb.auth.currentUser.uid;

      await fb.storage.ref(userId).put(image);

      dispatch("fetchUserImage", userId);
    },
    async updateGenres({ dispatch }, genres) {
      const userId = fb.auth.currentUser.uid;
      const favoriteGenres = await fb.genreCollection.doc(userId).get();

      if (favoriteGenres.exists) {
        const dataset = favoriteGenres.data().genres;

        genres.map(genre => {
          let added = false;
          favoriteGenres.data().genres.map((data, index) => {
            if (data.name === genre) {
              dataset[index].value += 1;
              added = true;
            }
          });
          if (added === false) {
            dataset.push({ name: genre, value: 1 });
          }
        });

        await fb.genreCollection.doc(userId).update({
          genres: dataset
        });
      } else {
        const dataset = [];

        genres.map(genre => {
          dataset.push({ name: genre, value: 1 });
        });

        await fb.genreCollection.doc(userId).set({
          genres: dataset
        });
      }

      dispatch("fetchGenres", userId);
    },
    async likeMovie({ dispatch }, movie) {
      const userId = fb.auth.currentUser.uid;
      const likedMovies = await fb.likesCollection.doc(userId).get();
      const dislikedMovies = await fb.dislikesCollection.doc(userId).get();

      if (likedMovies.exists) {
        await fb.likesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayUnion(movie)
        });
      } else {
        await fb.likesCollection.doc(userId).set({
          movies: [movie]
        });
      }

      if (dislikedMovies.exists) {
        await fb.dislikesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayRemove(movie)
        });
      }

      // Fetch likedMovies and set in state
      dispatch("fetchLikedMovies", userId);

      // Update Genres
      dispatch("updateGenres", movie.genres);
    },
    async dislikeMovie({ dispatch }, movie) {
      const userId = fb.auth.currentUser.uid;
      const likedMovies = await fb.likesCollection.doc(userId).get();
      const dislikedMovies = await fb.dislikesCollection.doc(userId).get();

      if (dislikedMovies.exists) {
        await fb.dislikesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayUnion(movie)
        });
      } else {
        await fb.dislikesCollection.doc(userId).set({
          movies: [movie]
        });
      }

      if (likedMovies.exists) {
        await fb.likesCollection.doc(userId).update({
          movies: fb.db.FieldValue.arrayRemove(movie)
        });
      }

      // Fetch dislikedMovies and set in state
      dispatch("fetchDislikedMovies", userId);
    }
  }
});

export default store;
