<template>
  <a-form-model
    class="setting"
    :model="form"
    :label-col="labelCol"
    :wrapper-col="wrapperCol"
  >
    <a-form-model-item label="Nick Name">
      <a-input v-model="form.name" />
      <!-- <a-input v-model="username" /> -->
    </a-form-model-item>
    <!-- <a-form-model-item label="Send Email">
      <a-switch v-model="form.email" />
    </a-form-model-item> -->
    <a-form-model-item label="Introduction">
      <a-input v-model="form.description" type="textarea" />
      <!-- <a-input v-model="description" type="textarea" /> -->
    </a-form-model-item>
    <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
      <a-button
        class="update-btn"
        @click="onUpdate(form.name, form.description)"
      >
        Update
      </a-button>
      <a-button class="cancel-btn" style="margin-left: 10px;">
        <router-link :to="{ name: 'Home' }">
          Cancel
        </router-link>
      </a-button>
    </a-form-model-item>
  </a-form-model>
</template>

<script>
export default {
  name: "Setting",
  data() {
    return {
      labelCol: { span: 4 },
      wrapperCol: { span: 14 },
      form: {
        name: "",
        email: false,
        description: ""
      }
    };
  },
  methods: {
    onUpdate(name, description) {
      this.$store.dispatch("updateProfile", { name, description });
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
.setting {
  width: 700px;
  margin: 50px 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.update-btn,
.cancel-btn {
  background-color: transparent;
  color: white;
}

.update-btn:hover,
.cancel-btn:hover {
  border-color: white;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .setting {
    width: 250px;
    margin: 0 auto;
  }
}
</style>
