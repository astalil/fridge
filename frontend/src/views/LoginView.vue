<template>
  <div>
    <h1>Sign In</h1>
    <div class="auth-errors-div">
      <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
    </div>
    <div class="input-div">
      <FloatLabel>
        <InputText type="email" id="email" v-model="form.email" />
        <label for="email">Email</label>
      </FloatLabel>
    </div>
    <div class="input-div">
      <FloatLabel>
        <Password v-model="form.password" inputId="password" />
        <label for="password">Password</label>
      </FloatLabel>
    </div>
    <div>
      <a href="login">Forgot your password?</a>
    </div>
    <div>
      <Button @click="submit" severity="success" label="Login" />
    </div>
    <div>
      <p>Don't have an account yet? <a href="register">Sign Up</a></p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useUserStore } from "@/store/user";

export default {
  setup() {
    const userStore = useUserStore();
    return {
      userStore,
    };
  },

  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errors: [],
    };
  },
  methods: {
    async submit() {
      this.errors = [];
      if (this.form.email === "") {
        this.errors.push("Email field can not be empty");
      }
      if (this.form.password === "") {
        this.errors.push("Password field can not be empty");
      }
      if (this.errors.length === 0) {
        await axios
          .post("/login/", this.form)
          .then((response) => {
            this.userStore.setToken(response.data);
            axios.defaults.headers.common["Authorization"] =
              "Bearer " + response.data.access;

            console.log("This is reponse: ", response.data);
          })
          .catch((error) => {
            this.errors.push(error.response.data.detail);
            console.log("This is the error: ", error);
          });

        await axios
          .get("/user-data/")
          .then((response) => {
            console.log("this is login response: ", response.data);
            this.userStore.setUserInfo(
              response.data.user,
              response.data.fridges
            );

            this.$router.push("/");
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
</style>
