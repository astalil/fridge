<template>
  <div class="invites-div">
    <Toast />
    <h1>Currently you have {{ inviteCount.length }} invites!</h1>

    <div v-if="inviteCount.length > 0">
      <ul>
        <li style="margin-bottom: 10px" v-for="invite in inviteCount" :key="invite">
          <b>
            {{ invite.sender_name }} {{ invite.sender_surname }} ({{invite.fridge_name}})
          </b>
          sent you a fridge request.
          <Button
            icon="pi pi-plus"
            label="Accept"
            size="small"
            severity="success"
            @click="handleInvite(invite.id, 'accept')"
          />
          <Button
            icon="pi pi-times"
            severity="danger"
            label="Decline"
            size="small"
            @click="handleInvite(invite.id, 'decline')"
          />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useToast } from "primevue/usetoast";
import { useUserStore } from "@/store/user";

export default {
  setup() {
    const userStore = useUserStore();
    const toast = useToast();
    return {
      userStore,
      toast
    };
  },

  data() {
    return {
      errors: [],
    };
  },
  
  computed: {
    inviteCount() {
      return this.userStore.inviteCount;
    },
  },

  methods: {
    // getInvites() {
    //   axios
    //     .get("/fridge/invitations")
    //     .then((response) => {
    //       this.invites = response.data.invites;
    //       console.log("these are the invites: ", response.data.invites);
    //       console.log(typeof this.invites);
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },

    handleInvite(inviteId, action) {
      axios
        .post("/fridge/invite-action", { invite_id: inviteId, action: action })
        .then((response) => {
          console.log("response data: ", response.data);
          if (response.data.message === "error") {
            this.errors = response.data.error;
          } else if (
            response.data.message === "success" &&
            action === "accept"
          ) {
            this.userStore.addFridge(response.data.fridge);
            this.toast.add({
              severity: "success",
              summary: "New fridge added",
              detail: "Successfully joined a new fridge",
              life: 3000,
            });
          }

          if (response.data.message === "success") {
            this.userStore.removeInvitation(inviteId)
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
