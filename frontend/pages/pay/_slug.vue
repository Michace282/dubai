<template>
    <div class="container text-center" v-if="link">
        <iframe width="482" height="500" scrolling="No" frameborder="0" id="paymentFrame" :src="link"> </iframe>
    </div>
</template>
<script>
    export default {
        name: 'pay',
        layout: 'empty',
        computed: {
            link() {
                return this.$store.state.payLink;
            },
        },
        created() {
            if (!this.link) {
                this.$root.error({ statusCode: 404 });
            }
        },
    };
</script>
