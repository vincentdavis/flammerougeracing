<template>
    <div>
        <div>
            <v-row>
                <template v-for="(field, key) in field_mapping">
                    <v-col v-bind:key="key" v-if="project_detail[field.value]" cols="12" sm="6">
                        <Customer prefix="Customer:" mode='view' readonly :clearable="false" v-if="field.value == 'customer'" 
                            :field="{valuelist: [project_detail[field.value]] , value: project_detail[field.value].id}"
                            itemtext="name" itemvalue="id"></Customer>
                        <v-text-field v-else readonly dense hide-details :value="`${project_detail[field.value]} `">
                            <template v-slot:label>
                              <h3>{{field.text}}</h3>
                            </template>
                        </v-text-field>
                    </v-col>
                </template>
            </v-row>
        </div>
    </div>
</template>

<script>
import Customer from '@/components/AutoComplete/Customer.vue'

export default {
    props: {
        project_detail: { default: {} },
        field_mapping: { default: [] },
    },
    components: {
        Customer
    },
    data(){
        return {
            panel: [0],
        }
    },
}
</script>