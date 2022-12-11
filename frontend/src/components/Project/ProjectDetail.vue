<template>
  <v-card elevation="0" class="ma-2">
    <v-tabs v-model="tab" elevation="0" light show-arrows height="35">
      <v-tab key="0" v-if="show_widget" class="text-capitalize">Widgets</v-tab>
      <v-tab key="1" class="text-capitalize">Details</v-tab>
      <v-tab key="2" class="text-capitalize">Activity Stream</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item v-if="show_widget">
        <Widgets ></Widgets>
      </v-tab-item>
      <v-tab-item>
        <div id="project_information" class="ma-2">
          <v-expansion-panels focusable multiple v-model="panel" left>
            <v-expansion-panel>
              <v-expansion-panel-header>
                Project Information
                <template v-slot:actions>
                  <v-icon color="primary"> mdi-arrow-down-drop-circle-outline </v-icon>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <project-information
                  :project_detail="project_detail"
                  :field_mapping="field_mapping"
                ></project-information>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header>
                Attachments
                <template v-slot:actions>
                  <v-icon color="primary"> mdi-arrow-down-drop-circle-outline </v-icon>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <Attachments  :pid="project_detail.id"></Attachments>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </div>
      </v-tab-item>
      <v-tab-item>
        <div>
          <ActivityStream :pid="project_detail.id"></ActivityStream>
        </div>
      </v-tab-item>
    </v-tabs-items>
  </v-card>

  <!-- <v-simple-table fixed-header height="400px">
    <template v-slot:default>
      <thead class="ma-0 pa-0">
        <tr class="ma-0 pa-0">
          <th class="ma-0 pa-0">
            
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="ma-0 pa-0">
          <td class="ma-2 pa-2">
            <v-tabs-items>
              <b>Hellow</b>
            </v-tabs-items>
            
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table> -->
</template>

<script>
import ProjectInformation from '@/components/Project/ProjectInformation.vue'
import Attachments from '@/components/Project/Attachments.vue'
import ActivityStream from '@/components/Project/ActivityStream.vue'
import Widgets from '@/components/Project/Widgets.vue'

export default {
  props: {
    project_detail: { default: {} },
    field_mapping: { default: [] },
    show_widget: { default: false },
  },
  components: {
    ProjectInformation,
    Attachments,
    ActivityStream,
    Widgets
  },
  data() {
    return {
      panel: [0,1],
      tab: null,
    }
  },
}
</script>

<style>
</style>