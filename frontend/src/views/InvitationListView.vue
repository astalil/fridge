<template>
    <div class="invites-div">
        <Toast />
        <h1>Currently you have {{ invites.length }} invites!</h1>

        <div v-if="invites.length > 0">
            <ul>
                <li style="margin-bottom: 10px;" v-for="invite in invites" :key="invite"><b>{{ invite.sender_name }} {{ invite.sender_surname }} ({{ invite.fridge_name }})</b> sent you a fridge request. <Button icon="pi pi-plus" label="Accept" size="small" severity="success" @click="handleInvite(invite.id, 'accept')" /> <Button icon="pi pi-times" severity="danger" label="Decline" size="small" @click="handleInvite(invite.id, 'decline')" /></li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { useToast } from "primevue/usetoast";
import { useUserStore } from "@/store/user";

export default {
    setup(){
        const store = useUserStore()
        const toast = useToast();
        return {
            store,
            toast
        }
    },

    data() {
        return {
            invites: [],
            errors: []
        }
    },
    created() {
        this.getInvites()
    },

    methods: {
        getInvites() {
            axios
            .get("/fridge/invitations")
            .then( (response) => {
                this.invites = response.data.invites
                console.log("these are the invites: ", response.data.invites)
                console.log(typeof this.invites)
            })
            .catch((error) => {
                console.log(error)
            })
        },

        handleInvite(inviteId, action){
          
            axios
            .post("/fridge/invite-action", {invite_id: inviteId, action:action})
            .then( (response) => {
                console.log("response data: ", response.data)
                if (response.data.message === 'error'){
                    this.errors = response.data.error
                }
                else if (response.data.message==='success' && action === 'accept') {
                    this.store.addFridge(response.data.fridge)
                    this.toast.add({ severity: 'success', summary: 'New fridge added', detail: 'Successfully joined a new fridge', life: 3000 });
                }

                if (response.data.message === 'success') {
                    this.invites = this.invites.filter( invite => {
                        return invite.id !== inviteId
                    });
                }
                
            })
            .catch((error) => {
                console.log(error)
            })
        }
    }
}
</script>