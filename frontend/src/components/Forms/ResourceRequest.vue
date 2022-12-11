<template>
  <div>
    <div class="ma-4">
      <v-form :disabled="disabled" ref="NewResourceRequest_Ref" v-model="form">
        <v-row>
          <template v-for="(field, key) in $store.state.Drawer.DrawerForm">
            <v-col
              cols="12"
              v-if="
                field.conditionfield
                  ? $store.state.Drawer.DrawerForm.filter(obj => {
                      return obj.dbfield == field.conditionfield && obj.value == field.conditionvalue
                    }).length == 1
                  : true
              "
              :sm="field.sm"
              v-bind:key="key"
            >
              <components
                :label="field.name"
                :rules="field.rules"
                :readonly="field.readonly"
                :disabled="field.disabled"
                :is="field.fieldtype"
                :error_message="field.error_message"
                :maxdate="
                  field.maxdate_field
                    ? $store.state.Drawer.DrawerForm.filter(obj => {
                        return obj.dbfield == field.maxdate_field && obj.fieldtype == 'DateField'
                      })[0].value
                    : field.maxdate
                "
                :mindate="
                  field.mindate_field
                    ? $store.state.Drawer.DrawerForm.filter(obj => {
                        return obj.dbfield == field.mindate_field && obj.fieldtype == 'DateField'
                      })[0].value
                    : field.mindate
                "
                :field="field"
                :itemtext="field.itemtext"
                :itemvalue="field.itemvalue"
                :dropdownitems="field.valuelist"
                :type="field.type"
                :prependicon="field.prependicon"
                :prependinnericon="field.prependinnericon"
              >
              </components>
            </v-col>
          </template>
        </v-row>
        <v-row v-if="$store.state.Drawer.DrawerForm.length >= 1">
          <Button v-if="$store.state.Drawer.DrawerActionType == 'new'"
            :disabled="disabled"
            title="Add"
            click="TeamResourceStore/ResourceRequest_API_POST"
            @success="success"
            :options="{
              refs: $refs,
              validate_form: true,
              validate_form_name: 'NewResourceRequest_Ref',
              data: $store.state.Drawer.DrawerForm,
            }"
          />&nbsp;&nbsp;&nbsp;
          <Button v-if="$store.state.Drawer.DrawerActionType == 'edit'"
            :disabled="disabled"
            title="Update"
            click="TeamResourceStore/ResourceRequest_API_POST"
            @success="Editsuccess"
            :options="{
              refs: $refs,
              validate_form: true,
              validate_form_name: 'EditResourceRequest_Ref',
              data: $store.state.Drawer.DrawerForm,
              custom_action: `${$store.state.Drawer.DrawerForm.filter(obj => { return obj.dbfield == 'project_details'})[0].value}/`,
            }"
          />&nbsp;&nbsp;&nbsp;
          <Button :disabled="disabled" color="error" title="Cancel" click="CloseDrawer" :options="{}" />
        </v-row>
      </v-form>
    </div>
  </div>
</template>

<script>
import TextField from '@/components/TextField/TextField.vue'
import DateField from '@/components/DateTimeField/DateField.vue'
import TextArea from '@/components/TextField/TextArea.vue'
import AutoComplete from '@/components/DropDown/AutoComplete.vue'
import Button from '@/components/Button/BaseButton.vue'
import CostCenter from '@/components/AutoComplete/CostCenter.vue'
import Customer from '@/components/AutoComplete/Customer.vue'
import Team from '@/components/AutoComplete/Team.vue'
import { status_color } from '@/helper'
import { bus } from '@/main';

export default {
  props: {
    disabled: { default: false },
  },
  components: {
    TextField,
    DateField,
    TextArea,
    AutoComplete,
    Button,
    CostCenter,
    Customer,
    Team,
  },
  data: () => ({
    form: false,
  }),
  methods: {
    success(click, api_response) {
      this.$store.dispatch('Snackbar', {
        bar: true,
        color: status_color(api_response.status),
        text: 'Resource Request Added Successfully',
      })
      this.$store.dispatch('CloseDrawer')
      // Refresh Project Table

    },
    Editsuccess(click, api_response) {
      this.$store.dispatch('Snackbar', {
        bar: true,
        color: status_color(api_response.status),
        text: 'Resource Request Updated Successfully',
      })
      this.$store.dispatch('CloseDrawer')
      // Refresh Project Table

    },
  },
}
</script>

<style>
</style>
