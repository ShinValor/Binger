<template>
  <a-form-model
    class="container"
    :model="form"
    :label-col="labelCol"
    :wrapper-col="wrapperCol"
  >
    <a-form-model-item label="Nick Name">
      <a-input v-model="form.name" />
    </a-form-model-item>
    <!-- <a-form-model-item label="Send Email">
      <a-switch v-model="form.email" />
    </a-form-model-item> -->
    <a-form-model-item label="Introduction">
      <a-input v-model="form.description" type="textarea" />
    </a-form-model-item>
    <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
      <a-button
        class="update-btn"
        @click="onUpdate(form.name, form.description)"
      >
        Update
      </a-button>
      <a-button class="cancel-btn">
        <router-link :to="{ name: 'Home' }">
          Cancel
        </router-link>
      </a-button>
    </a-form-model-item>
  </a-form-model>
</template>

<script>
export default {
  name: "UserSetting",
  props: {
    username: String,
    description: String
  },
  data() {
    return {
      labelCol: { span: 4 },
      wrapperCol: { span: 14 },
      form: {
        name: this.username,
        description: this.description
        // email: false,
      }
    };
  },
  methods: {
    onUpdate(name, description) {
      this.$store.dispatch("updateProfile", { name, description });
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.update-btn,
.cancel-btn {
  margin-left: 20px;
  background-color: transparent;
  border-color: #f3c669;
  color: white;
}

.update-btn:hover,
.cancel-btn:hover {
  background-color: #f3c669;
}
</style>
