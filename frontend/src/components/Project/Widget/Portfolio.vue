<template>
  <v-card>
    <v-card-title class="align-start">
      <v-icon color="primary">mdi-drag</v-icon> <span>Project Portfolio</span>
      <v-spacer></v-spacer>
      <!-- <v-btn icon small class="me-n3 mt-n2">
        <v-icon>
          {{ icons.mdiDotsVertical }}
        </v-icon>
      </v-btn> -->
    </v-card-title>

    <!-- <v-card-subtitle class="mb-8 mt-n5">
      <span class="font-weight-semibold text--primary me-1">Total 48.5% Growth</span>
      <span>😎 this month</span>
    </v-card-subtitle> -->

    <v-card-text>
      <v-row>
        <v-col v-for="data in statisticsData" :key="data.title" cols="6" md="3" class="d-flex align-center">
          <v-avatar size="44" :color="resolveStatisticsIconVariation(data.title).color" rounded class="elevation-1">
            <v-icon dark color="white" size="30">
              {{ resolveStatisticsIconVariation(data.title).icon }}
            </v-icon>
          </v-avatar>
          <div class="ms-3">
            <p class="text-xs mb-0">
              {{ data.title }}
            </p>
            <h3 class="text-xl font-weight-semibold">
              {{ data.total }}
            </h3>
          </div>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
// eslint-disable-next-line object-curly-newline
import { mdiAccountOutline, mdiCurrencyUsd, mdiTrendingUp, mdiDotsVertical, mdiLabelOutline } from '@mdi/js'

export default {
  setup() {
    const statisticsData = [
      {
        title: 'Cost',
        total: '$0',
      },

      {
        title: 'Expense',
        total: '$0',
      },
      {
        title: 'Revenue',
        total: '$0',
      },
      {
        title: 'Profit',
        total: '$0',
      },
    ]

    const resolveStatisticsIconVariation = data => {
      if (data === 'Cost') return { icon: mdiCurrencyUsd, color: 'primary' }
      if (data === 'Expense') return { icon: mdiCurrencyUsd, color: 'primary' }
      if (data === 'Revenue') return { icon: mdiCurrencyUsd, color: 'primary' }
      if (data === 'Profit') return { icon: mdiTrendingUp, color: 'primary' }

      return { icon: mdiAccountOutline, color: 'success' }
    }

    return {
      statisticsData,
      resolveStatisticsIconVariation,

      // icons
      icons: {
        mdiDotsVertical,
        mdiTrendingUp,
        mdiAccountOutline,
        mdiLabelOutline,
        mdiCurrencyUsd,
      },
    }
  },
}
</script>
