<template>
  <div class="register-div">
    <div class="inside-register-div">
    
      <h1>Create a New Account</h1>
      <div class="errors-div">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
      <div class="input-div">
        <FloatLabel>
          <InputText id="first_name" v-model="form.first_name" />
          <label for="first_name">First name</label>
        </FloatLabel>
      </div>
      <div class="input-div">
        <FloatLabel>
          <InputText id="last_name" v-model="form.last_name" />
          <label for="last_name">Last name</label>
        </FloatLabel>
      </div>
      <div class="input-div">
        <FloatLabel>
          <InputText type="email" id="email" v-model="form.email" />
          <label for="email">Email</label>
        </FloatLabel>
      </div>
      <div class="input-div">
        <FloatLabel>
          <Password v-model="form.password1" inputId="password" />
          <label for="password">Password</label>
        </FloatLabel>
      </div>
      <div class="input-div">
        <FloatLabel>
          <Password v-model="form.password2" inputId="password2" />
          <label for="password2">Repeat password</label>
        </FloatLabel>
      </div>
      <div>
        <Button @click="submit" severity="success" label="Register" />
      </div>

      <div>
        <p>Already have an account? <a href="login">Sign In</a></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        first_name: "",
        last_name: "",
        email: "",
        password1: "",
        password2: "",
      },
      errors: [],
    };
  },
  methods: {
    submit() {
      this.errors = [];
      console.log(this.form);
      if (this.form.first_name === "") {
        this.errors.push("Enter first name");
      }
      if (this.form.last_name === "") {
        this.errors.push("Enter last name");
      }
      if (this.form.email === "") {
        this.errors.push("Enter email");
      }
      if (this.form.password1 === "") {
        this.errors.push("Enter password");
      }
      if (this.form.password2 === "") {
        this.errors.push("Repeat the password");
      }
      if (this.form.password2 !== this.form.password1) {
        this.errors.push("Passwords do not match");
      }
      if (this.errors.length === 0) {
        axios
          .post("/register/", this.form)
          .then((response) => {
            if (response.data.status === "error") {
              this.errors = response.data.errors;
            } else {
              this.$router.push("/login");
            }
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style>
.input-div {
  margin-bottom: 35px;
}

.errors-div {
  margin-bottom: 5vh;
}
</style>
