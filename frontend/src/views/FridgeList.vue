<template>
  <div>
    <div class="list">
      <Toast />
      <div>
        <p>Below you can see a list of fridges you're apart off!</p>
        <Button label="ADD NEW" @click="visible = true" />
      </div>

      <div>
        <ol>
          <li v-for="fridge in fridges" :key="fridge.id">
            <router-link
              :to="{ name: 'fridge-items', params: { id: fridge.id } }"
              >{{ fridge.name }}</router-link
            >
            <span v-if="fridge.is_owner">
              - {{ fridge.is_owner }} I own it</span
            >
          </li>
        </ol>
      </div>
    </div>
    <div>
      <Dialog v-model:visible="visible" modal header="Add your fridge">
        <div class="flex align-items-center gap-3 mb-3">
          <label for="name" class="font-semibold w-6rem">Name</label>
          <InputText
            id="name"
            class="flex-auto"
            v-model="name"
            autocomplete="off"
          />
        </div>

        <div class="flex justify-content-end gap-2">
          <Button
            type="button"
            label="Cancel"
            severity="secondary"
            @click="visible = false"
          ></Button>
          <Button type="button" label="Add" @click="addNewFridge"></Button>
        </div>
      </Dialog>
    </div>
  </div>
</template>

<script>
import { useToast } from "primevue/usetoast";
import { useUserStore } from "@/store/user";
import axios from "axios";

export default {
  setup() {
    const store = useUserStore();
    const toast = useToast();

    return {
      fridges: store.fridges,
      store,
      toast,
    };
  },

  data() {
    return {
      visible: false,
      name: null,
    };
  },

  methods: {
    addNewFridge() {
      axios
        .post("fridge/new-fridge", { name: this.name })
        .then((response) => {
          console.log("Adding fridge response data: ", response.data);
          if (response.data.message === "error") {
            //do something
          } else {
            this.store.addFridge(response.data.fridge);
            console.log("toast should open now");
            console.log(this.toast);
            this.toast.add({
              severity: "success",
              summary: "New fridge added",
              detail: "Successfully added a new fridge!",
              life: 3000,
            });
          }
        })
        .catch((error) => {
          console.log(error);
        });
      this.visible = false;
    },
  },
};
</script>

<style scoped>
.list {
  text-align: center;
}
ol {
  padding: 0;
  list-style: none;
}
</style>
