<template>
  <v-autocomplete
    color="primary"
    :search-input.sync="search"
    :loading="isLoading"
    :items="ComputedUserItems"
    v-model="ComputedUsers"
    :item-text="itemtext"
    :item-value="itemvalue"
    :rules="rules"
    dense
    clearable
    :placehoder="placehoder"
    :label="label"
    :outlined="outlined"
  >
    <template v-slot:label> {{ label }} <span style="color: red" v-if="field && field.required">*</span> </template>
    <template v-slot:item="data">
      <!-- <v-list >
        <v-list-item>
          <v-list-item-avatar>
        <v-avatar color="primary" size="30">
          <span :class="`white--text ${data.item.emp_fullname.split(' ').length > 2 ? 'text-caption' : ''} `">{{
            data.item.emp_fullname
              .split(' ')
              .map(str => str[0])
              .join('')
          }}</span>
        </v-avatar>
      </v-list-item-avatar>
      <v-list-item-content class="pa-1">
        <v-list-item-title>{{ data.item.emp_fullname }} ( {{ data.item.emp_userid }} )</v-list-item-title>
        <v-list-item-subtitle> {{ data.item.emp_title }}</v-list-item-subtitle>
      </v-list-item-content>
        </v-list-item>
        
      </v-list> -->
      
       <template >
                  <!-- <v-list-item-avatar>
                    <v-avatar color="primary" size="30">
          <span :class="`white--text ${data.item.emp_fullname.split(' ').length > 2 ? 'text-caption' : ''} `">{{
            data.item.emp_fullname
              .split(' ')
              .map(str => str[0])
              .join('')
          }}</span>
        </v-avatar>
                  </v-list-item-avatar> -->
                  <v-list-item-content>
                    <v-list-item-title >{{ data.item.emp_fullname }} ( {{ data.item.emp_userid }} )</v-list-item-title>
                    <v-list-item-subtitle >{{ data.item.emp_title }}</v-list-item-subtitle>
                  </v-list-item-content>
                </template>
    </template>
  </v-autocomplete>
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'

// Mixins
import { Users } from '@/mixins/Users'
export default {
  mixins: [Users],
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
    outlined: { default: false },
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
    ComputedUsers: {
      get() {
        return this.field.value
      },
      set(newName) {
        // Setting Field
        this.field.value = newName
        return ''
      },
    },
    ComputedUserItems: {
      get() {
        return this.UsersList
      },
      set(newName) {
        return ''
      },
    },
  },
  mounted() {
    try {
      this.SetUsersList(this.field.valuelist)
    } catch (err) {
      console.error(err)
    }
  },
  data() {
    return {
      search: '',
      isLoading: false,
      UsersList: [],
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
      if (val) {
        this.API_USERS('?search=' + val)
          .then(data => {
            if (data.data.results.length != 0) {
              this.SetUsersList(data.data.results)
            }
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

  methods: {
    SetUsersList(value) {
      this.UsersList = value
    },
  },
}
</script>

<style>
</style>