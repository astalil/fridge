import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import { createPinia } from "pinia";
import axios from "axios";
import PrimeVue from "primevue/config";
import "primevue/resources/themes/lara-light-indigo/theme.css";
//import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

import InputText from "primevue/inputtext";
import Button from "primevue/button";
import Password from "primevue/password";
import FloatLabel from "primevue/floatlabel";
import Dialog from 'primevue/dialog';
import OrderList from 'primevue/orderlist';


axios.defaults.baseURL = "http://127.0.0.1:8000";

const app = createApp(App);
app.use(createPinia());
app.use(router, axios);

app.use(PrimeVue);
app.component("InputText", InputText);
app.component("Button", Button);
app.component("Password", Password);
app.component("FloatLabel", FloatLabel);
app.component("Dialog", Dialog);
app.component("OrderList", OrderList);

app.mount("#app");
