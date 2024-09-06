<template>
  <div class="home">
    <div class="title">
      <p>Welcome to FreshAlert - Your Ultimate Food Management Companion!</p>
    </div>
    <div class="text-container">
      <div class="starting-container">
        <p>
          Tired of losing track of what's in your fridge? Say goodbye to wasted
          food and expired groceries with FreshAlert, the smart way to manage
          your kitchen.
        </p>
      </div>
      <div class="bullet-container">
        <ul class="bullet-list">
          <li>
            <h3>Register & Get Started</h3>
            <p>
              Sign up in seconds and start organizing your food items.
              FreshAlert helps you keep tabs on what's in your fridge, so you
              always know what's fresh and what's nearing its expiration date.
            </p>
          </li>
          <li>
            <h3>Create & Customize Your Fridge</h3>
            <p>
              Set up your personal fridge with just a few clicks. Add items, set
              expiration dates, and receive reminders when something is about to
              expire. Stay organized and never let good food go to waste again.
            </p>
          </li>
          <li>
            <h3>Invite Your Household</h3>
            <p>
              Cooking for a family or sharing a kitchen with roommates? No
              problem! FreshAlert allows you to invite others to your fridge.
              Collaborate on adding items, keeping everything in one place, and
              ensuring everyone is in the loop.
            </p>
          </li>
          <li>
            <h3>Stay Fresh Together</h3>
            <p>
              With FreshAlert, food management becomes a shared responsibility.
              Keep your fridge stocked, fresh, and waste-free, all while working
              together with the people you care about.
            </p>
          </li>
        </ul>
      </div>
      <div class="join-today-container">
        <p>
          Join FreshAlert today and make the most of your groceries, reduce
          waste, and enjoy a more organized kitchen!
        </p>
      </div>
      <div>
        <hr />
        <p>Brought to you by Ichner and Fat Patricia</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style>
.home {
  margin: 0 auto;
}
/* .text-container {
  border: 1px solid black;
  border-radius: 20px;
  background-image: url("@/assets/images/fridge.jpeg");
  background-repeat: no-repeat;
  background-position: center;
} */
.bullet-list {
  list-style-type: none;
  padding: 0;
}

li {
  border: 1px solid black;
  border-radius: 20px;
  padding: 10px;
  margin-top: 15px;
}
li > h3 {
  text-align: center;
}
li > p {
  text-align: center;
}
</style>
