<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-group">
                <ul class="menu">
                    <li>
                        <nuxt-link to="">Payment & Delivery</nuxt-link>
                    </li>
                    <li>
                        <nuxt-link to="">Contact us </nuxt-link>
                    </li>
                    <li>
                        <nuxt-link to="">Size charts</nuxt-link>
                    </li>
                    <li>
                        <nuxt-link to="">Returns & Refunds</nuxt-link>
                    </li>
                    <li>
                        <nuxt-link to="">Our advantages</nuxt-link>
                    </li>
                </ul>
                <div class="form-box">
                    <div class="description">Subscribe to receive updates, access to exclusive deals and more</div>
                    <div class="row form">
                        <div class="col-auto">
                            <input placeholder="E-MAIL" v-model="email" class="input" />
                        </div>
                        <div class="col-auto">
                            <button class="btn btn-send">Send</button>
                        </div>
                    </div>
                </div>
                <ul class="menu contacts">
                    <li>
                        <a href="tel: +971506553470">+971 50 655 3470</a>
                    </li>
                    <li>
                        <a href="tel: +971506553470">+971 50 655 3470</a>
                    </li>
                    <li class="text-right">
                        <a href="" class="mr-2"><img src="~/assets/images/icons/whatsApp.svg"/></a>
                        <a href=""><img src="~/assets/images/icons/instagram.svg"/></a>
                    </li>
                </ul>
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
    @import '../assets/css/colors.less';
    .footer {
        margin-top: 90px;
        background: @black;
        padding: 45px;

        .footer-group {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;

            .form-box {
                max-width: 380px;
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
    }
</style>
