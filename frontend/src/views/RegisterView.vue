<template>
  <div class="register-container">
    <h1>Create an Account</h1>
    <div class="auth-errors-div">
      <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
    </div>
    <div class="input-div">
      <InputText
        id="first_name"
        v-model="form.first_name"
        placeholder="First name"
      />
    </div>
    <div class="input-div">
      <InputText
        id="last_name"
        v-model="form.last_name"
        placeholder="Last name"
      />
    </div>
    <div class="input-div">
      <InputText
        type="email"
        id="email"
        v-model="form.email"
        placeholder="Email"
      />
    </div>
    <div class="input-div">
      <Password
        v-model="form.password1"
        inputId="password"
        placeholder="Password"
        toggleMask
      />
      <label for="password"></label>
    </div>
    <div class="input-div">
      <Password
        v-model="form.password2"
        inputId="password2"
        placeholder="Repeat password"
        toggleMask
      />
    </div>
    <div>
      <Button @click="submit" severity="success" label="Register" />
    </div>

    <div>
      <p>Already have an account? <a href="login">Sign In</a></p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useToast } from "primevue/usetoast";

export default {
  setup() {
    const toast = useToast();
    return {
      toast,
    };
  },

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

<style scoped>
.input-div {
  margin-bottom: 35px;
}

.register-container {
  border: 1px solid black;
  border-radius: 20px;
  padding-bottom: 20px;
  text-align: center;
}

#email,
#last_name,
#first_name {
  padding-right: 40px;
}
</style>
