<template>
  <v-card
    :loading="loading"
    class="mt-2"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      src="@/assets/Eventflyer.png"
    ></v-img>


    <v-card-text>
      <v-list >
      <template v-for="(item, index) in items">
        <v-subheader
          v-if="item.header"
          :key="item.header"
          v-text="item.header"
        ></v-subheader>

        <v-divider
          v-else-if="item.divider"
          :key="index"
          :inset="item.inset"
        ></v-divider>

        <v-list-item
          v-else
          :key="item.title"
        >
          

          <v-list-item-content>
            <v-list-item-title v-html="item.title"></v-list-item-title>
            <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>

      

    </v-card-text>


    <v-card-text>
      
    </v-card-text>

    
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      loading: false,
      selection: 1,

      items: [
        { header: 'Tour Schedule' },
        {
          title: 'Tour France',
          subtitle: ` Oct 22 to 30 Completed`,
        },
        {
          title: 'Tour Britannia',
          subtitle: ` Nov 26 to Dec 4`,
        },
        {
          title: 'Tour Watopia',
          subtitle: ` Jan 2 to 8th`,
        },
        {
          title: 'World Tour',
          subtitle: `March dates tbc - 2 weeks 14 Stages`,
        },
        { header: 'FRR World Championship' },
        {
          title: '1 Event',
          subtitle: ` 2 Stages - Back to Back`,
        },
        {
          title: 'Combined Stage time',
          subtitle: `Winner in each FRHC Class`,
        },
        {
          title: '7 Rider (FRHC)',
          subtitle: ``,
        },

      ]
    }),

    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
    },
  }
</script>