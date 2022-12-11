<template>
  <v-autocomplete
    chip
    color="primary"
    :prefix="prefix"
    :search-input.sync="search"
    :items="ComputedCustomersItems"
    v-model="ComputedCustomers"
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
    <template v-slot:no-data v-if="label == 'Customer'">
      <v-list-item
        @click="
          $store.dispatch('OpenDrawerOnClick', {
          ShowAppBarOnDrawer: true,
            DrawerSize: '35%',
            DrawerFormType: 'NewCustomer',
            DrawerExtraParam: '&name=' + search,
            DrawerFormAPICall: true,
            DrawerMutation: 'mutation__second_drawer',
            DrawerFormSubmit: {
              btn_name: 'Create Customer',
              store_action_name: 'CustomerStore/CustomerCreate',
            },
          })
        "
      >
        <v-list-item-title>
          No results matching "<strong>{{ search }}</strong
          >". Click <kbd>here</kbd> to create a new one
        </v-list-item-title>
      </v-list-item>
    </template>
    <template v-slot:label> {{ label }} <span style="color: red" v-if="field && field.required">*</span> </template>
    <template v-if="mode == 'view'" v-slot:selection="data">
      <CustomerView :customer="data.item"> </CustomerView>
    </template>
  </v-autocomplete>
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'
import CustomerView from '@/components/Helpers/CustomerView.vue'
import { bus } from '@/main'

// Mixins
import { Customer } from '@/mixins/Customer'
export default {
  mixins: [Customer],
  components: {
    BaseButton,
    CustomerView,
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
    readonly: { default: false },
    clearable: { default: true },
  },
  data() {
    return {
      search: '',
      isLoading: false,
    }
  },
  mounted() {
    try {
      this.SetCustomerList(this.field.valuelist)
    } catch (err) {
      console.error(err)
    }
  },

  created() {
    console.log("I AM HERE<,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    bus.$on('customer_form_success', (response, form_name, form_type=null) => {
      console.log(response)
      console.log(form_name)
      if (form_name == 'NewCustomer') {
        this.$store.dispatch('CloseSecondDrawer')
        this.$store.dispatch('CustomerStore/API_CUSTOMER', '?id=' + response.data.id)
        this.$store.state.Drawer.DrawerForm.filter(obj => {
          return obj.name == 'Customer'
        })[0].value = response.data.id
        this.$store.dispatch('DisableDrawerLoader')
      }
    })
  },
  watch: {
    search(val) {
      // Items have already been requested
      if (this.isLoading) return
      this.isLoading = true
      if (val && !this.ComputedCustomers) {
        this.API_CUSTOMER('?search=' + val)
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
