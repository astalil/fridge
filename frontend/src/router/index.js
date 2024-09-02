import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";
import FridgeItems from "../views/FridgeItems.vue";
import InvitationListView from "../views/InvitationListView.vue";
import SettingsView from "../views/SettingsView.vue";

import { useUserStore } from "@/store/user";
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/list",
    name: "list",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/FridgeList.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/fridge/:id",
    name: "fridge-items",
    component: FridgeItems,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/logout",
    name: "logout",
    meta: {
      requiresAuth: true,
    },
    beforeEnter: (to, from, next) => {
      const store = useUserStore();
      store.removeToken();
      next("/login");
    },
  },
  {
    path: "/invites",
    name: "invites",
    component: InvitationListView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/settings",
    name: "settings",
    component: SettingsView,
    meta: {
      requiresAuth: true,
    }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const store = useUserStore();
  if (to.meta.requiresAuth) {
    console.log("In if 1");
    if (store.user.isAuthenticated) {
      console.log("In if 2");
      next();
    } else {
      console.log("In if 3");
      next("/login");
    }
  } else if (
    (store.user.isAuthenticated && to.name === "login") ||
    (store.user.isAuthenticated && to.name === "register")
  ) {
    console.log("In else if");
    next("/");
  } else {
    console.log("In else");
    next();
  }
});

export default router;
