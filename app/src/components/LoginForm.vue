<template>
  <a-form
    class="login-form"
    :form="form"
    @submit="handleSubmit"
    @submit.prevent
  >
    <!-- <h1 :style="{ color: 'white' }">Log In</h1> -->
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
        class="remember-btn"
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
      <router-link class="forget-btn" to="/signup">
        Forgot password
      </router-link>
      <a-button class="login-btn" html-type="submit">
        Log in
      </a-button>
      <router-link class="register-btn" to="/signup">
        Register now!
      </router-link>
    </a-form-item>
  </a-form>
</template>

<script>
// import firebase from "firebase";

export default {
  name: "LoginForm",
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "normal_login" });
  },
  methods: {
    handleSubmit() {
      // e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          // firebase
          //   .auth()
          //   .signInWithEmailAndPassword(values.email, values.password)
          //   .then(() => {
          //     this.$router.push({ name: "Home" });
          //     this.$message.success("Successfully Logged In");
          //   })
          //   .catch(err => {
          //     this.error = err.message;
          //     this.$message.warning(this.error);
          //   });
          this.$store
            .dispatch("login", {
              email: values.email,
              password: values.password
            })
            .then(() => {
              // this.$router.push({ name: "Home" });
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

.remember-btn {
  float: left;
}

.forget-btn {
  float: right;
  color: white;
}

.forget-btn:hover {
  color: #f3c669;
}

.register-btn {
  color: white;
}

.register-btn:hover {
  color: #f3c669;
}

.login-btn {
  background-color: transparent;
  width: 100%;
  color: white;
  border-color: #f3c669;
}

.login-btn:hover {
  background-color: #f3c669;
}

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  .login-form {
    width: 250px;
  }
}
</style>
