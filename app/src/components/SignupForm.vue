<template>
  <a-form :form="form" @submit="onSignup" @submit.prevent>
    <a-form-item>
      <a-input
        v-decorator="[
          'name',
          {
            rules: [
              { required: true, message: 'Please input your display name!' }
            ]
          }
        ]"
        placeholder="Name"
      >
        <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-input
        v-decorator="[
          'email',
          {
            rules: [{ required: true, message: 'Please input your email!' }]
          }
        ]"
        placeholder="Email"
      >
        <a-icon slot="prefix" type="mail" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-input
        v-decorator="[
          'password',
          {
            rules: [{ required: true, message: 'Please input your Password!' }]
          }
        ]"
        type="password"
        placeholder="Password"
      >
        <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-input
        v-decorator="[
          'confirmPassword',
          {
            rules: [
              { required: true, message: 'Please confirm your password!' }
            ]
          }
        ]"
        type="password"
        placeholder="Confirm Password"
      >
        <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-button class="signup-btn" html-type="submit">
        Register
      </a-button>
    </a-form-item>
  </a-form>
</template>

<script>
export default {
  name: "SignupForm",
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "register" });
  },
  methods: {
    onSignup() {
      this.form.validateFields((err, values) => {
        if (!err) {
          if (values.password == values.confirmPassword) {
            this.$store
              .dispatch("signup", {
                email: values.email,
                password: values.password,
                name: values.name
              })
              .then(() => {
                this.$message.success("Successfully Logged In");
              })
              .catch(err => {
                this.error = err.message;
                this.$message.warning(this.error);
              });
          } else {
            this.$message.warning("Please Enter Same Password");
          }
        }
      });
    }
  }
};
</script>

<style scoped>
.signup-btn {
  background-color: transparent;
  width: 100%;
  color: white;
  border-color: #f3c669;
}

.signup-btn:hover {
  background-color: #f3c669;
}
</style>
