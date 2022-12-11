<template>
  <v-card elevation="0" class="ma-2">
    <v-card-title class="ma-0 pa-0">
      <div class="d-flex">
        <div class="ma-3">
          <v-progress-circular color="primary" :rotate="360" :size="60" :width="10" value="0"> 0 </v-progress-circular>
        </div>
        <div>
          <v-card-title class="text-capitalize">
            {{ project_detail.name }}
            <v-spacer></v-spacer>
          </v-card-title>
          <!-- <v-card-text class="mt-2 pa-0 text-capitalize">{{ project_detail.description }} </v-card-text> -->
          <v-card-text class="d-flex">
            <v-chip small color="success">{{ project_detail.status }}</v-chip>
            <v-divider class="ma-1" vertical></v-divider>
            Owner: {{ project_detail.bu_head_fullname ? project_detail.bu_head_fullname : project_detail.bu_head }}
          </v-card-text>
        </div>
      </div>
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon>mdi-dots-horizontal</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item @click="handleClick(item)">
            <v-list-item-title>
              <TableColoumnConfig @header_list="set_widget" title="Customize Widgets" :FieldList="widget_list">
              </TableColoumnConfig>
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-card-title>

    <v-card-actions>
      <v-spacer></v-spacer>
      <slot name="actions"> </slot>
    </v-card-actions>
  </v-card>
</template>

<script>
import TableColoumnConfig from '@/components/DataTable/TableColoumnConfig.vue'
// Mixins
import { Project } from '@/mixins/Project'
export default {
  mixins: [Project],
  components: {
    TableColoumnConfig,
  },
  props: {
    project_detail: { default: {} },
  },
  data() {
    return {
      items: [{ title: 'Customize Widgets' }],
      widget_list: [],
    }
  },
  mounted() {
    this.get_widget_list()
  },
  methods: {
    handleClick(item) {
      console.log(item)
    },
    set_widget(widgets) {
      console.log(widgets)
      this.SetWidgets(widgets)
    },
    get_widget_list() {
      if (this.project_detail.id) {
        this.PROJECT_API_PROJECT(this.project_detail.id + '/widgets/')
          .then(data => {
            this.widget_list = data.data
            this.SetWidgets(this.widget_list)
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
  },
}
</script>

<style>
</style>