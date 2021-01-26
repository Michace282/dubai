<template>
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col col-lg-auto order-1 order-lg-0 p-0">
                    <ul class="menu">
                        <li>
                            <nuxt-link to="/payment/">Payment & Delivery</nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="/contacts/">Contact us </nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="">Size charts</nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="/returns/">Returns & Refunds</nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="">Our advantages</nuxt-link>
                        </li>
                    </ul>
                </div>
                <div class="col-12 col-lg order-0 order-lg-1 p-0">
                    <div class="form-box">
                        <div class="description">Subscribe to receive updates, access to exclusive deals and more</div>
                        <div class="row form">
                            <div class="col-auto pr-2 pr-lg-3">
                                <input placeholder="E-MAIL" v-model="email" class="input" />
                            </div>
                            <div class="col-auto pr-0">
                                <button class="btn btn-send">Send</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-auto order-2 order-lg-2 p-0">
                    <ul class="menu contacts">
                        <li>
                            <a href="tel: +971506553470">+971 50 655 3470</a>
                        </li>
                        <li>
                            <a href="tel: +971506553470">+971 50 655 3470</a>
                        </li>
                        <li class="text-right">
                            <a href="" class="mr-2"><img src="~/assets/images/icons/whatsApp.svg" /></a>
                            <a href=""><img src="~/assets/images/icons/instagram.svg" /></a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</template>
<script>
    export default {
        name: 'TheFooter',
        data() {
            return {
                email: '',
            };
        },
    };
</script>
<style lang="less" scoped>
    @import '../assets/css/variables.less';
    .footer {
        margin-top: 90px;
        background: @black;
        padding: 45px;

        @media (max-width: 520px) {
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

                .input {
                    height: 100%;
                    font-family: 'Inter-Regular';
                    font-size: 14px;
                    background: black;
                    border: 0px;
                    border-bottom: 1px solid @white;
                    color: @grey4;

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
