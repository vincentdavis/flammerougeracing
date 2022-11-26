<template>
  
  <v-card rounded elevation="0">
          <v-img
            class="ma-0 pa-0"
            contain
            src="https://ts-production.imgix.net/images/9ced2ef0-d902-4672-8def-e23a4d57303d.jpg?auto=compress,format&w=800&h=450"
          >
            <v-app-bar flat color="rgba(0, 0, 0, 0)">
              <v-spacer></v-spacer>

              <v-btn color="white" icon>
                <v-icon>mdi-cards-heart-outline</v-icon>
              </v-btn>
              <v-btn color="white" icon>
                <v-icon>mdi-share-variant</v-icon>
              </v-btn>
            </v-app-bar>
          </v-img>

          <v-card-title>
            {{ race_detail.name }}
          </v-card-title>
        </v-card>
</template>

<script>
import { Index } from "@/mixins/index";

export default {
  mixins: [Index],
  data() {
    return {
      race_detail: null,
      selectedItem: 0,
    };
  },
  mounted() {
    this.detail_race();
  },
  methods: {
    detail_race() {
      if (this.$route.params.id) {
        this.detail_races(this.$route.params.id + "/").then((data) => {
          this.race_detail = data.data;
        });
      }
    },
  },
};
</script>

<style>

</style>