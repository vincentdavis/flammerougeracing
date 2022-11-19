<template>
  <v-row>
    <v-col cols="12" sm="12">
      <v-card elevation="0">
        <v-card-text>
          <v-carousel
            :continuous="true"
            :cycle="cycle"
            :show-arrows="true"
            hide-delimiter-background
            delimiter-icon="mdi-minus"
            height="300"
          >
            <v-carousel-item v-for="(slide, i) in getters_races" :key="i">
              <v-img :src="slide.logo"></v-img>
              <!-- <v-sheet :color="colors[i]" height="100%" tile>
                <v-row class="fill-height" align="center" justify="center">
                  <div class="text-h2">{{ slide }} event image</div>
                </v-row>
              </v-sheet> -->
            </v-carousel-item>
          </v-carousel>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col class="mt-0 pt-0" cols="12" sm="12">
      <v-card class="pt-0 mt-0 ma-4" elevation="0">
        <v-card-title class="mt-0 pt-0"
          >Races
          <v-spacer></v-spacer>
          <v-btn title text color="primary" @click="$router.push({name: 'series'})">View All</v-btn>
        </v-card-title>
        <v-card-text>
          <events_home></events_home>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import events_home from "@/components/events_home";
import { Index } from "@/mixins/index";

export default {
  components: { events_home },
  mixins: [Index],
  data() {
    return {
      colors: [
        "green",
        "secondary",
        "yellow darken-4",
        "red lighten-2",
        "orange darken-1",
      ],
      cycle: true,
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
    };
  },
  mounted() {
    // Get Races
  },
  methods: {},
};
</script>

<style>
</style>