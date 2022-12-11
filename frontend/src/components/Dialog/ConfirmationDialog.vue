<template>
  <div>
    <div>
      <v-dialog v-model="$store.state.ConfirmationDialog.Dialog" max-width="500" persistent>
        <v-card>
          <v-card-title class="text-h5">{{ $store.state.ConfirmationDialog.Title ? $store.state.ConfirmationDialog.Title: 'Confirmation'  }}</v-card-title>
          <v-card-text>
            {{ $store.state.ConfirmationDialog.Body }}
             <components :is="$store.state.ConfirmationDialog.SubmitButton.options.is_component"
             :props="$store.state.ConfirmationDialog.SubmitButton.options.ResourceConfirmation_Props"
              ></components>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <template>
              <Button :text="true" color="default" title="Close" click="CloseConfirmationDialog" :options="{}" />
              <Button
                @success="success"
                :text="$store.state.ConfirmationDialog.SubmitButton.text"
                :color="$store.state.ConfirmationDialog.SubmitButton.color"
                :title="$store.state.ConfirmationDialog.SubmitButton.title"
                :click="$store.state.ConfirmationDialog.SubmitButton.click"
                :options="$store.state.ConfirmationDialog.SubmitButton.options"
              />&nbsp;&nbsp;&nbsp;
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
import ResourceConfirmation from '@/components/Project/ResourceConfirmation.vue'

import { status_color } from '@/helper'
import { bus } from '@/main'

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
    ResourceConfirmation
  },
  data: () => ({
    form: false,
  }),
  methods: {
    success(click, options, api_response) {
      this.$store.dispatch('CloseConfirmationDialog')
      console.log('-->', click)
      console.log('-->', options)
      if (options && options.on_success && options.on_success.bus_emit) {
        bus.$emit(options.on_success.bus_emit, api_response, options)
      } else if (options && options.on_success && options.on_success.route) {
        this.$router.push(options.on_success.route)
      } else {
        bus.$emit('form_success', api_response, '')
      }
      // this.$router.push({ name: 'Project' })

      // bus.$emit('form_success', data, this.$store.state['ConfirmationDialog'].DrawerFormType, this.$store.state[''].DrawerActionType)
    },
  },
}
</script>

<style>
</style>
