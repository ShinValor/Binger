<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div class="container">
      <Profile></Profile>
      <Card name="John" desc="I am a student." />
    </div>
    <!-- <a-button type="primary" v-on:click="logout()">
      Log out
    </a-button> -->
    <!-- <a-button type="primary" v-on:click="profile()">
      Get Profile
    </a-button>
    <a-button type="primary" v-on:click="updateProfile()">
      Update Profile
    </a-button>
    <a-button type="primary" v-on:click="updateEmail()">
      Update Email
    </a-button>
    <a-button type="primary" v-on:click="setPassword()">
      Set Password
    </a-button>
    <a-button type="primary" v-on:click="resetPassword()">
      Reset Password
    </a-button>
    <a-button type="primary" v-on:click="fetchApi()">
      Fetch Api
    </a-button> -->
  </a-layout>
</template>

<script>
import firebase from "firebase";
import axios from "axios";
import Profile from "@/components/Profile.vue";
import Card from "@/components/Card.vue";

export default {
  name: "User",
  components: {
    Profile,
    Card
  },
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

<style scoped>
.container {
  margin-top: 64px;
  display: flex;
  justify-content: center;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .container {
    flex-direction: column-reverse;
  }
}
</style>
