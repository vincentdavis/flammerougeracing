<template>
    <div>
        <div>
            <v-dialog v-model="$store.state.Dialog.Dialog" max-width="500" persistent>
                <v-card>
                    <v-card-title class="text-h5">{{ $store.state.Dialog.Title }}</v-card-title>
                    <v-card-text>
                        <br>
                        <div class="text-center" v-if="$store.state.Dialog.Loader">
                            <v-progress-circular :size="50" :width="5" color="secondary" indeterminate></v-progress-circular>
                        </div>
                        <v-form :ref="$store.state.Dialog.RefName" v-model="form">
                            <v-row>
                                <template v-for="(field, key) in $store.state.Dialog.DialogForm">
                                    <v-col cols="12" :sm="field.sm" v-bind:key="key">
                                        <components :label="field.name" :rules="field.rules" :readonly="field.readonly" :disabled="field.disabled"
                                         :is="field.fieldtype" :error_message="field.error_message"  :outlined="field.outlined"
                                         :maxdate="field.maxdate_field ? $store.state.Drawer.DrawerForm.filter(obj => { return obj.dbfield == field.maxdate_field && obj.fieldtype == 'DateField' })[0].value : field.maxdate"
                                         :mindate="field.mindate_field ? $store.state.Drawer.DrawerForm.filter(obj => { return obj.dbfield == field.mindate_field && obj.fieldtype == 'DateField' })[0].value : field.mindate"
                                         :field="field" :itemtext="field.itemtext" :itemvalue="field.itemvalue" :dropdownitems="field.valuelist" :type="field.type">
                                        </components>
                                    </v-col>
                                </template>
                            </v-row>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <template v-if="$store.state.Dialog.DialogForm.length > 0">
                            <Button  :text="true" color="default" title="Close" click="CloseDialog" :options="{}" />
                            <Button @success="success" :text="$store.state.Dialog.SubmitButton.text" :color="$store.state.Dialog.SubmitButton.color" :title="$store.state.Dialog.SubmitButton.title" :click="$store.state.Dialog.SubmitButton.click" 
                                :options="{ refs: $refs, validate_form: true, validate_form_name: $store.state.Dialog.RefName, data: $store.state.Dialog.DialogForm, custom_action:$store.state.Dialog.SubmitButton.custom_action }"/>&nbsp;&nbsp;&nbsp;
                        </template>
                    </v-card-actions>
                </v-card>
            </v-dialog>
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
import Users from '@/components/AutoComplete/Users.vue'

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
    Users
  },
  data: () => ({
    form: false,
  }),
  methods: {
    success(click, api_response) {
        if (api_response && api_response.data && api_response.data.App && api_response.data.App =='Team'){
            this.$store.dispatch('CloseDialog')
            this.$store.dispatch('TeamResourceStore/GET_TeamNameDetails', '?id='+api_response.data.id)
            this.$store.state.Drawer.DrawerForm.filter(obj => { return obj.name == 'Team'})[0].value = api_response.data.id
            this.$store.dispatch('Snackbar', {
                bar: true,
                color: status_color(api_response.status),
                text: 'Team ' + api_response.data.team_name + ' Added',
            })
            this.$store.dispatch('DisableDrawerLoader')
        }else {
            this.$store.dispatch('CloseDialog')
            this.$store.dispatch('Snackbar', {
                bar: true,
                color: status_color(api_response.status),
                text: 'Project ' + api_response.data.name + ' Approved Successfully ...',
            })
            this.$router.push({ name: 'Project' })
        }
    },
  },
}
</script>

<style>
</style>
