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
import "primeflex/primeflex.css";
import "./assets/main.css";

import InputText from "primevue/inputtext";
import Button from "primevue/button";
import Password from "primevue/password";
import FloatLabel from "primevue/floatlabel";
import Dialog from "primevue/dialog";
import OrderList from "primevue/orderlist";
import ConfirmDialog from "primevue/confirmdialog";
import ConfirmationService from "primevue/confirmationservice";
import ConfirmPopup from "primevue/confirmpopup";
import Menubar from "primevue/menubar";
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import Calendar from "primevue/calendar";

import Avatar from "primevue/avatar";
import Badge from "primevue/badge";
import Ripple from "primevue/ripple";
import Sidebar from "primevue/sidebar";
import StyleClass from "primevue/styleclass";
import Menu from "primevue/menu";

axios.defaults.baseURL = "http://127.0.0.1:8000";

const app = createApp(App);
app.use(createPinia());
app.use(router, axios);

app.use(PrimeVue, { ripple: true });
app.use(ConfirmationService);
app.use(ToastService);

app.component("InputText", InputText);
app.component("Button", Button);
app.component("Password", Password);
app.component("FloatLabel", FloatLabel);
app.component("Dialog", Dialog);
app.component("OrderList", OrderList);
app.component("ConfirmDialog", ConfirmDialog);
app.component("ConfirmPopup", ConfirmPopup);
app.component("Menubar", Menubar);
app.component("Toast", Toast);
app.component("Calendar", Calendar);

app.component("Avatar", Avatar);
app.component("Badge", Badge);
app.component("Sidebar", Sidebar);
app.component("Menu", Menu);

app.directive("ripple", Ripple);
app.directive("styleclass", StyleClass);

app.mount("#app");
