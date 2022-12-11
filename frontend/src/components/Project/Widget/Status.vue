<template>
  <v-card>
    <v-card-title>
      <v-icon color="primary">mdi-drag</v-icon>
      {{ title }}
      <v-spacer></v-spacer>
      <div>
  

        <!-- Refresh -->
        <v-btn icon small @click="get_status">
          <v-icon size="20"> mdi-refresh </v-icon>
        </v-btn>

        <!-- Slot: After Actions -->
        <slot name="after-actions"></slot>
      </div>
      <!-- <v-btn color="primary" x-small outlined @click="get_resources">refresh</v-btn> -->
    </v-card-title>
    <!-- chart -->
    <v-card-text>
      <chartjs-component-doughnut-chart
        v-if="datasets"
        :height="150"
        :data="datasets"
        :options="chartjsData.doughnutChart.options"
      />
    </v-card-text>
    <!--/ chart -->

    <!-- stocks -->
    <v-card-text>
      <div
        v-for="(stock, index) in status"
        :key="stock.device"
        :class="index < status.length - 1 ? 'mb-4' : ''"
        class="d-flex justify-space-between"
      >
        <div class="d-flex align-center">
          <v-icon size="16" :color="stock.color">
            {{ stock.symbol }}
          </v-icon>
          <span class="font-weight-bold ms-2 me-2">{{ stock.device }}</span>
          <!-- <span>- {{ stock.percentage }}%</span> -->
        </div>
        <div>
          <span>{{ stock.percentage }}%</span>
        </div>
      </div>
    </v-card-text>
    <!--/ stocks -->
  </v-card>
</template>

<script>
// eslint-disable-next-line object-curly-newline
import { mdiMonitor, mdiTabletAndroid, mdiArrowUp, mdiArrowDown } from '@mdi/js'
import ChartjsComponentDoughnutChart from '@/components/charts-components/ChartjsComponentDoughnutChart.vue'
import chartjsData from '../chartjsData'
import { Project } from '@/mixins/Project'
import { ref } from '@vue/composition-api'

export default {
  components: {
    ChartjsComponentDoughnutChart,
  },
  props: {
    title: {},
    pid: { default: null },
    api: {},
  },
  mixins: [Project],

  setup(props) {
    const status = ref([])
    const datasets = ref(null)

    function get_status() {
      datasets.value = null
      this.PROJECT_API_PROJECT(props.api).then(data => {
        status.value = data.data.text_data
        datasets.value = data.data.datasets
      })
    }

    // const stockData = [
    //   {
    //     device: 'Completed',
    //     symbol: mdiMonitor,
    //     color: 'primary',
    //     percentage: 80,
    //     upDown: 2,
    //   },
    //   {
    //     device: 'InProgress',
    //     symbol: mdiTabletAndroid,
    //     color: 'warning',
    //     percentage: 10,
    //     upDown: 8,
    //   },
    //   {
    //     device: 'Suspended',
    //     symbol: mdiTabletAndroid,
    //     color: 'success',
    //     percentage: 10,
    //     upDown: -5,
    //   },
    // ]

    return {
      chartjsData,
      get_status,
      status,
      datasets,

      // stockData,
    }
  },
  mounted() {
    this.get_status()
  },
}
</script>
