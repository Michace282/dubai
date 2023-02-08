<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" alt="exit" /></a>
            <base-title title="Sign up" />
<!--            <socials-auth class="mt-30" />-->
            
            <base-input
                class="mt-45"
                v-model="$v.firstName.$model"
                label="First Name"
                name="firstName"
            />

            <base-input
                class="mt-45"
                v-model="$v.lastName.$model"
                label="Last Name"
                name="lastName"
            />

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
                firstName: '',
                lastName: '',
                email: '',
                pass: '',
                pass2: '',
            };
        },
        validations: {
            firstName: {
                minLength: minLength(0),
            },
            lastName: {
                minLength: minLength(0),
            },
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
                let v = this;
                v.$v.$touch();
                if (!v.$v.$error) {
                    v.$apollo
                        .mutate({
                            mutation: require('~/graphql/mutations/user/registration.graphql'),
                            variables: {
                                email: v.email,
                                firstName: v.firstName,
                                lastName: v.lastName,
                                password: v.pass,
                                passwordRepeat: v.pass2,
                                guestUuid: v.$store.state.user.guestUuid,
                            },
                        })
                        .then((data) => {
                            if (data && data.data.registration && data.data.registration.errors.length > 0) {
                                v.$bvToast.toast(data.data.registration.errors[0].messages, {
                                    title: 'Sign up',
                                    variant: 'danger',
                                });
                            } else {
                                v.$cookies.set('guestUuid', null);
                                v.$store.commit('user/update_guestUuid', null);
                                const observer = v.$apollo.subscribe({
                                    query: require('~/graphql/mutations/user/tokenAuth.graphql'),
                                    variables: {
                                        username: v.email,
                                        password: v.pass,
                                    },
                                });
                                observer.subscribe({
                                    next({ data: { tokenAuth } }) {
                                        v.$apolloHelpers.onLogin(tokenAuth.token);
                                        v.$store.commit('user/update_user', tokenAuth.user);
                                        v.$emit('hide');
                                    },
                                    error(error) {
                                        v.$bvToast.toast('Сouldnt log in', {
                                            title: 'Log in',
                                            variant: 'danger',
                                        });
                                    },
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
