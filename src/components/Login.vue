<template>
  <v-dialog v-model="dialog" persistent max-width="290" v-bind:style="{ zIndex: 200 }">
    <v-card>
      <v-toolbar dark color="amber darken-0" dense flat>
        <v-toolbar-title class="black--text"><span class="title">Login</span></v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form v-model="valid">
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            outline
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            type="password"
            :rules="passwordRules"
            label="Password"
            outline
            required
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions class="pt-0">
        <v-spacer></v-spacer>
        <v-btn color="grey darken-2" flat="flat" @click.native="submit">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  data: () => ({
    dialog: false,
    resolve: null,
    reject: null,
    options: {
      width: 290,
      zIndex: 200
    },
    valid: false,
    password: '',
    passwordRules: [
      v => !!v || 'Password is required',
      v => v.length <= 99 || 'Password must be less than 99 characters'
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid'
    ]
  }),
  methods: {
    open() {
      this.dialog = true
    },
    submit() {
      axios.post('/api/v1/rest-auth/login/', {
          username: this.email,
          password: this.password,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        })
        .then(function () {
          // always executed
          this.dialog = false;
        });
    },
    cancel() {
      this.dialog = false
    }
  }
}
</script>
