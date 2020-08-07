<template>
  <a-form-model>
    <div class="form">
      <h1 class="label">Name</h1>
      <a-input @input="changeName($event.target.value)" :value="username" />
    </div>
    <div class="form">
      <h1 class="label">Introduction</h1>
      <a-input
        class="introduction-input"
        @input="changeDesc($event.target.value)"
        :value="description"
        type="textarea"
      />
    </div>
    <div class="form-btn">
      <a-button class="update-btn" @click="onUpdate()">
        Update
      </a-button>
      <a-button class="cancel-btn">
        <router-link :to="{ name: 'Home' }">
          Cancel
        </router-link>
      </a-button>
    </div>
    <div class="form-btn2">
      <div>
        <h1 class="label">Purge Movie Data</h1>
        <a-button class="delete-btn" @click="onDelete">
          Delete
        </a-button>
      </div>
    </div>
  </a-form-model>
</template>

<script>
export default {
  name: "UserSetting",
  data() {
    return {
      name: "",
      desc: ""
    };
  },
  methods: {
    changeName(change) {
      this.name = change;
    },
    changeDesc(change) {
      this.desc = change;
    },
    onUpdate() {
      this.$store.dispatch("updateProfile", {
        name: this.name,
        description: this.desc
      });
    },
    onDelete() {
      this.$confirm({
        title: "Do you want to delete all movie data?",
        onOk: () => {
          this.$store.dispatch("deleteData", this.$store.state.uid);
          this.$message.success("You have deleted your movie data");
        }
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
.form {
  margin-top: 50px;
}

.label {
  text-align: left;
  color: white;
}

.introduction-input {
  height: 100px;
}

.form-btn {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.form-btn2 {
  margin-top: 50px;
  display: flex;
  justify-content: center;
}

.update-btn,
.cancel-btn {
  margin: 0 20px;
  background-color: transparent;
  border-color: #f3c669;
  color: white;
}

.delete-btn {
  background-color: transparent;
  border-color: #f3c669;
  color: white;
}

.update-btn:hover,
.cancel-btn:hover {
  background-color: #f3c669;
}

.delete-btn:hover {
  border-color: #ff9299 !important;
  background-color: #ff9299 !important;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .form {
    margin-top: 20px;
  }

  .label {
    font-size: 15px;
  }

  .form-btn {
    justify-content: space-evenly;
  }

  .form-btn2 {
    margin-top: 30px;
  }

  .update-btn,
  .cancel-btn {
    margin: 0;
  }
}
</style>
