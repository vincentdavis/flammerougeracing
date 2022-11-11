<template>
  <v-data-table
    class="user-search me-3 mb-4 row-pointer"
    :headers="generate_headers"
    :loading="loader"
    :show-select="show_select"
    v-model="selected"
    @click:row="handleClick"
    :options.sync="table_pagination"
    :server-items-length="items.count"
    :items="items.results"
  >
    <template v-slot:header.data-table-select="{ on, props }">
      <TableColoumnConfig @header_list="set_header" :FieldList="headers"> </TableColoumnConfig>
    </template>

    <template v-slot:item.status="{ item }">
      <slot name="item-status" :item="item"> </slot>
    </template>
    <template v-slot:item.state="{ item }">
      <slot name="item-state" :item="item"> </slot>
    </template>
    <template v-slot:item.milestone_type="{ item }">
      <slot name="item-milestone-type" :item="item"> </slot>
    </template>
    <template v-slot:item.impacted_milestone="{ item }">
      <slot name="item-impacted-milestone" :item="item"> </slot>
    </template>
    <template v-slot:item.payment_delivery_status="{ item }">
      <slot name="item-payment-delivery-status" :item="item"> </slot>
    </template>
    <template v-slot:item.cr="{ item }">
      <slot name="item-cr" :item="item"> </slot>
    </template>
    <template v-slot:item.milestones="{ item }">
      <slot name="item-milestones" :item="item"> </slot>
    </template>
    <template v-slot:item.dependencies="{ item }">
      <slot name="item-dependencies" :item="item"> </slot>
    </template>
    <template v-slot:item.risk="{ item }">
      <slot name="item-risk" :item="item"> </slot>
    </template>
    <template v-slot:item.customer="{ item }">
      <slot name="item-customer" :item="item"> </slot>
    </template>
    <template v-slot:item.CRDetail="{ item }">
      <slot name="item-CRDetail" :item="item"> </slot>
    </template>
    <template v-slot:item.team="{ item }">
      <slot name="item-team" :item="item"> </slot>
    </template>
    <template v-slot:item.actions="{ item }">
      <slot name="item-actions" :item="item"> </slot>
    </template>
    
    <template v-slot:item.availability="{ item }">
      <slot name="item-availability" :item="item"> </slot>
    </template>
    <template v-slot:item.notification_metrix="{ item }">
      <slot name="item-notification_metrix" :item="item"> </slot>
    </template>
  </v-data-table>
</template>

<script>
// Components
import TableColoumnConfig from '@/components/DataTable/TableColoumnConfig.vue'

// Mixins
// import { Helper } from '@/mixins/Helper'
import { bus } from '@/main'

export default {
  // mixins: [Helper],
  components: {
    TableColoumnConfig,
  },
      name: 'ListView',
  props: {
    options: {
      // store_action_name
    },
    handlerow: { default: true },
    show_select: { default: true },
    type: { default: null },
  },
  data() {
    return {
      table_pagination: {},
      headers: [],
      headers_list: [],
      items: [],
      selected: [],
      loader: false,
      temp_query : ''
    }
  },
  computed: {
    generate_headers() {
      return this.headers.filter(obj => {
        return obj.is_default
      })
    },
  },
  methods: {
    handleClick(items) {
      if (this.handlerow) {
        this.generate_route(items)
      }
    },
    set_header(header) {
      this.$store.dispatch('Snackbar', {
        bar: true,
        text: 'Order Updated',
      })
      this.headers = header
    },
    get_list(value, temp_query=null) {
      if (temp_query){
              this.temp_query =  temp_query
      }
      this.loader = true
      var query = ''
      if (this.$route.params.pid) {
        query = this.$route.params.pid
      } else if (this.$route.params.pid) {
        query = this.$route.params.pid
      }
      var query_param = '?project_details=' + query
      try {
        // Views
        if (value && value.view) {
          query_param += value.view
        }
        console.log(this.temp_query)
        // Views
        if (this.temp_query) {
          query_param += this.temp_query
        }

        // Sort By Query Generation
        if (value && value.sortBy && value.sortBy.length >= 1) {
          for (var [i, v] of value.sortBy.entries()) {
            if (value.sortDesc[i]) {
              query_param += '&ordering=-' + v + '&'
            } else {
              query_param += '&ordering=' + v + '&'
            }
          }
        } else {
          query_param += '&ordering=-submitted_date&'
        }
      } catch (err) {
        console.error(err)
      }

      // Pagination
      try {
        query_param += '&page=' + (value.page ? value.page : 1)
      } catch (_) {}

      //  API Call
      this.$store
        .dispatch(this.options.store_action_name, {api: this.options.api, query_params: query_param})
        .then(data => {
          this.headers = data.data.columns
          this.items = data.data
          this.loader = false
          bus.$emit('header_emit', data.data)
        })
        .catch(err => {
          console.error(err)
          this.loader = false
        })
    },
    resourcerequestsuccess(click, response) {
      this.$store.dispatch('Snackbar', {
        bar: true,
        color: status_color(response.status),
        text: 'Resource Request #' + response.data.id + ' Updated ...',
      })
      this.$store.dispatch('CloseDrawer')
    },
  },
  // mounted() {
  //   //  API to get Field values
  //   this.$store
  //     .dispatch(this.options.store_action_name, 'fields/')
  //     .then(data => {
  //       this.headers_list = data.data
  //       this.field_fetch = false
  //       this.headers = this.headers_list
  //     })
  //     .catch(err => {})
  // },
  watch: {
    table_pagination: {
      handler(value) {
        this.get_list(value)
      },
    },
    selected(values) {
      this.$emit('item-clicked', values)
    },
  },
}
</script>

<style lang="css" scoped>
.row-pointer >>> tbody tr :hover {
  cursor: pointer;
}
</style>