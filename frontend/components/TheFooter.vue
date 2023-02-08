<template>
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col col-md-auto order-1 order-md-0">
                    <ul class="menu">
                        <li>
                            <nuxt-link to="/payment/">Payment & Delivery</nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="/contacts/">Contact us</nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="/returns/">Returns & Refunds</nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="/page/privacy_policy">Privacy Policy</nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="/page/terms_condition">Terms & Condition</nuxt-link>
                        </li>
                    </ul>
                </div>
                <div class="col-12 col-md order-0 order-md-1">
                    <div class="form-box">
                        <div class="description">Subscribe to receive updates, access to exclusive deals and more</div>
                        <div class="row form">
                            <div class="col pr-2 pr-lg-3 d-flex align-items-end">
                                <base-input class="dark" label="email" name="email"/>
                            </div>
                            <div class="col-auto input-box">
                                <button class="btn btn-send">Send</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-auto order-2 order-md-2">
                    <ul class="menu contacts">
                        <li>
                            <a href="tel:+971585967208">+971 58 596 7208</a>
                        </li>
                        <li>
                            <a href="tel:+971506553470">+971 50 655 3470</a>
                        </li>
                        <li class="text-right">
                            <a href="https://wa.me/971585967208" target="_blank" class="mr-2"><img
                                src="~/assets/images/icons/whatsApp.svg" alt="whatsapp icon" /></a>
                            <a href="https://www.instagram.com/dcs_dancewear/" target="_blank"><img
                                src="~/assets/images/icons/instagram.svg" alt="instagram icon" /></a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="row">
                <div class="col-12 copyright">
                    © Elite Performance Garments and Shoes L.L.C. {{ $moment(new Date()).format('YYYY') }}
                </div>
            </div>
        </div>
    </footer>
</template>
<script>
    import BaseInput from './fields/BaseInput.vue';

    export default {
        name: 'TheFooter',
        components: {BaseInput},
        data() {
            return {
                email: '',
            };
        },
    };
</script>
<style>
    .modal-container {
       position:relative!important;
    }
    .content.hide {
       display: none
    }
</style>
<style lang="less" scoped>
    .footer {
        background: @black;
        padding: 45px;

        .copyright {
            color: @white;
            text-align: center;
        }

        @media (max-width: 991px) {
            padding: 30px 20px;
        }

        .order-0 {
            @media @large {
                margin-bottom: 60px;
            }
        }

        .form-box {
            max-width: 400px;
            margin: 0 auto;

            .description {
                font-family: 'Inter-Medium';
                font-size: 14px;
                text-transform: uppercase;
                color: @white;
            }

            .form {
                margin-top: 30px;

                .dark {
                    @media (max-width: 475px) {
                        max-width: 155px;
                    }
                }

                .btn-send {
                    padding: 9px 60px;
                    background: @white;
                    border: 1px solid @white;
                    border-radius: 2px;
                    font-family: 'Inter-SemiBold';
                    font-size: 14px;
                    text-transform: uppercase;
                    color: @black;

                    @media @small {
                        @media @medium {
                            padding: 9px 57px 8px 58px;
                        }
                    }

                    &:hover {
                        border: 1px solid @white;
                        background: @black;
                        color: @white;
                    }
                }
            }
        }

        .menu {
            list-style: none;
            padding: 0px;

            &.contacts {
                li {
                    font-family: 'Inter-Medium';

                    &:nth-child(2) {
                        margin-top: 5px !important;
                    }

                    &:last-child {
                        margin-top: 15px;
                    }
                }
            }

            li {
                font-weight: normal;
                font-size: 14px;
                text-transform: uppercase;

                &:not(:first-child) {
                    margin-top: 10px;
                }

                a {
                    color: @white !important;
                }
            }
        }
    }
</style>
