<template>
    <div class="container">
        <base-title title="contact us" />
        <div class="contacts-box">
            <div>
                <div class="contact-group">
                    <div class="label">E-mail</div>
                    <div class="value"><a href="mailto:dcs.dancewear@gmail.com">dcs.dancewear@gmail.com</a></div>
                </div>
                <div class="contact-group">
                    <div class="label">Telephone</div>
                    <div class="value">
                        <a href="tel:+971506553479">+971 50 655 3479</a>
                        <a href="tel:+971585967208">+971 58 596 7208</a>
                    </div>
                </div>
                <div class="contact-group">
                    <div class="label">Registered office</div>
                    <div class="value">
                        UAE, Dubai, Business Bay, Binary Tower, 20th floor
                        <div class="d-flex align-items-center mt-30">
                            <a href="" class="mr-3"><img src="~/assets/images/icons/whatsApp-gold.svg" /></a>
                            <a href="" class="ml-1"><img src="~/assets/images/icons/instagram-gold.svg" /></a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-group mt-45 mt-xl-0">
                <div class="title">Get in touch</div>
                <div class="row mt-45">
                    <div class="col-12 col-md-6">
                        <base-input label="Name" name="name" />
                    </div>
                    <div class="col-12 col-md-6 mt-30 mt-md-0">
                        <base-input label="E-mail or phone" name="phone" />
                    </div>
                </div>
                <div class="row mt-30">
                    <div class="col-12 textarea-group">
                        <label for="message" class="label">Message</label>
                        <textarea
                            type="text"
                            id="message"
                            class="w-100"
                            placeholder="Message"
                            name="message"
                        ></textarea>
                    </div>
                </div>
                <div class="text-right">
                    <button class="btn btn-black mt-30">Send</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import BaseInput from '../components/fields/BaseInput.vue';
    export default {
        components: { BaseInput },
        name: 'contacts',
        created() {
            this.$store.commit('set_breadcrumbs', [
                { link: 'index', name: 'Home' },
                { link: 'contacts', name: 'Contact us' },
            ]);
        },
    };
</script>
<style lang="less" scoped>
    @import '../assets/css/variables.less';

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

        .textarea-group {
            .label {
                margin: 0px;
                font-family: 'Inter-Regular';
                font-size: 14px;
                text-transform: uppercase;
                color: @grey4;
                text-transform: uppercase;
                @media @medium {
                    display: none;
                }
            }

            textarea {
                height: 43px;
                border: none;
                text-transform: uppercase;
                border-bottom: 1px solid @black;
                resize: none;
                background: @grey3;

                @media @medium {
                    height: 77px;
                }

                &::placeholder {
                    font-size: 14px;
                    opacity: 0;
                    @media @medium {
                        opacity: 1;
                    }
                }
            }
        }
    }
</style>
