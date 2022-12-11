<template>
  <v-simple-table fixed-header>
    <template v-slot:default>
      <v-row class="ma-1">
        <template v-for="widget in Widgets">
          <v-col v-bind:key="widget" v-if="widget.is_default" cols="12" :sm="widget.sm ? widget.sm : ''" class="ma-0 pa-1" >
            <components :is="widget.widget" :title="widget.text" :api="widget.api"> </components>
          </v-col>
        </template>

        <!-- <v-col cols="12" md="4">
                <Status title="Milestone Status" api="status/?tab=milestone"></Status>
              </v-col>
              <v-col cols="12" md="4">
                <Status title="Dependency Status"></Status>
              </v-col>
              <v-col cols="12" md="4">
                <Status title="Risk Status"></Status>
              </v-col> -->
      </v-row>
    </template>
  </v-simple-table>
</template>

<script>
import Status from '@/components/Project/Widget/Status.vue'
import AllocatedResource from '@/components/Project/Widget/AllocatedResource.vue'
import Portfolio from '@/components/Project/Widget/Portfolio.vue'
import Expense from '@/components/Project/Widget/Expense.vue'
import { Project } from '@/mixins/Project'

export default {
  mixins: [Project],
  components: {
    Status,
    AllocatedResource,
    Portfolio,
    Expense
  },
}
</script>

<style>
</style>