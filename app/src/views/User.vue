<template>
  <a-layout :style="{ minHeight: '100%', overflow: 'auto' }">
    <div class="container">
      <UserSetting />
      <Card class="profile-card" :name="username" :desc="description" />
    </div>
    <div>
      <div
        :style="{
          'background-color': 'white',
          height: '350px',
          width: '350px',
          margin: '25px auto',
          display: 'flex',
          'justify-content': 'center',
          'align-items': 'center'
        }"
      >
        <img class="preview" height="300" width="300" :src="userImage" />
      </div>
      <div :style="{ margin: '25px' }">
        <input
          type="file"
          ref="imageInput"
          :style="{ display: 'none' }"
          @change="previewImage"
          accept="image/*"
        />
        <a-button @click="onClick">Upload Picture</a-button>
      </div>
    </div>
  </a-layout>
</template>

<script>
// import firebase from "firebase";
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
      // name: "Username",
      // caption: "",
      // imageUrl: "",
      imageData: null
    };
  },
  methods: {
    onClick() {
      this.$refs.imageInput.click();
    },
    previewImage(event) {
      // console.log("EVENT", event);
      // this.uploadValue = 0;
      this.imageData = event.target.files[0];
      this.uploadImage();
    },
    uploadImage() {
      this.$store.dispatch("updateProfileImage", this.imageData);

      // this.imageUrl = null;
      // const storageRef = firebase
      //   .storage()
      //   // .ref(`${this.imageData.name}`)
      //   .ref(firebase.auth().currentUser.uid)
      //   .put(this.imageData);

      // storageRef.on(
      //   "state_changed",
      //   snapshot => {
      //     this.uploadValue =
      //       (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
      //   },
      //   err => {
      //     this.error = err;
      //     // console.log(err.message);
      //   },
      //   () => {
      //     this.uploadValue = 100;
      //     storageRef.snapshot.ref.getDownloadURL().then(url => {
      //       this.imageUrl = url;
      //       console.log(this.imageUrl);
      //     });
      //   }
      // );
    }
    // profile() {
    //   const user = firebase.auth().currentUser;
    //   if (user != null) {
    //     // const name = user.displayName;
    //     // const email = user.email;
    //     // const photoUrl = user.photoURL;
    //     // const emailVerified = user.emailVerified;
    //     // const uid = user.uid;
    //   }
    // },
    // updateProfile() {
    //   const user = firebase.auth().currentUser;
    //   user
    //     .updateProfile({
    //       displayName: "Jane Q. User",
    //       photoURL: "https://example.com/jane-q-user/profile.jpg"
    //     })
    //     .catch(error => {
    //       this.error = error.message;
    //     });
    // },
    // updateEmail() {
    //   const user = firebase.auth().currentUser;

    //   user.updateEmail("user@example.com").catch(error => {
    //     this.error = error.message;
    //   });
    // },
    // setPassword() {
    //   const user = firebase.auth().currentUser;
    //   const newPassword = "onetwothreefourfivesix";

    //   user.updatePassword(newPassword).catch(error => {
    //     this.error = error.message;
    //   });
    // },
    // resetPassword() {
    //   const user = firebase.auth().currentUser;
    //   const emailAddress = user.email;
    //   const auth = firebase.auth();

    //   auth.sendPasswordResetEmail(emailAddress).catch(error => {
    //     this.error = error.message;
    //   });
    // }
  },
  computed: {
    username() {
      return this.$store.state.userProfile["name"];
    },
    userImage() {
      if (this.$store.state.userImage) {
        return this.$store.state.userImage;
      } else {
        return "../assets/svg/profile-pic.svg";
      }
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
