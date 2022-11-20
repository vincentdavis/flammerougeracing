<template>
  <v-app>
    <v-overlay :value="main_loader" absolute>
      <v-progress-circular indeterminate size="25"></v-progress-circular>
      Loading FRR
    </v-overlay>

    <v-app-bar v-if="!main_loader" color="white" elevation="0" app>
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

      <profile></profile>
    </v-app-bar>

    <v-main v-if="!main_loader">
      <v-banner v-if="!profile.zwift_id" dense v-model="v0" single-line
        ><v-icon slot="icon" color="warning" size="36">
          mdi-alert-circle
        </v-icon>
        Zwifit account not linked. Please link your zwift account to join race
        <template v-slot:actions>
          <v-btn
            transition="slide-y-transition"
            small
            rounded
            color="primary"
            class="text-capitalize"
            @click="add_zwift"
          >
            Link Zwift Account
          </v-btn>
          <v-btn small rounded color="red" @click="v0 = false" icon
            ><v-icon>mdi-close</v-icon></v-btn
          >
        </template>
      </v-banner>
      <link_zwift_account></link_zwift_account>
      <transition name="scroll-x-transition" mode="out-in" appear>
        <router-view></router-view>
      </transition>
    </v-main>
  </v-app>
</template>

<script>
import { Index } from "@/mixins/index";
import profile from "@/components/profile.vue";
import link_zwift_account from "@/components/link_zwift_account.vue";

export default {
  mixins: [Index],
  name: "App",
  components: { profile, link_zwift_account },
  data: () => ({
    v0: true,
    main_loader: true,

    //
  }),
  methods:{
    add_zwift(){
      this.zwift_link_modal(true)
    }
  },
  mounted() {
    this.main_loader = true;
    this.get_profile()
      .then(() => {
        this.main_loader = false;
      })
      .catch(() => {
        this.main_loader = false;
      });
  },
};
</script>
