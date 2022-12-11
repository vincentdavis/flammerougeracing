<template>
  <div class="ma-2">
    <div class="ma-3">
      <div class="d-flex justify-space-between">
        <Section :label="`${resources.length} Resource Allocated`"></Section><br />

        <div>
          <div class="d-flex">
            <div class="mr-2">
              <!-- View -->
              <v-btn-toggle small mandatory rounded color="primary" dense v-model="toggle_view">
                <v-btn>
                  <v-icon>mdi-card-account-details</v-icon>
                </v-btn>

                <v-btn>
                  <v-icon>mdi-table</v-icon>
                </v-btn>
              </v-btn-toggle>
            </div>

            <div class="mt-1">
              <BaseButton
                click="OpenDrawerOnClick"
                title="Add Resource"
                tooltip="Add New Resource to Team"
                :options="{
                  ShowAppBarOnDrawer: true,
                  DrawerSize: '70%',
                  DrawerFormType: 'ResourceAdd',
                  DrawerFormTitle: 'Resource Add',
                  DrawerFormAPICall: true,
                  DrawerMutation: 'mutation__drawer',
                  DrawerActionType: 'new',
                  DrawerShowAction: false,
                  DrawerFormSubmit: {
                    btn_name: '',
                    store_action_name: '',
                    custom_action: '',
                  },
                }"
              />
            </div>
          </div>
        </div>
      </div>
      <br />
    </div>

    <div class="ma-2">
      <!-- View -->
      <v-row v-if="toggle_view == 0">
        <v-col class="ma-0 pa-1" cols="12" sm="3" v-bind:key="resource" v-for="resource in resources">
          <v-card>
            <v-list-item>
              <template v-slot:default="{ active }">
                <v-list-item-content>
                  <v-list-item-title v-text="resource.resource_name"></v-list-item-title>

                  <v-list-item-subtitle class="text--primary" v-text="resource.role"></v-list-item-subtitle>

                  <v-list-item-subtitle v-text="resource.team"></v-list-item-subtitle>
                  <div class="ma-0 pa-0">
                    <div class="d-flex justify-space-between">
                      <div>
                        <b>{{ resource.start_date }}</b>
                      </div>
                      <v-divider class="mt-2 ml-2"></v-divider>
                      <!-- <div>
                        <b>{{ resource.end_date }}</b>
                      </div> -->
                    </div>
                  </div>
                </v-list-item-content>

                <v-list-item-action>
                  <v-list-item-action-text>
                    <!-- <b>{{ resource.start_date }}</b> To <b>{{ resource.end_date }} </b> -->
                    <!-- <b>{{ resource.allocation }}</b> % -->
                  </v-list-item-action-text>

                  <div>
                    <b>{{ resource.allocation }}</b> %
                  </div>
                  <div>
                    <!-- <b>{{ resource.allocation }}</b> % -->
                    <b>{{ resource.end_date }}</b>
                  </div>
                  <!-- <v-icon
                    color="red"
                    >
                    mdi-trash-can
                    </v-icon> -->
                </v-list-item-action>
              </template>
            </v-list-item>
            <v-divider></v-divider>
            <v-card-actions class="ma-2 pa-0">
              <v-btn icon small @click="delete_resource(resource)"
                ><v-icon small color="red">mdi-trash-can</v-icon></v-btn
              >
              <v-btn icon small><v-icon small color="blue">mdi-pencil</v-icon></v-btn>
              <v-spacer></v-spacer>
              <b> {{ resource.cost | currency_format }}</b>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col v-if="resources.length < 1">
          <v-alert border="top" type="error"
            >No Resource allocated. Please click `Add Resource` to add new resource</v-alert
          >
        </v-col>
        <v-col cols="12" sm="12">
          <v-divider></v-divider>
          <v-list>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Total Cost</v-list-item-title>
              </v-list-item-content>

              <v-list-item-action>
                <v-list-item-action-text
                  ><h2>{{ calculate_total_cost | currency_format }}</h2></v-list-item-action-text
                >
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
      <template v-if="toggle_view == 1">
        <ViewList
          :handlerow="false"
          ref="ProjectList"
          :options="{
            store_action_name: 'ResourceStore/Resource_API',
          }"
        >
          <template #item-team="{ item }">
            <v-chip small>{{ item.team }}</v-chip>
          </template>
          
        </ViewList>
      </template>
    </div>
  </div>
</template>

<script>
import Section from '@/components/Helpers/Section.vue'
import BaseButton from '@/components/Button/BaseButton.vue'
import ViewList from '@/components/DataTable/ViewList.vue'

import { Project } from '@/mixins/Project'
import { Helper } from '@/mixins/Helper'
import { ref } from '@vue/composition-api'
import { bus } from '@/main'
import { status_color } from '@/helper'

export default {
  mixins: [Project, Helper],
  props: {
    pid: { default: null },
  },
  created() {
    bus.$on('resource__delete_confirmation', (value, options, value2) => {
      console.log(options)
      this.PROJECT_API_PROJECT_DELETE(this.pid + '/resources/' + options.resource_id + '/')
        .then(data => {
          this.$store.dispatch('Snackbar', {
            bar: true,
            color: status_color(data.status),
            text: data.data,
          })
          this.get_resources()
        })
        .catch(err => {
          
          console.log(err)
        })
    })
  },
  computed: {
    calculate_total_cost() {
      var total = 0
      for (var resource of this.resources) {
        total += resource.cost
      }
      return total
    },
  },
  setup(props) {
    const resources = ref([])
    const toggle_view = ref(0)
    function get_resources() {
      this.PROJECT_API_PROJECT(props.pid + '/resources/').then(data => {
        resources.value = data.data
      })
    }
    function delete_resource(resource) {
      this.$store.dispatch('OpenConfirmationDialogOnClick', {
        Dialog: true,
        Title: 'Confirmation',
        Body: `Remove ${resource.resource_name} ?`,
        SubmitButton: {
          title: 'Yes, Remove',
          text: true,
          color: 'success',
          click: 'CloseConfirmationDialog',
          options: {
            resource_id: resource.id,
            on_success: {
              bus_emit: 'resource__delete_confirmation',
            },
          },
        },
      })
    }

    return {
      resources,
      toggle_view,
      get_resources,
      delete_resource,
    }
  },
  mounted() {
    this.get_resources()
  },
  components: {
    Section,
    BaseButton,
    ViewList,
  },
}
</script>

<style>
</style>