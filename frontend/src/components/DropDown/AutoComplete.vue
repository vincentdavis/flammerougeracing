<template>
  <v-autocomplete
    color="primary"
    v-model="field.value"
    :item-text="itemtext"
    :item-value="itemvalue"
    :rules="rules"
    hide-details="auto"
    dense
    :items="dropdownitems"
    :placehoder="placehoder"
    :label="label"
    :outlined="outlined"
    :clearable="clearable"
  >
    <template v-slot:label> {{ label }} <span style="color: red" v-if="field && field.required">*</span> </template>
  </v-autocomplete>
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'
export default {
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
    outlined: { default: false },
    clearable: { default: false },
  },

  computed: {
    rules() {
      var data = []
      if (this.field && this.field.required) {
        data.push(v => (!!v || v == 0) || this.field.name + ' is required')
      } else {
        data = []
      }
      return data
    },
  },

  watch: {},

  methods: {},
}
</script>

<style>
</style>