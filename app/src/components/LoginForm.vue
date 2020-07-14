<template>
  <a-form class="login-form" :form="form" @submit="handleSubmit">
    <h1 :style="{ color: 'white' }">Log In</h1>
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
      <a-checkbox
        :style="{ float: 'left', color: 'white' }"
        v-decorator="[
          'remember',
          {
            valuePropName: 'checked',
            initialValue: true
          }
        ]"
      >
        Remember Me
      </a-checkbox>
      <a :style="{ float: 'right' }" href="">
        Forgot password
      </a>
      <a-button type="primary" html-type="submit" :style="{ width: '100%' }">
        Log in
      </a-button>
      <router-link to="/signup">
        Register now!
      </router-link>
    </a-form-item>
  </a-form>
</template>

<script>
import firebase from "firebase";

export default {
  name: "LoginForm",
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "normal_login" });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          firebase
            .auth()
            .signInWithEmailAndPassword(values.email, values.password)
            .then(() => {
              this.$router.replace({ name: "User" });
              this.$message.success("Successfully Logged In");
            })
            .catch(err => {
              this.error = err.message;
              this.$message.warning(this.error);
            });
        }
      });
    }
  }
};
</script>

<style scoped>
.login-form {
  width: 500px;
  margin: 100px auto 0;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .login-form {
    width: 250px;
  }
}
</style>
