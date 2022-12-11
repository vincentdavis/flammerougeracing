<template>
 <div>
    <div class="d-flex flex-row-reverse">
        <BaseButton
        click="OpenDrawerOnClick"
        title=" Add Race Series"
        tooltip="Add Race Series"
        :options="{
          ShowAppBarOnDrawer: true,
          DrawerSize: '50%',
          DrawerFormType: 'Events',
          DrawerFormTitle: 'Add Race Series',
          DrawerFormAPICall: true,
          DrawerMutation: 'mutation__drawer',
          DrawerActionType: 'new',
          DrawerFormSubmit: {
            btn_name: 'Create Race Series',
            store_action_name: 'CREATE_EVENT',
            custom_action: 'create_race_series',
          },
        }"/>
    </div>
    <div class="mt-2">
        <v-row v-bind:key="race_series.id" v-for="race_series in RaceSeries">
            <v-col cols="12" sm="6">
                <v-card>
                    <v-card-text><div v-html="race_series.description"></div></v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" sm="6">
                <v-card>
                    <v-img :src="race_series.logo"></v-img>
                </v-card>
            </v-col>
        </v-row>
    </div>
 </div>
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'

export default {
    components: {
        BaseButton
    },
    data(){
        return {
            RaceSeries: []
        }
    },
    mounted(){
        this.get_all_races_series()
    },
    methods: {
        get_all_races_series(){
            this.$store.dispatch('LIST_EVENT')
            .then(data => {
                 console.log(data)
                 this.RaceSeries = data.data
            })
        }
    }
}
</script>

<style>

</style>