<template>
  <div>
    <Listview
      :options="{
        store_action_name: 'API',
        api: `/api/zwift_result/?zwift_id=${zwift_id}`,
      }"
    >
    </Listview>
  </div>
</template>

<script>
import { Index } from "@/mixins/index";
import Listview from "@/components/DataTable/Listview.vue";
export default {
  mixins: [Index],
  components: {
    Listview,
  },
  props: {
    zwift_id: {}
  },
  name: "race-resulr",
  data() {
    return {
     
    };
  },
  mounted() {
  },
  methods: {
    
  },
};
</script>


<style>
</style>

