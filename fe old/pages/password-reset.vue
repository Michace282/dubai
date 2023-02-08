<template>
  <v-container>
    <v-layout row>
      <v-flex xs12 sm8 offset-sm2>
        <v-card>
          <v-card-text>
            <v-container>
              <form @submit.prevent="onRestorePassword">
                <v-layout row>
                  <v-flex xs-12>
                    <input name="email" type="text" id="email" placeholder="email">
                  </v-flex>
                </v-layout>
                <v-layout row>
                  <v-flex xs-12>
                    <button type="submit">
        Restore
      </button>
                  
                  </v-flex>
                </v-layout>
              </form>
            </v-container>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import Alert from '@/components/Shared/Alerts/Error'

  export default {
    components: {
      Alert
    },
    data () {
      return {
        email: '',
        errors: {
          email: []
        },
        rules: {
          required: (value) => !!value || 'Required.'
        }
      }
    },
    computed: {
      error () {
        return this.$store.getters.error
      },
      loading () {
        return this.$store.getters.loading
      }
    },
    watch: {
      error (values) {
        if (values !== null) {
          for (let value in values.response.data) {
            this.errors[value] = values.response.data[value]
          }
        }
      }
    },
    methods: {
      onRestorePassword () {
        this.$store.dispatch('restorePassword', {
          email: this.email
        })
      },
      onDismissed () {
        this.$store.dispatch('clearError')
      }
    }
  }
</script>
