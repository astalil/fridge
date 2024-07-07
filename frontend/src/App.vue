<template>
  <div class="container">
    <nav>
      <span>FreshAlert</span>
      <Sidebar v-model:visible="visible">
        <template #container="{ closeCallback }">
          <div class="flex flex-column h-full">
            <div
              class="flex align-items-center justify-content-between px-4 pt-3 flex-shrink-0"
            >
              <span class="inline-flex align-items-center gap-2">
                <svg
                  width="35"
                  height="40"
                  viewBox="0 0 35 40"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M25.87 18.05L23.16 17.45L25.27 20.46V29.78L32.49 23.76V13.53L29.18 14.73L25.87 18.04V18.05ZM25.27 35.49L29.18 31.58V27.67L25.27 30.98V35.49ZM20.16 17.14H20.03H20.17H20.16ZM30.1 5.19L34.89 4.81L33.08 12.33L24.1 15.67L30.08 5.2L30.1 5.19ZM5.72 14.74L2.41 13.54V23.77L9.63 29.79V20.47L11.74 17.46L9.03 18.06L5.72 14.75V14.74ZM9.63 30.98L5.72 27.67V31.58L9.63 35.49V30.98ZM4.8 5.2L10.78 15.67L1.81 12.33L0 4.81L4.79 5.19L4.8 5.2ZM24.37 21.05V34.59L22.56 37.29L20.46 39.4H14.44L12.34 37.29L10.53 34.59V21.05L12.42 18.23L17.45 26.8L22.48 18.23L24.37 21.05ZM22.85 0L22.57 0.69L17.45 13.08L12.33 0.69L12.05 0H22.85Z"
                    fill="var(--primary-color)"
                  />
                  <path
                    d="M30.69 4.21L24.37 4.81L22.57 0.69L22.86 0H26.48L30.69 4.21ZM23.75 5.67L22.66 3.08L18.05 14.24V17.14H19.7H20.03H20.16H20.2L24.1 15.7L30.11 5.19L23.75 5.67ZM4.21002 4.21L10.53 4.81L12.33 0.69L12.05 0H8.43002L4.22002 4.21H4.21002ZM21.9 17.4L20.6 18.2H14.3L13 17.4L12.4 18.2L12.42 18.23L17.45 26.8L22.48 18.23L22.5 18.2L21.9 17.4ZM4.79002 5.19L10.8 15.7L14.7 17.14H14.74H15.2H16.85V14.24L12.24 3.09L11.15 5.68L4.79002 5.2V5.19Z"
                    fill="var(--text-color)"
                  />
                </svg>
                <span class="font-semibold text-2xl text-primary"
                  >FreshAlert</span
                >
              </span>
              <span>
                <Button
                  type="button"
                  @click="closeCallback"
                  icon="pi pi-times"
                  rounded
                  outlined
                  class="h-2rem w-2rem"
                ></Button>
              </span>
            </div>
            <div class="overflow-y-auto">
              <ul class="list-none p-3 m-0">
                <li>
                  <router-link
                    to="/"
                    v-ripple
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple"
                  >
                    <i class="pi pi-home mr-2"></i>
                    <span class="font-medium">Home</span>
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/list"
                    v-ripple
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple"
                  >
                    <i class="pi pi-users mr-2"></i>
                    <span class="font-medium">Fridges list</span>
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/invites"
                    v-ripple
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple"
                  >
                    <i class="pi pi-comments mr-2"></i>
                    <span class="font-medium">Invitations</span>
                    <span
                      class="inline-flex align-items-center justify-content-center ml-auto bg-primary border-circle"
                      style="min-width: 1.5rem; height: 1.5rem"
                      >3</span
                    >
                  </router-link>
                </li>
                <li>
                  <router-link
                    v-ripple
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple"
                  >
                    <i class="pi pi-cog mr-2"></i>
                    <span class="font-medium">Settings</span>
                  </router-link>
                </li>
              </ul>
            </div>
            <div class="mt-auto">
              <div v-if="userStore.user.isAuthenticated">
                <router-link
                  v-ripple
                  to="/logout"
                  class="m-3 flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple"
                >
                  <i class="pi pi-sign-out mr-2"></i>
                  <span class="font-medium">Logout</span>
                </router-link>
              </div>
              <hr class="mb-3 mx-3 border-top-1 border-none surface-border" />
              <div v-if="userStore.user.isAuthenticated">
                <router-link
                  v-ripple
                  class="m-3 flex align-items-center cursor-pointer p-3 gap-2 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple"
                >
                  <Avatar
                    image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png"
                    shape="circle"
                  />
                  <span class="font-bold"
                    >{{ userStore.user.name }}
                    {{ userStore.user.surname }}</span
                  >
                </router-link>
              </div>
              <div v-else>
                <router-link
                  to="/login"
                  v-ripple
                  class="m-3 flex align-items-center cursor-pointer p-3 gap-2 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple"
                >
                  Sign In
                </router-link>
              </div>
            </div>
          </div>
        </template>
      </Sidebar>
      <Button icon="pi pi-bars" id="navbar-burger" @click="visible = true" />
    </nav>

    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/list">My fridges</router-link> |
      <router-link to="/register">Register</router-link> |
      <router-link to="/login">Login</router-link>|
      <router-link to="/logout">Logout</router-link>

     <span v-if="userStore.user.isAuthenticated">
       Logged in as: {{ userStore.user.email }}
      </span>
    </nav> -->

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
  data() {
    return {
      visible: false,
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
  min-height: 90vh;
  margin-top: 10vh;
}
</style>
