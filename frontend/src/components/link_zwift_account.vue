<template>
  <v-dialog
    v-model="zwift_link_modal_model"
    transition="dialog-top-transition"
    max-width="600"
  >
    <template v-slot:default="dialog">
      <v-card :disabled="loader">
        <v-toolbar color="primary" dark>Link Zwift Profile</v-toolbar>
        <v-card-text class="mt-2">
          <v-form ref="form">
            <v-text-field
              dense
              outlined
              v-model="email"
              :rules="[required, emailValidator]"
              label="Zwift Email"
            ></v-text-field>
            <v-text-field
              dense
              type="password"
              v-model="password"
              outlined
              label="Zwift Password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn text @click="dialog.value = false">Close</v-btn>
          <v-btn text color="success" :loading="loader" @click="link_account">Link </v-btn>
        </v-card-actions>
      </v-card>
    </template>
  </v-dialog>
</template>

<script>
import { Index } from "@/mixins/index";
import { required, emailValidator } from "@/utils/validation";

export default {
  mixins: [Index],
  data() {
    return {
      email: "",
      password: "",
      required,
      emailValidator,
      loader: false,
      //     validators: {
      //     required,
      //     emailValidator,
      //     passwordValidator,
      //     alphaValidator,
      //     confirmedValidator,
      //   }
    };
  },
  methods: {
    link_account() {
      this.loader = true;
      if (this.$refs.form.validate()) {
        this.link_zwifit({ user_id: this.email, user_password: this.password })
          .then(() => {
            this.loader = false;
            this.zwift_link_modal(false)
            this.get_profile()
          })
          .catch(() => {
            this.loader = false;
          });
      }
    },
  },
};
</script>

<style>
</style>