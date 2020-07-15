<template>
  <a-form class="signup-form" :form="form" @submit="handleSubmit">
    <h1 :style="{ color: 'white' }">Register Here !</h1>
    <a-form-item>
      <a-input
        v-decorator="[
          'nickname',
          {
            rules: [
              { required: true, message: 'Please input your display name!' }
            ]
          }
        ]"
        placeholder="Nickname"
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
      <a-button type="primary" html-type="submit" :style="{ width: '100%' }">
        Register
      </a-button>
    </a-form-item>
  </a-form>
</template>

<script>
import firebase from "firebase";

export default {
  name: "SignupForm",
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "register" });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err && values.password == values.confirmPassword) {
          if (values.password == values.confirmPassword) {
            firebase
              .auth()
              .createUserWithEmailAndPassword(values.email, values.password)
              .then(data => {
                data.user
                  .updateProfile({
                    displayName: values.nickname
                  })
                  .then(() => {
                    this.$router.replace({ name: "Login" });
                  });
              })
              .catch(err => {
                this.error = err.message;
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
.signup-form {
  width: 500px;
  margin: 100px auto 0;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .signup-form {
    width: 250px;
  }
}
</style>
