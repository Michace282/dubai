<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" /></a>
            <base-title title="Sign up" />
            <SocialsAuth class="mt-30" />
            <input type="text" class="input-dark w-100 mt-45" placeholder="e-mail or phone" name="name" />
            <input type="text" class="input-dark w-100 mt-30" placeholder="Password" name="pass" />
            <input type="text" class="input-dark w-100 mt-30" placeholder="repeat Password" name="pass2" />
            <div class="text-right mt-30">
                <button class="btn btn-black">Sign up</button>
                <a href.prevent class="link underline mt-45 d-block" @click="$emit('showAuthModal')">Already have an account? Log in</a>
            </div>
        </div>
    </div>
</template>
<script>
    import SocialsAuth from './SocialsAuth.vue';
    export default {
        components: { SocialsAuth },
        name: 'RegForm',
    };
</script>
<style lang="less" scoped>
    .btn-black {
        padding: 8px 51px;
    }
</style>
