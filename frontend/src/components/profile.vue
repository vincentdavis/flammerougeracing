<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-width="200"
    offset-x
  >
    <template v-slot:activator="{ on, attrs }">
      <v-avatar>
        <v-icon color="primary" large v-bind="attrs" v-on="on"> mdi-account-circle </v-icon>
      </v-avatar>
    </template>

    <v-card>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-icon color="primary" large > mdi-account-circle </v-icon>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title class="text-capitalize"
              >{{ profile.first_name }}
              {{ profile.second_name }}</v-list-item-title
            >
            <v-list-item-subtitle>{{ profile.email }}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <!-- <v-btn :class="fav ? 'red--text' : ''" icon @click="fav = !fav">
              <v-icon>mdi-heart</v-icon>
            </v-btn> -->
          </v-list-item-action>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item @click="add_zwift_profile" v-if="!profile.zwift_id">
          <v-list-item-title class="text--red">
            <v-alert dense type="error">Add Zwift Profile</v-alert>
          </v-list-item-title>
        </v-list-item>
        <v-list-item v-else>
          <v-list-item-title class="text--red">
            <v-alert dense type="success">Zwift ID: {{profile.zwift_id}}</v-alert>
          </v-list-item-title>
        </v-list-item>

        <!-- <v-list-item>
          <v-list-item-action>
            <v-switch v-model="hints" color="purple"></v-switch>
          </v-list-item-action>
          <v-list-item-title>Enable hints</v-list-item-title>
        </v-list-item> -->
      </v-list>

      <v-card-actions>
        <v-spacer></v-spacer>

        <!-- <v-btn text @click="menu = false"> Cancel </v-btn> -->
        <v-btn color="primary" text @click="menu = false"> Logout </v-btn>
      </v-card-actions>
    </v-card>
  </v-menu>
</template>

<script>
import { Index } from "@/mixins/index";

export default {
  mixins: [Index],

  name: "ProfileComponent",
  data: () => ({
    fav: true,
    menu: false,
    message: false,
    hints: true,
  }),
  methods: {
    add_zwift_profile(){
        this.zwift_link_modal(true)
    }
  }
};
</script>

<style>
</style>