<template>
  <div class="container">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/list">My fridges</router-link> |
      <router-link to="/register">Register</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/logout">Logout</router-link>

     <span v-if="userStore.user.isAuthenticated">
       Logged in as: {{ userStore.user.email }}
      </span>
      
    </nav>
    <div class="content">
      <router-view />
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
  beforeCreate() {
    this.userStore.initStore();
    const token = this.userStore.user.access;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>

<style>
.content {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}
</style>
