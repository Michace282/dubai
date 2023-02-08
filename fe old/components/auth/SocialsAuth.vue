<template>
    <div class="row">
        <div class="col-auto caption pr-0 pr-md-2">
            With your social network
        </div>
        <div class="col pr-0">
            <a href.prevent class="mr-2"><img src="~/assets/images/icons/facebook.svg" alt="facebook icon" /></a>
            <a href.prevent><img src="~/assets/images/icons/google.svg" alt="google icon" /></a>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'SocialsAuth',
    };
</script>
<style lang="less" scoped>
    .caption {
        display: flex;
        align-items: center;
        font-size: 18px;
    }
</style>
