<template>
  <div>
     <v-expansion-panels>
    <v-expansion-panel v-bind:key="race" v-for="race in races">
        <v-expansion-panel-header disable-icon-rotate>
          {{race.name}}
          <template v-slot:actions>
            <v-chip small>{{race.time}}</v-chip>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
            <Results :zwift_id="race.zwift_id"></Results>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import { Index } from "@/mixins/index";
import Results from '@/views/Results.vue'
export default {
  mixins: [Index],
  components: {Results},
  name: "race-s",
  data() {
    return {
      races: null,
      selectedItem: 0,
    };
  },
  mounted() {
    this.detail_race();
  },
  methods: {
    detail_race() {
      if (this.$route.params.id) {
        this.racesAPI('?race_series='+this.$route.params.id ).then((data) => {
          this.races = data.data;
        });
      }
    },
  },
};
</script>

<style>
</style>