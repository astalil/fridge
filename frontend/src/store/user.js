import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore({
  id: "user",

  state: () => ({
    user: {
      name: null,
      surname: null,
      email: null,
      access: null,
      refresh: null,
      isAuthenticated: false,
    },
    fridges: [],
    invites: []
  }),

  actions: {
    initStore() {
      if (localStorage.getItem("user.access")) {
        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");
        this.user.id = localStorage.getItem("user.id");
        this.user.name = localStorage.getItem("user.name");
        this.user.surname = localStorage.getItem("user.surname");
        this.user.email = localStorage.getItem("user.email");
        this.user.isAuthenticated = true;
        this.fridges =
          JSON.parse(
            localStorage.getItem("fridges") == ""
              ? "{}"
              : localStorage.getItem("fridges")
          ) || [];

        this.refreshToken();

        console.log("Type of fridges: ", typeof fridges);
        console.log("Initialized user:", this.user);
      }
    },
    setToken(data) {
      console.log("setToken", data);

      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;

      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);

      console.log("user.access: ", localStorage.getItem("user.access"));
    },

    removeToken() {
      console.log("removeToken");

      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = false;
      this.user.name = false;
      this.user.surname = false;
      this.user.email = false;

      this.fridges = [];

      localStorage.setItem("user.access", "");
      localStorage.setItem("user.refresh", "");
      localStorage.setItem("user.id", "");
      localStorage.setItem("user.name", "");
      localStorage.setItem("user.surname", "");
      localStorage.setItem("user.email", "");

      localStorage.setItem("fridges", "");
    },

    setUserInfo(user, fridges) {
      console.log("setUserInfo", user, fridges);

      this.user.id = user.id;
      this.user.name = user.name;
      this.user.surname = user.surname;
      this.user.email = user.email;

      this.fridges = fridges;

      localStorage.setItem("user.id", this.user.id);
      localStorage.setItem("user.name", this.user.name);
      localStorage.setItem("user.surname", this.user.surname);
      localStorage.setItem("user.email", this.user.email);

      localStorage.setItem("fridges", JSON.stringify(fridges));
      console.log("Type of fridges: ", typeof fridges);
      console.log("User", this.user);
    },

    refreshToken() {
      axios
        .post("/refresh/", {
          refresh: this.user.refresh,
        })
        .then((response) => {
          this.user.access = response.data.access;

          localStorage.setItem("user.access", response.data.access);

          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);

          this.removeToken();
        });
    },

    addItemToFridge(newItem, fridgeId) {
      // Make API call to add item to the fridge
      // console.log("thos should be the id: ", fridgeId, itemName, quantity, expiryDate)
      // const response = await axios
      // .post(`/fridge/${fridgeId}/add-item`, { name: itemName, quantity: quantity, expiry_date: expiryDate })

      // console.log("Adding item reposnse code:", response.status)
      // if (response.status !== 200) {
      //   throw new Error('Failed to add item to fridge');
      // }
      // // Retrieve the newly created item from the response
      // const newItem = response.data;
      // console.log("this is the response data for adding new item: ", response.data)
      // Update fridges array in the store with the updated data
      console.log("this is fridgeId in store: ", fridgeId);
      this.fridges = this.fridges.map((fridge) => {
        if (fridge.id === fridgeId) {
          return {
            ...fridge,
            items: [...fridge.items, newItem], // Add the newly created item to the fridge
          };
        }
        return fridge;
      });
      // Save fridges data to localStorage
      localStorage.setItem("fridges", JSON.stringify(this.fridges));
      console.log("Saved new item");
    },
    removeItemFromFridge(fridgeId, itemIds) {
      console.log("This is fridge id: ", fridgeId);
      console.log("These are items: ", itemIds);
      this.fridges = this.fridges.map((fridge) => {
        if (fridge.id === fridgeId) {
          const updatedItems = fridge.items.filter(
            (item) => !itemIds.includes(item.id)
          );

          return {
            ...fridge,
            items: updatedItems,
          };
        }
        return fridge;
      });
      localStorage.setItem("fridges", JSON.stringify(this.fridges));
      console.log("Removed the items in the store");
    },

    addFridge(fridge) {
      this.fridges.push(fridge);
      localStorage.setItem("fridges", JSON.stringify(this.fridges));
      console.log("Saved new fridge");
    },

    async fetchInvites() {
      if (this.user.isAuthenticated) {
        try {
          const response = await axios.get('/fridge/invitations');
          this.invites = response.data.invites;
        } catch (error) {
          console.error('Error fetching invitations:', error);
        }
      } else {
        this.invites = 0;
      }
    },

    removeInvitation(inviteId) {
      this.invites = this.invites.filter(invite => invite.id !== inviteId);
    }
  },

  getters: {
    getFridgeById: (state) => (fridgeId) => {
      return state.fridges.find((fridge) => fridge.id === fridgeId);
    },

    inviteCount: (state) => state.invites,
  },
});
