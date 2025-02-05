<template>
  <div>
    <div class="items-header">
      <h1 class="page-header">
        {{ fridge.name }}
        <Button
          icon="pi pi-plus"
          aria-label="Save"
          style="font-size: 10px"
          @click="showInvitePopUp = true"
        />
      </h1>
      <ConfirmPopup></ConfirmPopup>
      <div class="items-view-buttons">
        <Button
          label="ADD"
          style="margin-right: 10px"
          @click="showAddPopUp = true"
        />
        <Button
          label="REMOVE"
          :disabled="selectedItems.length === 0"
          @click="removeItems"
        />
      </div>
      <ConfirmDialog></ConfirmDialog>
    </div>

    <div v-if="errors.length > 0">
      {{ errors }}
    </div>

    <div>
      <OrderList v-model="fridge.items" listStyle="height:auto" dataKey="id">
        <template #header> List of Items </template>
        <template #item="slotProps">
          <div
            class="flex flex-wrap p-2 align-items-center gap-3 item-div"
            @click="addToList(slotProps.item.id)"
          >
            <div class="flex-1 flex flex-column gap-2">
              <span class="font-bold"
                >{{ slotProps.item.name }} x {{ slotProps.item.quantity }}</span
              >
              <div class="flex align-items-center gap-2">
                <i class="pi pi-calendar text-sm"></i>
                <span>{{ slotProps.item.expiry_date }}</span>
              </div>
            </div>
          </div>
        </template>
      </OrderList>
    </div>

    <div>
      <Dialog
        v-model:visible="showAddPopUp"
        modal
        header="Add Item"
        :style="{ width: '25rem' }"
      >
        <span class="p-text-secondary block mb-6">Add new item</span>
        <div v-if="fridge_error.length > 0">
          {{ fridge_error }}
        </div>
        <div class="flex align-items-center gap-3 mb-5">
          <FloatLabel>
            <InputText id="first_name" v-model="name" />
            <label for="first_name">Name</label>
          </FloatLabel>
        </div>
        <div class="flex align-items-center gap-3 mb-5">
          <FloatLabel>
            <InputText id="quantity" v-model="quantity" />
            <label for="quantity">Quantity</label>
          </FloatLabel>
        </div>
        <div class="flex align-items-center gap-3 mb-5">
          <FloatLabel>
            <Calendar
              v-model="expiryDate"
              dateFormat="yy/mm/dd"
              inputId="expiry_date"
            />
            <label for="expiry_date">Expiry date</label>
          </FloatLabel>
        </div>

        <div class="flex justify-content-end gap-2">
          <Button
            type="button"
            label="Cancel"
            severity="secondary"
            @click="showAddPopUp = false"
          ></Button>
          <Button type="button" label="Add" @click="addNewItem"></Button>
        </div>
      </Dialog>

      <Dialog
        v-model:visible="showInvitePopUp"
        modal
        header="Edit Profile"
        :style="{ width: '25rem' }"
      >
        <span class="p-text-secondary block mb-5">Add people</span>

        <div class="flex align-items-center gap-3 mb-3">
          <label for="email" class="font-semibold w-6rem">Email</label>
          <InputText
            id="email"
            class="flex-auto"
            v-model="email"
            autocomplete="off"
          />
        </div>

        <div class="flex justify-content-end gap-2">
          <Button
            type="button"
            label="Cancel"
            severity="secondary"
            @click="showInvitePopUp = false"
          ></Button>
          <Button type="button" label="Add" @click="invitePeople"></Button>
        </div>
      </Dialog>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { useUserStore } from "@/store/user";
import { useConfirm } from "primevue/useconfirm";
import { useRoute } from "vue-router";
import axios from "axios";

export default {
  setup() {
    const store = useUserStore();
    const router = useRoute();

    let fridge = store.getFridgeById(parseInt(router.params.id));
    const confirm = useConfirm();
    return {
      store,
      fridge,
      confirm,
    };
  },

  data() {
    return {
      showAddPopUp: false,
      showInvitePopUp: false,
      expiryDate: null,
      quantity: null,
      name: null,
      email: null,
      selectedItems: [],
      errors: [],
      items: [],
      fridge_error: [],
    };
  },
  created() {
    this.retrieveItems();
  },

  methods: {
    retrieveItems() {
      axios
        .get(`/fridge/get-items/${this.fridge.id}`)
        .then((response) => {
          this.items = response.data.items;
          console.log("items:", response.data.items);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async addNewItem() {
      this.fridge_error = [];
      console.log(
        "these are the form values: ",
        this.name,
        this.quantity,
        this.expiryDate
      );
      console.log("This the ID: ", this.fridge.id);

      axios
        .post(`/fridge/${this.fridge.id}/add-item`, {
          name: this.name,
          quantity: this.quantity,
          expiry_date: this.expiryDate,
        })
        .then((response) => {
          console.log("Adding item reposnse code:", response.status);
          if (response.data.errors) {
            this.fridge_error.push(response.data.errors);
          } else {
            const newItem = response.data.item;
            console.log("newitem", newItem);

            this.store.addItemToFridge(newItem, newItem.fridge);
            this.showAddPopUp = false;
            location.reload();
          }
        })
        .catch((error) => {
          console.log("Error", error);
        });
    },

    invitePeople() {
      this.errors = [];
      axios
        .post("/fridge/invite-people", {
          receiver: this.email,
          fridge: this.fridge.id,
        })
        .then((response) => {
          if (response.data.message === "error") {
            this.errors.push(response.data.error);
          }
          console.log("Sent requets to join the fridge", response.data);
        });

      this.showInvitePopUp = false;
    },

    addToList(itemId) {
      const index = this.selectedItems.indexOf(itemId);
      if (index === -1) {
        console.log("does not exist");
        this.selectedItems.push(itemId);
      } else {
        this.selectedItems.splice(index, 1);
      }
      console.log(this.selectedItems);
    },

    removeItems() {
      this.confirm.require({
        message: "Are you sure you want to delete these items?",
        header: "Delete items",
        icon: "pi pi-exclamation-triangle",
        rejectClass: "p-button-secondary p-button-outlined",
        rejectLabel: "Cancel",
        acceptLabel: "Remove",
        accept: () => {
          axios
            .post(`/fridge/remove-item`, { items: this.selectedItems })
            .then((response) => {
              console.log("response data: ", response.data);
              if (response.data.message === "success") {
                this.store.removeItemFromFridge(
                  this.fridge.id,
                  this.selectedItems
                );
                location.reload();
              }
            })
            .catch((error) => {
              console.log(error);
            });
        },
        reject: () => {
          console.log("Declined");
        },
      });
    },
  },
};
</script>
<style>
.items-header {
  text-align: center;
}
.p-orderlist-list > li {
  padding: 0;
}
.p-orderlist-list > li > .item-div {
  padding: 12px 20px 12px 20px;
}
</style>
