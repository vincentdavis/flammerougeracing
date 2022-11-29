<template>
  <div>
    <v-row v-if="getters_races.length >= 1">
      <template v-if="getters_race_loader">
        <v-col  cols="12" sm="4"  class="ma-0 pa-0" v-bind:key="i" v-for="i in 9">
        <v-skeleton-loader
          v-bind="attrs"
          type="list-item-avatar-two-line"
        ></v-skeleton-loader>
      </v-col>
      </template>
      
      <v-col cols="12" sm="4" v-bind:key="race" v-for="race in getters_races">
        

        <v-card
          @click="
            $router.push({
              name: 'race_series_detail',
              params: { id: race.id },
            })
          "
          elevation="0"
        >
          <v-list-item three-line>
            <v-list-item-avatar tile size="60">
              <v-img :src="race.logo"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <!-- <div class="text-overline mb-4">OVERLINE</div> -->
              <v-list-item-title :title="race.name" class="mb-1">
                {{ race.name }}
              </v-list-item-title>
              <v-list-item-subtitle
              v-if="race.start_time"
                >Starts in
                <b style="color: red">{{ race.start_time }}</b></v-list-item-subtitle
              >
              <v-list-item-subtitle
              v-if="race.end_time"
                >Ending in
                <b style="color: red">{{ race.end_time }}</b></v-list-item-subtitle
              >
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
    <template v-else>
      <center>No Race Found</center>
    </template>
  </div>
</template>

<script>
import { Index } from "@/mixins/index";
// import eventsVue from './events.vue';
export default {
  mixins: [Index],
  mounted() {
    setInterval(() => {
      this.startTimer();
    }, 1000);
  },
  data() {
    return {
      timerOutput: "0",
    };
  },
  computed: {},
  methods: {
    startTimer: function () {
      try{
        for (var event of this.getters_races) {
          // console.log(this.caculate_time(event.start_date))
          event.start_time = this.caculate_time(event.start_date)
          if (!this.caculate_time(event.start_date)){
            event.end_time = this.caculate_time(event.end_date)

          }
        }
      }
      catch(err){err}
    },
  },
};
</script>

<style>
</style>