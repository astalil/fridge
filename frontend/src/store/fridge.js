import { defineStore } from 'pinia'

export const  useFridgeStore = defineStore({

    id: "fridge",

    state: () => ({
        fridges: []
    }),

    actions: {
        setFridges(data) {
            this.fridges = data.fridges
        }
    }
})