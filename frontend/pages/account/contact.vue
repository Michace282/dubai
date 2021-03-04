<template>
    <div class="container">
        <contact-form btnName="save" @buy="userUpdate"/>
    </div>
</template>
<script>
    import ContactForm from '../../components/ContactForm.vue';

    export default {
        components: {ContactForm},
        name: 'contact',
        middleware: 'authenticated',
        created() {
            this.$store.commit('set_breadcrumbs', [
                {route: {name: 'account'}, name: 'personal account'},
                {route: {name: 'account-contact'}, name: 'contact information'},
            ]);
        },
        methods: {
            userUpdate(formInfo) {
                let v = this;
                let userUpdateInput = {
                    firstName: formInfo.firstName,
                    lastName: formInfo.lastName,
                    country: formInfo.country,
                    city: formInfo.city,
                    address: formInfo.address,
                    postalCode: formInfo.postalCode,
                    email: formInfo.email,
                    phone: formInfo.phone,
                };
                this.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/user/userUpdate.graphql'),
                        variables: {
                            input: userUpdateInput,
                        },
                    })
                    .then((data) => {
                        if (data && data.data.userUpdate.errors.length == 0) {
                            v.$bvToast.toast('Update CONTACT INFORMATION', {
                                title: 'Update CONTACT INFORMATION',
                                variant: 'success',
                            });
                            v.$store.commit('user/update_user', data.data.userUpdate.user);
                        } else {
                            v.$bvToast.toast(data.data.userUpdate.errors[0].messages[0], {
                                title: 'Update CONTACT INFORMATION',
                                variant: 'danger',
                            });
                        }
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
        },
    };
</script>
