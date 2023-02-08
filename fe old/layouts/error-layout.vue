<template>
    <div>
        <the-navbar />
        <nuxt />
        <the-footer />
    </div>
</template>
<script>
    import TheNavbar from '~/components/TheNavbar.vue';
    import TheFooter from '~/components/TheFooter.vue';
    export default {
        name: 'error-layout',
        components: { TheNavbar, TheFooter },
    };
</script>
