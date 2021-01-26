<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" /></a>
            <base-title title="Sign up" />
            <socials-auth class="mt-30" />
            <div class="input-box">
                <base-input class="mt-45" label="e-mail or phone" name="email" />
            </div>
            <div class="input-box">
                <base-input class="mt-30" label="Password" name="pass" />
            </div>
            <div class="input-box">
                <base-input class="mt-30" label="repeat Password" name="pass2" />
            </div>
            <div class="text-right mt-30">
                <button class="btn btn-black">Sign up</button>
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
    export default {
        components: { SocialsAuth, BaseInput },
        name: 'RegForm',
    };
</script>
<style lang="less" scoped>
    .btn-black {
        padding: 8px 51px;
    }
</style>
