<template>
  <div>
    <v-list dense subheader two-line>
      <v-list-item v-for="file in files" :key="file.id">
        <v-list-item-avatar>
          <v-icon class="grey lighten-1" dark> mdi-folder </v-icon>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="file.name"></v-list-item-title>

          <v-list-item-subtitle v-text="file.upload_date"></v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <a style="text-decoration: none;" :href="file.file" target="__blank__">
            <v-icon color="primary">mdi-download</v-icon>
          </a>
        
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import { Project } from '@/mixins/Project'

export default {
  mixins: [Project],

  props: {
    pid: {},
  },
  data() {
    return {
      files: [],
      loader: false,
    }
  },
  mounted() {
    this.loader = true
    this.PROJECT_API_PROJECT(this.pid + '/attachments/')
      .then(data => {
        this.files = data.data
        this.loader = false
      })
      .catch(err => {
        this.loader = false
        console.log(err)
      })
  },
}
</script>

<style>
</style>