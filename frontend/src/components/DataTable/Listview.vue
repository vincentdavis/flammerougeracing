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
    <template v-slot:[`header.data-table-select`]="{ }">
      <TableColoumnConfig @header_list="set_header" :FieldList="headers"> </TableColoumnConfig>
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
        var query_param = ''
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
      } catch (_) {
        console.error(_)
      }

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
        color: 'blue',
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