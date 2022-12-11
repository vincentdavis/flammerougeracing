<template>
  <app-card-actions @refresh="refetchData">
    <template slot="title" class="text-caption"
      ><v-icon color="primary">mdi-drag-vertical</v-icon> {{ title }}
    </template>
    <template slot="before-actions">
      <v-chip v-if="show_chip && items" class="v-chip-light-bg primary--text me-3"  color="primary" small>
        {{ items.overall_total }} Pending Approvals</v-chip
      >
    </template>
    <v-card-text>
      <v-simple-table dense fixed-header height="300px">
        <template v-slot:default>
          <v-list dense>
            <template v-for="(item, index) in items.results">
              <v-list-item :key="item.title">
                <template v-slot:default="{ active }">
                  <!-- If Project -->
                  <template v-if="item.type == 'project'">
                    <v-list-item-content>
                      <v-list-item-title class="text-capitalize">
                        <b>{{ item.name }}</b
                        >({{ item.type }})</v-list-item-title
                      >

                      <v-list-item-subtitle class="d-flex">
                        {{ item.status }}
                        <v-divider class="ma-1" vertical></v-divider>
                        Submitter: {{ item.submitter }}
                      </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-action>
                      <v-btn x-small text color="primary text-capitalize" @click="generate_route(item)"> Approve</v-btn>
                    </v-list-item-action>
                  </template>
                  <!-- If CR -->
                  <template v-if="item.type == 'change request'">
                    <v-list-item-content>
                      <v-list-item-title class="text-capitalize">
                        <b>{{ item.reason }}</b
                        >({{ item.type }})</v-list-item-title
                      >

                      <v-list-item-subtitle class="d-flex">
                        {{ item.status }}
                        <v-divider class="ma-1" vertical></v-divider>
                        Submitter: {{ item.submitter }}
                      </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-action>
                      <v-btn x-small text color="primary text-capitalize" @click="generate_cr_route(item)">
                        Approve</v-btn
                      >
                    </v-list-item-action>
                  </template>
                </template>
              </v-list-item>

              <v-divider v-if="index < items.length - 1" :key="index"></v-divider>
            </template>
          </v-list>
        </template>
      </v-simple-table>
    </v-card-text>
  </app-card-actions>
</template>

<script>
import AppCardActions from '@core/components/app-card-actions/AppCardActions.vue'
import store from '@/store'
import { ref, onUnmounted } from '@vue/composition-api'

import { Helper } from '@/mixins/Helper'

export default {
  mixins: [Helper],
  components: {
    AppCardActions,
  },
  mounted() {
    this.refetchData()
  },
  props: {
    title: { default: 'Default' },
    api: { default: '' },
    show_chip: { default: false },
  },
  setup(props) {
    const items = ref([])

    const refetchData = hideOveraly => {
      store.dispatch('API', props.api).then(data => {
        items.value = data.data
        try {
          hideOveraly()
        } catch (_) {}
      })
    }

    return {
      refetchData,
      items,
    }
  },
}
</script>
