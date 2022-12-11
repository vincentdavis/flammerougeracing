<template>
  <v-card>
    <v-card-title>
      <v-icon color="primary">mdi-drag</v-icon>
      Allocated Resource
      <v-spacer></v-spacer>
      <div>
        <!-- Refresh -->
        <v-btn icon small>
          <v-icon size="20" @click="$refs.ResourceList.get_list()"> mdi-refresh </v-icon>
        </v-btn>

        <!-- Slot: After Actions -->
        <slot name="after-actions"></slot>
      </div>
    </v-card-title>
    <v-card-text>
      <ViewList
        :handlerow="false"
        ref="ResourceList"
        :options="{
          store_action_name: 'ResourceStore/Resource_API',
        }"
      >
        <template #item-team="{ item }">
          <v-chip small>{{ item.team }}</v-chip>
        </template>
      </ViewList>
    </v-card-text>
  </v-card>
</template>

<script>
import ViewList from '@/components/DataTable/ViewList.vue'

export default {
  components: {
    ViewList,
  },
}
</script>

<style>
</style>