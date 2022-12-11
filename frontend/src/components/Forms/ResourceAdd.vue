<template>
  <div>
     <div>
      <FormGenerator ref="form" :form="form"> </FormGenerator>
    </div>
    <div class="d-flex flex-row-reverse ma-2">
      <v-btn color="primary" small @click="call_resource_search">Search</v-btn>

      <div class="mr-2">
        <Team ref="team" :field="field" label="Team" itemtext="team_name" itemvalue="id"></Team>
      </div>
      <div>
        <v-btn
          color="primary"
          text
          class="mr-2"
          dense
          small
          @click="
            $store.dispatch('OpenDialogOnClick', {
              Dialog: true,
              Title: 'Add New Team',
              RefName: 'NewTeam_Ref',
              DialogEditType: 'new',
              FormName: 'NewTeam',
              DialogMutation: 'mutation__dialog',
              DialogExtraParam: `&project_details=${$route.params.pid}`,
              SubmitButton: { title: 'Add', text: true, color: 'success', click: 'TeamResourceStore/TeamNameCreate' },
            })
          "
          >Add New Team</v-btn
        >
      </div>
    </div>
    <div class="ma-3">
      <div class="d-flex justify-space-between">
        <Section label="Available Resources"></Section><br />
        <div>
          <!-- <h3>
            <b> Resource Selected</b>
          </h3> -->
          <v-btn v-if="selected_resource.length >= 1" @click="add_multiple_resource_to_team(selected_resource)" color="primary"  outlined x-small>
            Add ({{ selected_resource.length }}) resource
          </v-btn>
        </div>
      </div>
      <br />
      <ViewList
        :handlerow="false"
        @item-clicked="item_clicked"
        ref="search_result"
        :options="{
          store_action_name: 'JiraStore/integration_API_jira',
        }"
      >
        <template #item-availability="{ item }">
          <div style="max-width: 100px ma-1">
            <v-timeline class="ma-2" dense>
              <v-timeline-item color="orange" small>
                <v-row justify="space-between">
                  <v-col cols="7">
                    <!-- <v-chip
              class="white--text ml-0"
              color="orange"
              label
              small
            >
              Allocated
            </v-chip> -->
                    From : {{ item.start_date }} To: {{ item.end_date }}
                  </v-col>
                  <v-col class="text-right" cols="5">
                    {{ item.team }}/{{ item.project }} @ {{ item.allocation }} %</v-col
                  >
                </v-row>
              </v-timeline-item>

              <v-timeline-item color="green" v-bind:key="avl" v-for="avl in item.availability" small>
                <v-row justify="space-between">
                  <v-col cols="7">
                    <v-chip class="white--text ml-0" color="green" label small> Available </v-chip> From :
                    <b>{{ avl.start_date }}</b> To: <b>{{ avl.end_date }}</b> 
                    <template v-if="avl.start_date != item.a_sd">
                      <br />
                      Note: Resource not available from project start date
                    </template>
                    <!-- <template v-if="avl.end_date != item.a_ed">
              <br>
             Note: Resource not available till project end date
             </template> -->
                  </v-col>
                  <v-col class="text-right" cols="5">
                    {{ avl.allocation }} %
                    <v-btn color="primary" text small @click="add_to_team(item, avl)">+ Team</v-btn></v-col
                  >
                </v-row>
              </v-timeline-item>
            </v-timeline>
          </div>
        </template>
      </ViewList>
    </div>
  </div>
</template>

<script>
import FormGenerator from '@/components/Forms/FormGenerator.vue'
import Section from '@/components/Helpers/Section.vue'
import ViewList from '@/components/DataTable/ViewList.vue'
import Team from '@/components/AutoComplete/Team.vue'
import Resources from '@/components/Project/Resources.vue'
import BaseButton from '@/components/Button/BaseButton.vue'

import { Setup } from '@/mixins/Setup'
import { bus } from '@/main'
import { Project } from '@/mixins/Project'

export default {
  components: {
    FormGenerator,
    Section,
    ViewList,
    Team,
    Resources,
    BaseButton
  },
  mixins: [Setup, Project],

  data() {
    return {
      form: [{}],
      field: {
        value: null,
      },
      search_method: true,
      selected_resource: [],
    }
  },
  mounted() {
    this.get_form()
    this.call_resource_search()
  },
//   created() {
//     bus.$on('add_resource_to_team', (value, options, value2) => {
//       console.log(options.ResourceConfirmation_Props)
//       // this.add_resource_to_team()
//       this.PROJECT_API_PROJECT_POST({
//         custom_action: this.$route.params.pid + '/add_resource',
//         data: options.ResourceConfirmation_Props,
//         not_execute_extract: true,
//       }).then(data => {
//         this.$store.dispatch('Snackbar', {
//           bar: true,
//           color: 'green',
//           text: data.data,
//         })
//         this.$refs.resources.get_resources()
//       })
//     })
//   },
  destroyed() {
    bus.$off('add_resource_to_team')
  },
  methods: {
    add_multiple_resource_to_team(resources){
      var avl = []
      for (var resoure of resources){
        console.log(resoure)
        var temp = resoure.availability[0]
        temp['role'] = resoure.role
        temp['emp_id'] = resoure.emp_id
        temp['team_name'] = this.$refs.team.search
        temp['team'] = this.field.value
        avl.push(temp)
      }
      if (this.field.value) {
        this.$store.dispatch('OpenConfirmationDialogOnClick', {
          Dialog: true,
          Title: `Adding Resource To Team - ${this.$refs.team.search}`,
          SubmitButton: {
            title: 'Add To Team',
            text: true,
            color: 'success',
            click: 'CloseConfirmationDialog',
            options: {
              on_success: {
                bus_emit: 'add_resource_to_team',
              },
              is_component: 'ResourceConfirmation',
              ResourceConfirmation_Props: avl,
            },
          },
        })
      }
      // If Team Not selected
      else {
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'red',
          text: 'Please select Team',
        })
      }
       
    },
    add_to_team(item , avl) {
      if (this.field.value) {
        avl['role'] = item.role
        avl['emp_id'] = item.emp_id
        avl['team_name'] = this.$refs.team.search
        avl['team'] = this.field.value
        this.$store.dispatch('OpenConfirmationDialogOnClick', {
          Dialog: true,
          Title: `Adding Resource To Team - ${this.$refs.team.search}`,
          SubmitButton: {
            title: 'Add To Team',
            text: true,
            color: 'success',
            click: 'CloseConfirmationDialog',
            options: {
              on_success: {
                bus_emit: 'add_resource_to_team',
              },
              is_component: 'ResourceConfirmation',
              ResourceConfirmation_Props: [avl],
            },
          },
        })
      }
      // If Team Not selected
      else {
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'red',
          text: 'Please select Team',
        })
      }
    },
    get_form() {
      this.loading = true
      this.SETUP_API_FORMMODEL_GET('get_form/?form_name=' + 'ResourceSearch' + '&pid=' + this.$route.params.pid).then(
        data => {
          this.form = data.data
          // this.loading = false
        },
      )
    },
    item_clicked(item) {
      // if(item.availability.length >1){
      //   alert("Multiple Availability Found")
      // }
      // else{
        this.selected_resource = item
      // }
    },
    call_resource_search(value) {
      if (this.$refs.form.form_validation()) {
        var query_params = '?search_type=available'

        for (var query of this.$refs.form.Form) {
          if (query.value) {
            query_params += '&' + query.dbfield + '=' + query.value
          }
        }
        console.log('query_params', query_params)
        this.$refs.search_result.get_list({ view: query_params }, query_params)
      } else {
        console.log('Else block')
      }
    },
  },
}
</script>

<style>

</style>