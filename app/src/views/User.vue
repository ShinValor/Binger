<template>
  <div class="user">
    <h1>This page will be built later</h1>
    <a-button type="primary" v-on:click="logout()">
      Log out
    </a-button>
    <a-button type="primary" v-on:click="profile()">
      Get Profile
    </a-button>
    <a-button type="primary" v-on:click="providerProfile()">
      User Provider
    </a-button>
    <!-- <a-button type="primary" v-on:click="updateProfile()">
      Update Profile
    </a-button>
    <a-button type="primary" v-on:click="updateEmail()">
      Update Email
    </a-button>
    <a-button type="primary" v-on:click="verifyEmail()">
      Verify Email
    </a-button>
    <a-button type="primary" v-on:click="setPassword()">
      Set Password
    </a-button>
    <a-button type="primary" v-on:click="resetPassword()">
      Reset Password
    </a-button>
    <a-button type="primary" v-on:click="deleteUser()">
      Delete User
    </a-button>
    <a-button type="primary" v-on:click="reauthenticate()">
      Re-authenticate User
    </a-button> -->
    <a-button type="primary" v-on:click="fetchApi()">
      Fetch Api
    </a-button>
  </div>
</template>

<script>
import firebase from "firebase";
import axios from "axios";

export default {
  name: "User",
  created() {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        console.log("You are signed in.");
      } else {
        console.log("You are not signed in.");
        this.$router.replace({ name: "Home" });
      }
    });
  },
  data() {
    return {
      info: null,
      loading: true
    };
  },
  methods: {
    logout() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          console.log("You have signed out.");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    profile() {
      const user = firebase.auth().currentUser;

      if (user != null) {
        const name = user.displayName;
        const email = user.email;
        const photoUrl = user.photoURL;
        const emailVerified = user.emailVerified;
        const uid = user.uid;
        console.log("Name: ", name);
        console.log("Email: ", email);
        console.log("Photo Url: ", photoUrl);
        console.log("Email Verified: ", emailVerified);
        console.log("Uid: ", uid);
      }
    },
    providerProfile() {
      const user = firebase.auth().currentUser;

      if (user != null) {
        user.providerData.forEach(profile => {
          console.log("Sign-in provider: " + profile.providerId);
          console.log("  Provider-specific UID: " + profile.uid);
          console.log("  Name: " + profile.displayName);
          console.log("  Email: " + profile.email);
          console.log("  Photo URL: " + profile.photoURL);
        });
      }
    },
    updateProfile() {
      const user = firebase.auth().currentUser;

      user
        .updateProfile({
          displayName: "Jane Q. User",
          photoURL: "https://example.com/jane-q-user/profile.jpg"
        })
        .then(() => {
          alert("Updated Profile");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    updateEmail() {
      const user = firebase.auth().currentUser;

      user
        .updateEmail("user@example.com")
        .then(() => {
          alert("Updated Email");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    verifyEmail() {
      const user = firebase.auth().currentUser;

      user
        .sendEmailVerification()
        .then(() => {
          alert("Email Sent");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    setPassword() {
      const user = firebase.auth().currentUser;
      const newPassword = "onetwothreefourfivesix";

      user
        .updatePassword(newPassword)
        .then(() => {
          alert("Updated Password");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    resetPassword() {
      const user = firebase.auth().currentUser;
      const emailAddress = user.email;
      const auth = firebase.auth();

      auth
        .sendPasswordResetEmail(emailAddress)
        .then(() => {
          alert("Email Sent");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    deleteUser() {
      const user = firebase.auth().currentUser;

      user
        .delete()
        .then(() => {
          alert("User Deleted");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    reauthenticate() {
      const user = firebase.auth().currentUser;
      let credential;

      user
        .reauthenticateWithCredential(credential)
        .then(function() {
          // User re-authenticated.
          alert("User Re-authenticated");
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    },
    fetchApi() {
      firebase
        .auth()
        .currentUser.getIdToken(/* forceRefresh */ true)
        .then(token => {
          console.log("Token: ", token);
          axios
            .get("http://127.0.0.1:5000/test", {
              params: {
                token: token
              }
            })
            .then(response => {
              this.info = response;
              console.log("Response: ", this.info);
            })
            .catch(error => {
              this.error = error.message;
              alert(this.error);
            })
            .finally(() => {
              this.loading = false;
            });
        })
        .catch(error => {
          this.error = error.message;
          alert(this.error);
        });
    }
  }
};
</script>
