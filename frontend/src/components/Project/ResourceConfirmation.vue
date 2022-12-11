<template>
  <div>
    <!-- <b>{{props}}</b> -->
    <v-list two-line>
      <template v-for="(item, index) in props">
        <v-list-item :key="item.title">
          <template v-slot:default="{ active }">
            <v-list-item-content>
              <v-list-item-title v-text="item.emp_id"></v-list-item-title>

              <v-list-item-subtitle class="text--primary" v-text="item.role"></v-list-item-subtitle>

              <v-list-item-subtitle
                >From <b>{{ item.start_date }}</b> To <b>{{ item.end_date }}</b></v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-action>
              <v-list-item-action-text><input type="number" v-model="item.allocation" /> %</v-list-item-action-text>
              <v-list-item-action-text > <b>{{item.cost |currency_format}}</b></v-list-item-action-text>
            </v-list-item-action>
          </template>
        </v-list-item>

        <v-divider v-if="index < props.length - 1" :key="index"></v-divider>
      </template>
     
    </v-list>
     <v-divider></v-divider>
      <v-list>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>Total Cost</v-list-item-title>
          </v-list-item-content>

          <v-list-item-action>
            <v-list-item-action-text><h2>{{calculate_total_cost |currency_format}}</h2></v-list-item-action-text>
          </v-list-item-action>
        </v-list-item>
      </v-list>
  </div>
</template>

<script>
import { Helper } from '@/mixins/Helper'

export default {
  mixins:[Helper],
  data() {
    return {}
  },
  props: {
    props: {},
  },
  computed:{
    calculate_total_cost(){
      var total = 0
      for (var resource of this.props){
        total += resource.cost
      }
      return total
    }
  }
}
</script>

<style>
</style>