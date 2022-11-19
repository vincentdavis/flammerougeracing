<template>
  <v-app>
    <v-app-bar color="white" elevation="0" app>
      <!-- <v-toolbar-title style="cursor:pointer" @click="$router.push({name: 'home'})">Flamme Rouge Racing</v-toolbar-title> -->
      <v-img
        style="cursor: pointer"
        @click="$router.push({ name: 'home' })"
        max-height="53"
        max-width="250"
        src="@/assets/FRR.png"
      ></v-img>
      <v-text-field
        clearable
        width="30"
        color="primary"
        class="ma-5"
        placeholder="Search for races"
        outlined
        hide-details
        rounded
        dense
        prepend-inner-icon="mdi-magnify"
      ></v-text-field>

      <v-spacer></v-spacer>
      <v-avatar
        class="hidden-sm-and-down"
        color="grey darken-1 shrink"
        size="32"
      ></v-avatar>
    </v-app-bar>

    <v-main>
      <!-- <v-banner dense v-model="v0" single-line
        >Notification Banner
        <template v-slot:actions>
          <v-btn
            text
            transition="slide-y-transition"
            small
            color="primary"
            class="text-capitalize"
          >
            Banner action
          </v-btn>
          <v-btn small color="red" @click="v0 = false" icon
            ><v-icon>mdi-close</v-icon></v-btn
          >
        </template>
      </v-banner> -->

      <transition
      name="scale-transition"
      mode="out-in"
      appear
    >
      <router-view></router-view>
    </transition>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    v0: true,

    //
  }),
};
</script>
