<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" /></a>
            <base-title title="Sign up" />
            <socials-auth class="mt-30" />
            <base-input
                class="mt-45"
                :class="{ error: $v.email.$error }"
                v-model="$v.email.$model"
                label="e-mail"
                name="email"
                :error="!$v.email.email ? 'Enter the correct email' : ''"
            />
            <base-input
                class="mt-30"
                :class="{ error: $v.pass.$error }"
                v-model="$v.pass.$model"
                label="Password"
                name="pass"
                type="password"
                :error="!$v.pass.minLength ? 'Eenter a combination of at least six numbers' : ''"
            />
            <base-input
                class="mt-30"
                :class="{ error: $v.pass2.$error }"
                v-model="$v.pass2.$model"
                label="repeat Password"
                name="pass2"
                type="password"
                :error="!$v.pass2.sameAsPassword ? 'passwords dont match' : ''"
            />
            <div class="text-right mt-30">
                <button class="btn btn-black" @click="signUp">Sign up</button>
                <a href.prevent class="link underline mt-45 d-block" @click="$emit('showAuthModal')"
                    >Already have an account? Log in</a
                >
            </div>
        </div>
    </div>
</template>
<script>
    import BaseInput from '../fields/BaseInput.vue';
    import SocialsAuth from './SocialsAuth.vue';
    import { required, email, sameAs, minLength } from 'vuelidate/lib/validators';
    export default {
        components: { SocialsAuth, BaseInput },
        name: 'RegForm',
        data() {
            return {
                email: '',
                pass: '',
                pass2: '',
            };
        },
        validations: {
            email: {
                required,
                email,
            },
            pass: {
                required,
                minLength: minLength(6),
            },
            pass2: {
                required,
                sameAsPassword: sameAs('pass'),
            },
        },
        methods: {
            signUp() {
                this.$v.$touch();
                if (!this.$v.$error) {
                    this.$apollo
                        .mutate({
                            mutation: require('~/graphql/mutations/user/registration.graphql'),
                            variables: {
                                name: this.email,
                                email: this.email,
                                password: this.pass,
                                passwordRepeat: this.pass2,
                                guestUuid: this.$store.state.user.guestUuid,
                            },
                        })
                        .then((data) => {
                            console.log(data);
                            if (data && data.data.registration && data.data.registration.errors.length > 0) {
                                this.$bvToast.toast(data.data.registration.errors[0].messages, {
                                    title: 'Sign up',
                                    variant: 'danger',
                                });
                            } else {
                                this.$apollo
                                    .mutate({
                                        mutation: require('~/graphql/mutations/user/tokenAuth.graphql'),
                                        variables: {
                                            username: this.email,
                                            password: this.pass,
                                        },
                                    })
                                    .then((data) => {
                                        console.log(data);
                                    });
                            }
                        });
                }
            },
        },
    };
</script>
<style lang="less" scoped>
    .btn-black {
        padding: 8px 51px;
    }
</style>
