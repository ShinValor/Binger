<template>
  <a-form-model
    class="profile"
    :model="form"
    :label-col="labelCol"
    :wrapper-col="wrapperCol"
  >
    <a-form-model-item label="Nick Name">
      <a-input v-model="form.name" />
    </a-form-model-item>
    <a-form-model-item label="Time zone">
      <a-select
        v-model="form.region"
        placeholder="please select your time zone"
      >
        <a-select-option value="est">
          Eastern
        </a-select-option>
        <a-select-option value="ct">
          Central
        </a-select-option>
        <a-select-option value="pst">
          Pacific
        </a-select-option>
      </a-select>
    </a-form-model-item>
    <a-form-model-item label="Birth Date">
      <a-date-picker
        v-model="form.date1"
        show-time
        type="date"
        placeholder="Pick a date"
        style="width: 100%;"
      />
    </a-form-model-item>
    <a-form-model-item label="Email Opt In/Out">
      <a-switch v-model="form.delivery" />
    </a-form-model-item>
    <a-form-model-item label="Movie type">
      <a-checkbox-group v-model="form.type">
        <a-checkbox value="1" name="type">
          Action
        </a-checkbox>
        <a-checkbox value="2" name="type">
          Comedy
        </a-checkbox>
        <a-checkbox value="3" name="type">
          Horror
        </a-checkbox>
      </a-checkbox-group>
    </a-form-model-item>
    <a-form-model-item label="Gender">
      <a-radio-group v-model="form.resource">
        <a-radio value="1">
          Male
        </a-radio>
        <a-radio value="2">
          Female
        </a-radio>
      </a-radio-group>
    </a-form-model-item>
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
  name: "Profile",
  data() {
    return {
      labelCol: { span: 4 },
      wrapperCol: { span: 14 },
      form: {
        name: "",
        region: undefined,
        date1: undefined,
        delivery: false,
        type: [],
        resource: "",
        desc: ""
      }
    };
  },
  methods: {
    onSubmit() {
      console.log("submit!", this.form);
    }
  }
};
</script>

<style scoped>
.profile {
  width: 700px;
  margin: 50px 20px !important;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .profile {
    width: 250px;
    margin: 0 auto !important;
  }
}
</style>
