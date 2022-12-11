<template>
  <div class="text-center">
    <v-dialog v-model="dialog" hide-overlay persistent width="300">
      <v-card :loading="true">
        <v-img src="@/assets/images/FRR.png"></v-img>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: true,
    }
  },
  mounted() {
    setTimeout(() => {
        this.dialog = false
        this.$router.push({name: 'home'})
    }, 3000)
  },
}
</script>