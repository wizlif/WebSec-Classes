<template>
  <v-row align-content="center" justify="center" no-gutters style="height: 100vh">
    <v-col cols="12" md="4">
      <v-card>
        <v-card-title>Sign Up</v-card-title>
        <v-divider/>
        <v-card-text>
          <v-row>
            <v-col cols="12" sm="12">
              <v-form v-model="valid" :lazy-validation="false" ref="form">
                <span>Email Address</span>
                <v-text-field
                    v-model="email"
                    :rules="rules.email"
                    validate-on-blur
                    class="mt-3"
                    outlined
                    placeholder="Email"
                ></v-text-field>
                <span>Password</span>
                <v-text-field
                    v-model="password"
                    :rules="rules.password"
                    validate-on-blur
                    type="password"
                    class="mt-3"
                    outlined
                    placeholder="Password"
                ></v-text-field>
                <span>Confirm Password</span>
                <v-text-field
                    v-model="confirm_password"
                    :rules="confirmPasswordRules"
                    validate-on-blur
                    type="password"
                    class="mt-3"
                    outlined
                    placeholder="Password"
                ></v-text-field>

                <v-btn
                    @click="signUpWithEmail"
                    :loading="loading"
                    rounded
                    x-large
                    depressed
                    block
                    color="primary"
                    class="text-capitalize"
                >Sign Up
                </v-btn
                >

                <v-row align="center" class="my-6">
                  <v-divider class="mr-5"></v-divider>
                  Already have an account ?
                  <v-divider class="ml-5"></v-divider>
                </v-row>

                <v-btn
                    rounded
                    x-large
                    depressed
                    block
                    color="primary"
                    outlined
                    class="text-capitalize mb-12"
                    @click="$router.push({ name: 'sign-in' })"
                >
                  Sign In
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
import validation_mixins from "../mixins/validations";
import axios from "axios";

export default {
  name: "sign-up",
  mixins: [validation_mixins],
  components: {},
  data() {
    return {
      valid: false,
      username: "",
      password: "",
      confirm_password: "",
      email: "",
      loading: false
    };
  },
  computed: {
    confirmPasswordRules: function () {
      return [
        v => !!v || "Password Confirmation required",
        v => v === this.password || "Passwords do not match."
      ];
    }
  },
  methods: {
    async signUpWithEmail() {
      this.$refs.form.validate();

      if (this.valid) {
        this.loading = true;
        try {
          const {data: result} = await axios.post('https://3179-154-230-147-236.ngrok.io/sign-up', {
            email: this.email,
            password: this.password
          });

          console.log(result);
          await this.$router.push('/home');
        } catch (e) {
          // TODO - Show Error
          console.log(e);
        } finally {
          this.loading = false;
        }

      }
    }
  }
};
</script>

<style scoped></style>