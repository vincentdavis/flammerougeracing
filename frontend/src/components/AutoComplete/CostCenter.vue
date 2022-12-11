<template>
    <v-autocomplete
    color="primary"
    :search-input.sync="search"
    :loading="isLoading"
    :items="ComputedCostCenterItems"
    v-model="ComputedCostCenter"
    :item-text="itemtext"
    :item-value="itemvalue"
    :rules="rules"
    dense
    clearable
    :placehoder="placehoder"
    :label="label"
  >
  <template v-slot:label>
           {{label}} <span style="color:red" v-if="field && field.required ">*</span>
        </template>
  </v-autocomplete>
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'

// Mixins
import { CostCenter } from '@/mixins/CostCenter'
export default {
  mixins: [CostCenter],
  components: {
    BaseButton,
  },
  props: {
    label: { required: true, type: String },
    field: { default: {} },
    rows: { default: 5 },
    rowheight: { default: 20 },
    prependicon: { default: '' },
    appendicon: { default: '' },
    prependinnericon: { default: '' },
    appendoutericon: { default: '' },
    dropdownitems: [],
    placehoder: { default: '' },
    itemtext: '',
    itemvalue: '',
    loading: false,
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
  mounted() {
    try {
      this.SetCostCenterList(this.field.valuelist)
    } catch (err) {
      console.error(err)
    }
  },
    data() {
    return {
      search: '',
      isLoading: false,
    }
  },
  watch: {
    field: {
      handler(value) {
        if (value && value.name == 'Cost Center') {
          this.$store.state.Drawer.DrawerForm.filter(obj => {
            return obj.name == 'Department'
          })[0].value = value.valuelist.filter(obj => {
            return obj.id == value.value
          })[0].name
        }
      },
      deep: true,
    },
    search(val) {
      // Items have already been requested
      if (this.isLoading) return
      this.isLoading = true
      if (val && !this.ComputedCostCenter) {
        this.API_COSTCENTER('?search=' + val)
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

  methods: {},
}
</script>

<style>
</style>