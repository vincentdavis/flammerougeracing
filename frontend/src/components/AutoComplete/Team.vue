<template>
<v-autocomplete
    chip
    color="primary"
    :prefix="prefix"
    :search-input.sync="search"
    :items="ComputedTeamItems"
    v-model="ComputedTeams"
    :auto-select-first="auto_select_first"
    :item-text="itemtext"
    :item-value="itemvalue"
    :rules="rules"
    dense
    :clearable="clearable"
    :loading="isLoading"
    :placehoder="placehoder"
    :label="label"
    :menu-props="{ closeOnContentClick: true }"
    :readonly="readonly"
  >
    <template v-slot:no-data v-if="label == 'Team'">
      <v-list-item @click="$store.dispatch('OpenDialogOnClick', 
            {
                Dialog: true,
                Title: 'Add New Team',
                RefName: 'NewTeam_Ref',
                DialogEditType: 'new',
                FormName: 'NewTeam',
                DialogMutation: 'mutation__dialog',
                DialogExtraParam: `&project_details=${$route.params.pid}&team_name=${search}`,
                SubmitButton: { title: 'Add', text: true, color: 'success', click: 'TeamResourceStore/TeamNameCreate' },
            })"
        >
            <v-list-item-title>No results matching "<strong>{{ search }}</strong>". Click <kbd>here</kbd> to create a new one</v-list-item-title>
        </v-list-item>
    </template>
    <template v-slot:label> {{ label }} <span style="color: red" v-if="field && field.required">*</span> </template>
</v-autocomplete>
  
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'
import CustomerView from '@/components/Helpers/CustomerView.vue'
// Mixins
import { TeamResource } from '@/mixins/TeamResource'
export default {
  mixins: [TeamResource],
  components: {
    BaseButton,
    CustomerView
  },
  props: {
    label: { type: String },
    field: { default: {} },
    rows: { default: 5 },
    rowheight: { default: 20 },
    prependicon: { default: '' },
    appendicon: { default: '' },
    prependinnericon: { default: '' },
    appendoutericon: { default: '' },
    dropdownitems: [],
    placehoder: { default: '' },
    prefix: { default: '' },
    itemtext: '',
    itemvalue: '',
    mode: '',
    readonly: {default : false},
    clearable: {default : true},
    auto_select_first: {default : true}
  },
  data() {
    return {
      search: '',
      isLoading: false,
    }
  },
  mounted() {
    try {
      this.SetTeamList(this.field.valuelist)
      this.GET_TeamNameDetails('?project_details='+ this.$route.params.pid)
      .then(() => {
        this.isLoading = false
      })
      .catch(() => {
        this.isLoading = false
      })
    } catch (err) {
      console.error(err)
    }
  },
  watch: {
    search(val) {
      // Items have already been requested
      if (this.isLoading) return
      this.isLoading = true
      if (val && !this.ComputedTeams) {
        this.GET_TeamNameDetails('?project_details='+ this.$route.params.pid+'&search=' + val)
          .then(() => {
            this.isLoading = false
          })
          .catch(() => {
            this.isLoading = false
          })
      } else {
        this.isLoading = false
      }
    },
  },
  computed: {
    rules() {
      var data = []
      if (this.field && this.field.required) {
        data.push(v => !!v || this.field.name + ' is required')
      } else {
        data = []
      }
      return data
    },
  },

  methods: {},
}
</script>

<style>
</style>