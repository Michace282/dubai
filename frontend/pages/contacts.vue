<template>
    <div class="container">
        <base-title title="contact us"/>
        <div class="contacts-box">
            <div>
                <div class="contact-group">
                    <div class="label">E-mail</div>
                    <div class="value"><a href="mailto:dcs.dancewear@gmail.com">dcs.dancewear@gmail.com</a></div>
                </div>
                <div class="contact-group">
                    <div class="label">Telephone</div>
                    <div class="value">
                        <a href="tel:+971506553479">+971 50 655 3470</a>
                        <a href="tel:+971585967208">+971 58 596 7208</a>
                    </div>
                </div>
                <div class="contact-group">
                    <div class="label">Registered office</div>
                    <div class="value">
                        <!-- UAE, Dubai, Business Bay, Binary Tower, 20th floor -->
                        Al Qouz 1, 6A steeet, “Palais De Danse” Dance Studio, Dubai, UAE
                        <div class="d-flex align-items-center mt-30">
                            <a href="https://wa.me/971585967208" target="_blank" class="mr-3"><img
                                src="~/assets/images/icons/whatsApp-gold.svg" alt="whatsapp icon"/></a>
                            <a href="https://www.instagram.com/dcs_dancewear/" target="_blank" class="ml-1"><img
                                src="~/assets/images/icons/instagram-gold.svg" alt="instagram icon"/></a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-group mt-45 mt-xl-0">
                <div class="title">Get in touch</div>
                <div class="row mt-45">
                    <div class="col-12 col-md-6">
                        <base-input label="Name" name="name" v-model="name"/>
                    </div>
                    <div class="col-12 col-md-6 mt-30 mt-md-0">
                        <base-input label="E-mail or phone"
                                    name="text"
                                    :class="{ error: $v.email_or_phone.$error }"
                                    v-model="$v.email_or_phone.$model"/>
                    </div>
                </div>
                <div class="row mt-30">
                    <div class="col-12 textarea-group" :class="{ error: $v.message.$error }">
                        <label for="message" class="label">Message</label>
                        <textarea
                            v-model="$v.message.$model"
                            type="text"
                            id="message"
                            class="w-100"
                            placeholder="Message"
                            name="message"
                        ></textarea>
                    </div>
                </div>
                <div class="text-right">
                    <button class="btn btn-black mt-30" @click="submit">Send</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import {required} from 'vuelidate/lib/validators';
    import BaseInput from '../components/fields/BaseInput.vue';

    export default {
        components: {BaseInput},
        name: 'contacts',
        head() {
            return {
                title: 'Contacts',
                meta: [
                    {
                        hid: 'description',
                        name: 'description',
                        content: 'Contacts',
                    },
                ],
            };
        },
        data() {
            return {
                name: null,
                email_or_phone: null,
                message: null
            }
        },
        validations: {
            email_or_phone: {
                required,
            },
            message: {
                required,
            },
        },
        created() {
            this.$store.commit('set_breadcrumbs', [
                {route: '/', name: 'Home'},
                {route: {name: 'contacts'}, name: 'Contact us'},
            ]);
        },
        methods: {
            submit() {
                let v = this;
                v.$v.$touch();
                if (!v.$v.$error) {
                    v.$apollo
                        .mutate({
                            mutation: require('~/graphql/mutations/user/contactCreate.graphql'),
                            variables: {
                                input: {
                                    emailOrPhone: v.email_or_phone,
                                    name: v.name,
                                    text: v.message
                                }
                            }
                        })
                        .then((data) => {
                            if (data) {
                                if (data.data.contactCreate.errors.length > 0) {
                                    v.$bvToast.toast(data.data.contactCreate.errors[0].messages[0], {
                                        title: 'CONTACT US',
                                        variant: 'danger',
                                    });
                                } else {
                                    v.$bvToast.toast('GOOD JOB!', {
                                        title: 'CONTACT US',
                                        variant: 'success',
                                    });
                                    v.name = '';
                                    v.email_or_phone = '';
                                    v.message = '';
                                    v.$v.$reset();
                                }
                            }
                        });

                }


            }
        }
    };
</script>
<style lang="less" scoped>
    .textarea-group {
        &.error {
            label {
                color: red;
            }

            textarear {
                border-bottom-color: red;
            }
        }
    }

    .contacts-box {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-top: 15px;

        .contact-group {
            display: flex;
            margin-bottom: 30px;

            @media @small {
                flex-direction: column;
            }

            .label {
                width: 90px;
                font-family: 'Inter-Medium';
                margin-right: 20px;
                font-style: normal;
                font-weight: 500;
                font-size: 18px;
                text-align: right;
                color: @black;

                @media @small {
                    text-align: left;
                }
            }

            .value {
                max-width: 290px;
                font-family: 'Inter-Light';
                font-size: 18px;
                color: @black;

                a {
                    display: block;
                    color: @black;
                }
            }
        }
    }

    .form-group {
        max-width: 635px;
        width: 100%;
        padding: 30px 45px 30px 50px;
        background: @grey3;
        border-radius: 2px;

        @media @medium {
            padding: 30px 20px;
        }

        .title {
            font-family: 'Inter-Regular';
            font-size: 24px;
            text-transform: uppercase;
            color: @black;
        }
    }
</style>
