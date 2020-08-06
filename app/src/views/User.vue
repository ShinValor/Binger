<template>
  <a-layout>
    <div class="container">
      <UserSetting class="setting" />
      <Card
        class="profile"
        :name="username"
        :desc="description"
        :img="avatarUrl"
      />
    </div>
    <div>
      <input
        type="file"
        ref="imageInput"
        :style="{ display: 'none' }"
        @change="previewImage"
        accept="image/*"
      />
      <a-button class="upload-btn" @click="onClick">
        Upload Picture
      </a-button>
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
  },
  computed: {
    username() {
      return this.$store.state.userProfile["name"];
    },
    avatarUrl() {
      return this.$store.state.userImage;
    },
    description() {
      return this.$store.state.userProfile["description"];
    }
  }
};
</script>

<style scoped>
.container {
  margin: 50px 0 25px;
  display: flex;
  justify-content: space-evenly;
}

.profile {
  height: 500px;
  width: 450px;
}

.setting {
  width: 500px;
  margin: 0;
}

.upload-btn {
  width: 200px;
  margin-right: 275px;
  float: right;
  background-color: transparent;
  border-color: #f3c669;
  color: white;
}

.upload-btn:hover {
  background-color: #f3c669;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .container {
    margin: 10px;
    flex-direction: column-reverse;
  }

  .profile {
    height: 400px;
    width: 300px;
  }

  .setting {
    width: 300px;
    margin: 0 auto;
  }

  .upload-btn {
    margin: 30px 75px 30px;
  }
}
</style>
