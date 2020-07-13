<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div class="container">
      <Profile />
      <Card class="profile-card" name="John" desc="I am a student." />
    </div>
  </a-layout>
</template>

<script>
import firebase from "firebase";
import Profile from "@/components/Profile.vue";
import Card from "@/components/Card.vue";

export default {
  name: "User",
  components: {
    Profile,
    Card
  },
  methods: {
    getProfile() {
      const user = firebase.auth().currentUser;

      if (user != null) {
        // const name = user.displayName;
        // const email = user.email;
        // const photoUrl = user.photoURL;
        // const emailVerified = user.emailVerified;
        // const uid = user.uid;
        // console.log("Name: ", name);
        // console.log("Email: ", email);
        // console.log("Photo Url: ", photoUrl);
        // console.log("Email Verified: ", emailVerified);
        // console.log("Uid: ", uid);
      }
    },
    created() {
      firebase.auth().onAuthStateChanged(user => {
        if (!user) {
          this.$router.replace({ name: "Home" });
        }
      });
    },
    updateProfile() {
      const user = firebase.auth().currentUser;

      user
        .updateProfile({
          displayName: "Jane Q. User",
          photoURL: "https://example.com/jane-q-user/profile.jpg"
        })
        .then(() => {
          // alert("Updated Profile");
        })
        .catch(error => {
          this.error = error.message;
          // alert(this.error);
        });
    },
    updateEmail() {
      const user = firebase.auth().currentUser;

      user
        .updateEmail("user@example.com")
        .then(() => {
          // alert("Updated Email");
        })
        .catch(error => {
          this.error = error.message;
          // alert(this.error);
        });
    },
    setPassword() {
      const user = firebase.auth().currentUser;
      const newPassword = "onetwothreefourfivesix";

      user
        .updatePassword(newPassword)
        .then(() => {
          // alert("Updated Password");
        })
        .catch(error => {
          this.error = error.message;
          // alert(this.error);
        });
    },
    resetPassword() {
      const user = firebase.auth().currentUser;
      const emailAddress = user.email;
      const auth = firebase.auth();

      auth
        .sendPasswordResetEmail(emailAddress)
        .then(() => {
          // alert("Email Sent");
        })
        .catch(error => {
          this.error = error.message;
          // alert(this.error);
        });
    }
  }
};
</script>

<style scoped>
.container {
  margin: 64px;
  display: flex;
  justify-content: center;
}

.profile-card {
  height: 400px;
  width: 400px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .container {
    margin: 10px;
    flex-direction: column-reverse;
  }

  .profile-card {
    height: 300px;
    width: 300px;
  }
}
</style>
