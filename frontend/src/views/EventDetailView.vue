<template>
  <div
    style="
      background: #e3f2fd;
      background: -webkit-linear-gradient(to top, #ffffff, #ffffff, #bbdefb);
      background: linear-gradient(to top, #ffffff, #ffffff, #bbdefb);
    "
  >
    <v-row v-if="race_detail" class="ma-5">
      <v-col sm="2">
        <v-list rounded nav dense color="transparent">
          <v-list-item-group v-model="selectedItem" color="primary">
            <v-list-item  :to="{ name: 'race-details', params: { id: race_detail.id } }" link>
              <v-list-item-icon>
                <v-icon>mdi-directions</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title> Race Series </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{ name: 'races', params: { id: race_detail.id } }" link>
              <v-list-item-icon>
                <v-icon>mdi-bike</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title> Race </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>

          <v-divider class="my-2"></v-divider>

          <v-list-item link color="grey lighten-4">
            <v-list-item-content>
              <v-list-item-title> Refresh </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col sm="8">
                <router-view></router-view>

      </v-col>
      <v-col sm="2">
        <v-btn block color="primary" rounded
          >Enter Race <v-icon>mdi-arrow-right-thin</v-icon></v-btn
        >

        <v-card class="mt-3" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="">Have a question?</div>

              <v-list-item-subtitle
                >Send your queries to the event organizer
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-card-actions>
            <v-btn outlined small class="text-capitalize" rounded block>
              Contact Organizer
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- <v-col cols="12" sm="10">
        <v-tabs horizontal>
          <v-tab class="text-capitalization"> Race Series </v-tab>
          <v-tab disabled>
            <v-icon left> </v-icon>
            Venue
          </v-tab>
          <v-tab disabled>
            <v-icon left> </v-icon>
            Notification
          </v-tab>
          <v-tab>
            <v-icon left> </v-icon>
            Races
          </v-tab>

          <v-tab-item>
            <v-card oulined>
              <v-card-title>{{ race_detail.name }}</v-card-title>

              <v-img height="400" contain :src="race_detail.logo"></v-img>
              <v-divider></v-divider>
              <p>{{ race_detail.description }}</p>
            </v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card flat> </v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card flat> </v-card>
          </v-tab-item>
        </v-tabs>
      </v-col>

      <v-col cols="12" sm="2">
        <center>
          <v-btn color="primary" x-large rounded
            >Enter Race <v-icon>mdi-arrow-right-thin</v-icon></v-btn
          >
        </center>
      </v-col> -->
    <!-- </v-row> -->
  </div>
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
    this.$router.push({ name: 'race-details', params: { id: this.$route.params.id  } })
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