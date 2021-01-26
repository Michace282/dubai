<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" /></a>
            <base-title title="Log in" />
            <socials-auth class="mt-30" />
            <div class="input-box">
                <base-input class="mt-45" label="e-mail or phone" name="email" />
            </div>
            <div class="input-box">
                <base-input class="mt-30" label="Password" name="pass" />
            </div>
            <div class="text-right mt-30">
                <button class="btn btn-black">Log in</button>
                <a href.prevent class="link mt-45 d-block">Forgot password?</a>
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

    export default {
        name: 'AuthForm',
        components: { SocialsAuth, BaseInput },
    };
</script>
<style lang="less" scoped></style>
