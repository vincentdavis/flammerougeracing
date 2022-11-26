<template>
  <v-container color="red">
    <h2>Upcoming Race Series</h2>
    <v-divider></v-divider>
    <div class="text-center mt-2" v-if="getters_race_loader">
    <v-progress-circular
      indeterminate
      color="primary"
    ></v-progress-circular>
      </div>
    <v-row class="mt-2">
      
      
      <v-col v-bind:key="race" v-for="race in getters_races" cols="12" sm="4">
        <v-hover v-slot="{ hover }" open-delay="10">
          <v-card @click="$router.push({name: 'race_series_detail' , params: {id: race.id}})" rounded :elevation="hover ? 18 : 2" :class="hover ? 'mb-5' : ''">
            <v-img
              gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
              height="200"
              :src="race.logo"
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
            <v-card-title>{{ race.name }}</v-card-title>
            <v-card-subtitle
              >{{ race.start_date }} - {{ race.end_date }}
            </v-card-subtitle>
          

            <v-divier></v-divier>

            <!-- <v-card-title>Dates</v-card-title>

    <v-card-text>
      <v-chip-group 
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip>5:30PM</v-chip>

        <v-chip>7:30PM</v-chip>

        <v-chip>8:00PM</v-chip>

        <v-chip>9:00PM</v-chip>
      </v-chip-group>
    </v-card-text> -->
          </v-card>
        </v-hover>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { Index } from "@/mixins/index";

export default {
  mixins: [Index],

  name: "HomeView",
  data() {
    return {};
  },
  mounted() {
    this.get_races();
  },
  components: {},
};
</script>
