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
                >Starts in
                <b style="color: red">{{ race.time }}</b></v-list-item-subtitle
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
      for (var event of this.getters_races) {
        event.time = this.caculate_time(event.start_date);
        //   this.timerOutput =
        //     remainingDays +
        //     " Days " +
        //     remainingHours +
        //     " Hrs " +
        //     remainingMinutes +
        //     " Min " +
        //     remainingSeconds +
        //     " Sec";
      }
      //   const timeNow = new Date().getTime();
      //   const timeDifference = new Date("Nov 22, 2022 21:00:00").getTime() - timeNow;
      //   const millisecondsInOneSecond = 1000;
      //   const millisecondsInOneMinute = millisecondsInOneSecond * 60;
      //   const millisecondsInOneHour = millisecondsInOneMinute * 60;
      //   const millisecondsInOneDay = millisecondsInOneHour * 24;
      //   const differenceInDays = timeDifference / millisecondsInOneDay;
      //   const remainderDifferenceInHours =
      //     (timeDifference % millisecondsInOneDay) / millisecondsInOneHour;
      //   const remainderDifferenceInMinutes =
      //     (timeDifference % millisecondsInOneHour) / millisecondsInOneMinute;
      //   const remainderDifferenceInSeconds =
      //     (timeDifference % millisecondsInOneMinute) / millisecondsInOneSecond;
      //   const remainingDays = Math.floor(differenceInDays);
      //   const remainingHours = Math.floor(remainderDifferenceInHours);
      //   const remainingMinutes = Math.floor(remainderDifferenceInMinutes);
      //   const remainingSeconds = Math.floor(remainderDifferenceInSeconds);
      //   this.timerOutput =
      //     remainingDays +
      //     " Days " +
      //     remainingHours +
      //     " Hrs " +
      //     remainingMinutes +
      //     " Min " +
      //     remainingSeconds +
      //     " Sec";
    },
  },
};
</script>

<style>
</style>