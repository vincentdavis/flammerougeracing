<template>
  <div>
    <v-card class="d-flex justify-space-between mb-1" flat elevation="0" tile>
      <v-card elevation="0">
        Races ( <b>{{ races.length }}</b> )
      </v-card>
    </v-card>

    <v-expansion-panels>
      <v-expansion-panel v-bind:key="race" v-for="race in races">
        <v-expansion-panel-header disable-icon-rotate>
                     {{ race.name }}
          <template v-slot:actions>
            <!-- <v-chip small>{{ race.start_time_format }}</v-chip> -->
            <b v-if="race.timer " style="color: red">{{ race.timer }}</b>
            <div v-else>
              <v-chip small color="success">Completed</v-chip>
            </div>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-chip> {{ race.start_time_format }} </v-chip>
          <Results :zwift_id="race.zwift_id"></Results>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import { Index } from "@/mixins/index";
import Results from "@/views/Results.vue";
export default {
  mixins: [Index],
  components: { Results },
  name: "race-s",
  data() {
    return {
      races: null,
      selectedItem: 0,
    };
  },
  mounted() {
    this.detail_race();
    setInterval(() => {
      this.startTimer();
    }, 1000);
  },
  methods: {
    startTimer: function () {
      try{
        for (var race of this.races) {
          // console.log(this.caculate_time(event.start_date))
          console.log(race.start_time)
          console.log(this.caculate_time(race.start_time))
          race.timer = this.caculate_time(race.start_time)
          // if (!this.caculate_time(race.start_date)){
          //   race.timer = 'Completed'

          // }
        }
      }
      catch(err){err}
    },
    detail_race() {
      if (this.$route.params.id) {
        this.racesAPI("?race_series=" + this.$route.params.id).then((data) => {
          this.races = data.data;
        });
      }
    },
  },
};
</script>

<style>
</style>