<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" alt="exit" /></a>
            <base-title title="Log in" />
<!--            <socials-auth class="mt-30" />-->
            <div class="input-box">
                <base-input
                    class="mt-45"
                    :class="{ error: $v.email.$error }"
                    :error="!$v.email.email ? 'Enter the correct email' : ''"
                    v-model="$v.email.$model"
                    label="e-mail"
                    name="email"
                />
            </div>
            <div class="input-box">
                <base-input
                    class="mt-30"
                    :class="{ error: $v.pass.$error }"
                    label="Password"
                    type="password"
                    v-model="$v.pass.$model"
                    name="pass"
                />
            </div>
            <div class="text-right mt-30">
                <button class="btn btn-black" @click="logIn">Log in</button>
                <a href.prevent class="link mt-45 d-block" @click="$emit('showResetModal')">Forgot password?</a>
                <a href.prevent class="link underline mt-15 d-block" @click="$emit('showRegModal')"
                    >No account? Sign up</a
                >
            </div>
        </div>
    </div>
</template>
<script>
    import BaseInput from '../fields/BaseInput.vue';
    import SocialsAuth from './SocialsAuth.vue';
    import { required, email } from 'vuelidate/lib/validators';

    export default {
        name: 'AuthForm',
        components: { SocialsAuth, BaseInput },
        data() {
            return {
                email: '',
                pass: '',
            };
        },
        validations: {
            email: {
                required,
                email,
            },
            pass: {
                required,
            },
        },
        methods: {
            logIn() {
                let v = this;
                v.$v.$touch();
                if (!v.$v.$error) {
                    const observer = v.$apollo.subscribe({
                        query: require('~/graphql/mutations/user/tokenAuth.graphql'),
                        variables: {
                            username: v.email,
                            password: v.pass,
                            guestUuid: v.$store.state.user.guestUuid,
                        },
                    });
                    observer.subscribe({
                        next({ data: { tokenAuth } }) {
                            v.$apolloHelpers.onLogin(tokenAuth.token);
                            v.$store.commit('user/update_user', tokenAuth.user);
                            v.$emit('hide');
                            v.$cookies.set('guestUuid', null);
                            v.$store.commit('user/update_guestUuid', null);
                        },
                        error(error) {
                            v.$bvToast.toast('Please enter valid credentials', {
                                title: 'Log in',
                                variant: 'danger',
                            });
                        },
                    });
                }
            },
        },
    };
</script>
<style lang="less" scoped></style>
