<template>
  <a-form-model
    class="setting"
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
      <a-input v-model="form.desc" type="textarea" />
    </a-form-model-item>
    <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
      <a-button type="primary" @click="onSubmit">
        Update
      </a-button>
      <a-button style="margin-left: 10px;">
        Cancel
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
        desc: ""
      }
    };
  },
  methods: {
    onSubmit() {
      // On Submit
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

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .setting {
    width: 250px;
    margin: 0 auto;
  }
}
</style>
