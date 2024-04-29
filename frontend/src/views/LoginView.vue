<template>
  <div>
    <div v-if="errors.length > 0">
      {{ errors }}
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
      <Button @click="submit" severity="success" label="Login" />
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
      await axios
        .post("/login/", this.form)
        .then((response) => {
          this.userStore.setToken(response.data);
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);
        });

      await axios
        .get("/user-data/")
        .then((response) => {
          this.userStore.setUserInfo(response.data);
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.input-div {
  margin-bottom: 35px;
}
</style>
