<template>
    <div class="container">
        <contact-form btnName="save" />
    </div>
</template>
<script>
    import ContactForm from '../../components/ContactForm.vue';
    export default {
        components: { ContactForm },
        name: 'contact',
        middleware: 'authenticated',
        created() {
            this.$store.commit('set_breadcrumbs', [
                { route: { name: 'account' }, name: 'personal account' },
                { route: { name: 'account-contact' }, name: 'contact information' },
            ]);
        },
    };
</script>
