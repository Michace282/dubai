<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" /></a>
            <base-title title="Log in" />
            <SocialsAuth class="mt-30" />
            <input type="text" class="input-dark w-100 mt-45" placeholder="e-mail or phone" name="name" />
            <input type="text" class="input-dark w-100 mt-30" placeholder="Password" name="pass" />
            <div class="text-right mt-30">
                <button class="btn btn-black">Log in</button>
                <a href.prevent class="link mt-45 d-block">Forgot password?</a>
                <a href.prevent class="link underline mt-15 d-block" @click="$emit('showRegModal')">No account? Sign up</a>
            </div>
        </div>
    </div>
</template>
<script>
    import SocialsAuth from './SocialsAuth.vue';

    export default {
        name: 'AuthForm',
        components: { SocialsAuth },
    };
</script>
<style lang="less" scoped></style>
