<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div class="container">
      <UserSetting />
      <Card class="profile-card" :name="username" :desc="description" />
    </div>
  </a-layout>
</template>

<script>
import firebase from "firebase";
import UserSetting from "@/components/UserSetting.vue";
import Card from "@/components/Card.vue";

export default {
  name: "User",
  components: {
    UserSetting,
    Card
  },
  data() {
    return {
      // name: "Username"
    };
  },
  methods: {
    profile() {
      const user = firebase.auth().currentUser;
      if (user != null) {
        // const name = user.displayName;
        // const email = user.email;
        // const photoUrl = user.photoURL;
        // const emailVerified = user.emailVerified;
        // const uid = user.uid;
      }
    },
    updateProfile() {
      const user = firebase.auth().currentUser;
      user
        .updateProfile({
          displayName: "Jane Q. User",
          photoURL: "https://example.com/jane-q-user/profile.jpg"
        })
        .catch(error => {
          this.error = error.message;
        });
    },
    updateEmail() {
      const user = firebase.auth().currentUser;

      user.updateEmail("user@example.com").catch(error => {
        this.error = error.message;
      });
    },
    setPassword() {
      const user = firebase.auth().currentUser;
      const newPassword = "onetwothreefourfivesix";

      user.updatePassword(newPassword).catch(error => {
        this.error = error.message;
      });
    },
    resetPassword() {
      const user = firebase.auth().currentUser;
      const emailAddress = user.email;
      const auth = firebase.auth();

      auth.sendPasswordResetEmail(emailAddress).catch(error => {
        this.error = error.message;
      });
    }
  },
  computed: {
    username() {
      return this.$store.state.userProfile["name"];
    },
    description() {
      return this.$store.state.userProfile["description"];
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
  height: 500px;
  width: 450px;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .container {
    margin: 10px;
    flex-direction: column-reverse;
  }

  .profile-card {
    height: 400px;
    width: 300px;
  }
}
</style>
