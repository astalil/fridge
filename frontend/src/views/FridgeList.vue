<template>
  <div class="list">
    <h2>My Fridges</h2> - <Button label="ADD NEW" @click="visible = true" />
    <div>

    </div>
    <div>
    
      <ol>
        <li v-for="fridge in fridges" :key="fridge.id"><router-link :to="{ name: 'fridge-items', params: { id: fridge.id }}">{{ fridge.name }}</router-link> <span v-if="fridge.is_owner"> - {{ fridge.is_owner }} I own it</span></li>
      </ol>
    </div>


    <div>
      <Dialog v-model:visible="visible" modal header="Edit Profile" :style="{ width: '25rem' }">
        <span class="p-text-secondary block mb-5">Add new fridge</span>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="font-semibold w-6rem">Name</label>
            <InputText id="name" class="flex-auto" v-model="name" autocomplete="off" />
        </div>
        

        <div class="flex justify-content-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
            <Button type="button" label="Add" @click="addNewFridge"></Button>
        </div>
      </Dialog>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/store/user";
import axios from "axios";

export default {
  setup() {
    const store = useUserStore()

    return{
      fridges: store.fridges,
      
    }
  },

  data(){
    return{
      visible: false,
      name: null
    }
  },

  methods: {
    async addNewFridge() {
      await axios
      .post("fridge/new-fridge", {name: this.name})
      .then( (response) => {
        if (response.data.message === 'error') {
          //do something
        }
        else {
          //refresh fridges (call backend maybe)
        }

      })
      this.visible = false
    }
  }
}

</script>