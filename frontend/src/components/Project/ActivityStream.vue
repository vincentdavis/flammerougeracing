<template>
  <div style="max-width: 600px ma-2">
    <v-timeline class="ma-2"  dense  v-bind:key="act" v-for="act in activity">
      <v-timeline-item color="green" small>
        <v-row justify="space-between">
          <v-col cols="7"> {{act.action_owner}} has <b>{{act.activity_state}} </b> {{act.activity}} {{act.comment}} </v-col>
          <v-col class="text-right" cols="5"> {{act.action_date}} </v-col>
        </v-row>
      </v-timeline-item>
    </v-timeline>
  </div>
</template>

<script>
import { Project } from '@/mixins/Project'

export default {
      mixins: [Project],
  props: {
    pid: {},
  },
  data: () => ({
    events: [],
    activity: [],
    input: null,
    nonce: 0,
  }),

  computed: {
    timeline() {
      return this.events.slice().reverse()
    },
  },
    mounted() {
    this.loader = true
    this.PROJECT_API_PROJECT(this.pid + '/history/')
      .then(data => {
        this.activity = data.data
        this.loader = false
      })
      .catch(err => {
        this.loader = false
        console.log(err)
      })
  },
  methods: {
    
    comment() {
      const time = new Date().toTimeString()
      this.events.push({
        id: this.nonce++,
        text: this.input,
        time: time.replace(/:\d{2}\sGMT-\d{4}\s\((.*)\)/, (match, contents, offset) => {
          return ` ${contents
            .split(' ')
            .map(v => v.charAt(0))
            .join('')}`
        }),
      })

      this.input = null
    },
  },
}
</script>