<template>
    <div class="container">
        <contact-form />
    </div>
</template>
<script>
    import ContactForm from '../../components/ContactForm.vue';
    export default {
        components: { ContactForm },
        name: 'contact',
        created() {
            this.$store.commit('set_breadcrumbs', [
                { link: 'account', name: 'personal account' },
                { link: 'contact', name: 'contact information' },
            ]);
        },
    };
</script>
