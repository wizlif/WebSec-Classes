<template>
  <v-row no-gutters align-content="center" justify="center" style="height: 100vh">
    <v-col cols="12" md="4">
      <v-card>
        <v-card-title>Sign In
          <v-spacer/>
          <v-btn
              large
              color="secondary"
              class="text-capitalize pa-3"
              rounded
              @click="signUp">Sign Up
          </v-btn>
        </v-card-title>
        <v-divider/>
        <v-card-text class="pa-12">
          <v-row no-gutters align="center">
            <v-col cols="12" sm="12">
              <v-form ref="form" v-model="sign_in.valid">
                <span>Email Address</span>
                <v-text-field class="mt-3" outlined placeholder="Email" v-model="sign_in.email" :rules="rules.email"/>
                <span>Password</span>
                <v-text-field
                    v-model="sign_in.password"
                    class="mt-3"
                    outlined
                    type="password"
                    placeholder="Password"
                />

                <v-btn
                    x-large
                    depressed
                    block
                    color="primary"
                    class="text-capitalize"
                    :loading="loading"
                    @click="signIn"
                >Sign In
                </v-btn
                >
              </v-form>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import validationMixin from "../mixins/validations";

export default {
  name: "sign-in",
  mixins: [validationMixin],
  data: () => ({
    sign_in: {
      email: "",
      password: "",
      valid: false
    },
    loading: false
  }),
  methods: {
    async signIn() {
      this.$refs.form.validate();

      if (this.sign_in.valid) {
        this.loading = true;
        await this.$router.push("/home");
      }

    },

    async signUp() {
      await this.$router.push("/auth/sign-up");
    }
  }
};
</script>

<style scoped></style>