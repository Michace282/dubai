<template>
    <div class="account-head-group">
        <base-title title="Personal account"/>
        <div class="bg-grey d-none d-lg-flex mt-45" v-if="user">
            <div>
                <div class="name">{{ user.firstName }} {{ user.lastName }}</div>
                <nuxt-link class="link-grey" to="/account/contact/">Сhange personal information</nuxt-link>
                <a
                    href.prevent
                    class="link-grey"
                    @click="
                        $store.commit('user/logout');
                        $apolloHelpers.onLogout();
                    "
                >Log out</a
                >
            </div>
            <div v-if="user.profile && user.profile.address">
                <div class="label">Address:</div>
                <div class="value">{{ user.profile.address }}</div>
            </div>
            <div>
                <div class="label" v-if="user.profile && user.profile.phone">Phone:</div>
                <div class="value" v-if="user.profile && user.profile.phone">{{ user.profile.phone }}</div>
                <div class="label mt-30">E-mail:</div>
                <div class="value">{{ user.email }}</div>
            </div>
        </div>
        <div class="bg-grey d-block d-lg-none mt-45" v-if="user">
            <div class="name">{{ user.firstName }} {{ user.lastName }}</div>
            <div class="row mt-30" v-if="user.profile && user.profile.address">
                <div class="col-6">
                    <div class="label">Address:</div>
                    <div class="value">{{ user.profile.address }}</div>
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-6">
                    <div class="label">E-mail:</div>
                    <div class="value">{{ user.email }}</div>
                </div>
                <div class="col-6" v-if="user.profile && user.profile.phone">
                    <div class="label">Phone:</div>
                    <div class="value">{{ user.profile.phone }}</div>
                </div>
            </div>
            <div class="row mt-30">
                <div class="col-auto">
                    <nuxt-link class="link-grey" to="/account/contact/">Сhange personal information</nuxt-link>
                </div>
                <div class="col">
                    <a
                        href.prevent
                        class="link-grey"
                        @click="
                            $store.commit('user/logout');
                            $apolloHelpers.onLogout();
                        "
                    >Log out</a
                    >
                </div>
            </div>
        </div>
<!--        <div class="bg-black" v-if="user">-->
<!--            <div class="title">How happy are you with your order? Your opinion matters for us!</div>-->
<!--            <div class="d-flex align-items-center flex-wrap mt-4 mt-xl-0">-->
<!--                <div class="rating-group mr-3 mr-sm-4">-->
<!--                    <a class="rating" href.prevent @click="rating = i" v-for="i in 5" :key="i">-->
<!--                        <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">-->
<!--                            <path-->
<!--                                v-if="i > rating"-->
<!--                                d="M24.2341 8.95635L16.7305 7.87774L13.354 1.07765C13.1282 0.611414 12.5672 0.416536 12.1009 0.642383C11.911 0.734392 11.7576 0.887709 11.6657 1.07765L8.2891 7.87774L0.785523 8.95635C0.430147 9.01317 0.138592 9.26819 0.0351839 9.61289C-0.0560166 9.94501 0.03285 10.3007 0.269648 10.5508L5.70972 15.8502L4.44351 23.3069C4.38651 23.6648 4.53058 24.025 4.81872 24.2448C5.10247 24.4607 5.48415 24.4971 5.80353 24.3386L12.5098 20.7744L19.2161 24.3386L19.6382 24.4324C19.8436 24.4498 20.0471 24.382 20.2009 24.2448C20.489 24.025 20.6331 23.6648 20.5761 23.3069L19.3099 15.8502L24.75 10.5508C24.9868 10.3007 25.0757 9.94501 24.9844 9.61289C24.881 9.26828 24.5895 9.01317 24.2341 8.95635ZM17.6216 14.8654C17.4297 15.0836 17.3439 15.3754 17.3872 15.6627L18.4189 21.7593L12.9319 18.8986C12.6648 18.7719 12.3549 18.7719 12.0877 18.8986L6.60072 21.7593L7.63247 15.6627C7.67574 15.3754 7.58993 15.0837 7.39801 14.8654L2.94274 10.5509L9.0863 9.65983C9.38826 9.60678 9.6484 9.41603 9.78978 9.14396L12.5098 3.61008L15.2299 9.14396C15.3712 9.41603 15.6313 9.60678 15.9333 9.65983L22.0769 10.5509L17.6216 14.8654Z"-->
<!--                                fill="#E6C643"-->
<!--                            />-->
<!--                            <path-->
<!--                                v-else-->
<!--                                d="M24.2341 8.95635L16.7305 7.87774L13.354 1.07765C13.1282 0.611414 12.5672 0.416536 12.1009 0.642383C11.911 0.734392 11.7576 0.887709 11.6657 1.07765L8.2891 7.87774L0.785523 8.95635C0.430147 9.01317 0.138592 9.26819 0.0351839 9.61289C-0.0560166 9.94501 0.03285 10.3007 0.269648 10.5508L5.70972 15.8502L4.44351 23.3069C4.38651 23.6648 4.53058 24.025 4.81872 24.2448C5.10247 24.4607 5.48415 24.4971 5.80353 24.3386L12.5098 20.7744L19.2161 24.3386L19.6382 24.4324C19.8436 24.4498 20.0471 24.382 20.2009 24.2448C20.489 24.025 20.6331 23.6648 20.5761 23.3069L19.3099 15.8502L24.75 10.5508C24.9868 10.3007 25.0757 9.94501 24.9844 9.61289C24.881 9.26828 24.5895 9.01317 24.2341 8.95635Z"-->
<!--                                fill="#E6C643"-->
<!--                            />-->
<!--                        </svg>-->
<!--                    </a>-->
<!--                </div>-->
<!--                <button class="btn btn-outline-black">Send</button>-->
<!--            </div>-->
<!--        </div>-->
        <div class="navigation-group">
            <nuxt-link class="navigation" to="/account/">Active Orders</nuxt-link>
            <nuxt-link class="navigation" to="/account/previous-orders/" v-if="user">Previous Orders</nuxt-link>
            <nuxt-link class="navigation" to="/account/wish-list/">wishlist</nuxt-link>
            <nuxt-link class="navigation" to="/account/track-orders/" v-if="user">Track orders</nuxt-link>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'AccountHeadGroup',
        data() {
            return {
                rating: 1,
            };
        },
        computed: {
            user() {
                return this.$store.state.user.user;
            },
        },
    };
</script>
<style lang="less">
.account-head-group {
    .block-title {
        @media @small {
            max-width: 170px;
            line-height: 44px;
        }

        .front-title {
            @media @small {
                line-height: 29px;
                bottom: 15px;
            }
        }
    }
}
</style>
<style lang="less" scoped>
.account-head-group {
    .block-title {
        @media @small {
            max-width: 170px;
            line-height: 44px;
        }

        .front-title {
            @media @small {
                line-height: 29px;
            }
        }
    }

    .bg-grey {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        background: @grey3;
        padding: 30px;

        @media @large {
            padding: 30px 20px;
        }

        .name {
            font-family: 'Inter-Medium';
            font-size: 24px;
            line-height: 29px;
            text-transform: uppercase;
            color: @black;
        }

        .link-grey {
            display: block;
            margin-top: 15px;
            font-family: 'Inter-Light';
            font-size: 14px;
            line-height: 17px;
            text-decoration-line: underline;
            color: @grey4;
        }

        .label {
            font-family: 'Inter-Light';
            font-size: 18px;
            line-height: 22px;
            color: @grey4;

            @media @medium {
                font-size: 14px;
                line-height: 17px;
            }
        }

        .value {
            max-width: 255px;
            margin-top: 15px;
            font-family: 'Inter-Medium';
            font-size: 18px;
            line-height: 22px;
            color: @black;

            @media @medium {
                margin-top: 10px;
                font-size: 14px;
                line-height: 17px;
            }
        }
    }

    .bg-black {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-top: 60px;
        padding: 30px;
        background: @black;

        @media @small {
            padding: 30px 20px;
        }

        .title {
            font-size: 18px;
            line-height: 22px;
            text-transform: uppercase;
            color: @white;

            @media @medium {
                font-size: 14px;
                line-height: 17px;
            }
        }

        .rating-group {
            display: flex;
            align-items: center;

            .rating {
                margin-right: 5px;
                cursor: pointer;
            }
        }

        .btn-outline-black {
            font-family: 'Inter-Medium';
            padding: 9px 60px 8px 60px;

            &:hover {
                background: #a9a8a8;
                color: @black !important;
            }

            @media @medium {
                padding: 9px 57px 8px 58px;
            }

            @media @small {
                padding: 9px 46px 8px 47px;
            }
        }
    }

    .navigation-group {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        margin-top: 60px;

        .navigation {
            font-family: 'Inter-Medium';
            font-size: 24px;
            line-height: 29px;
            text-transform: uppercase;
            color: @grey4;

            @media @large {
                font-size: 18px;
                margin-bottom: 15px;
                line-height: 22px;
            }

            @media @xs {
                &:nth-child(2) {
                    margin-right: 0px !important;
                }
            }

            &:not(:last-child) {
                margin-right: 45px;

                @media @small {
                    margin-right: 25px;
                }
            }

            &.nuxt-link-exact-active {
                color: @black;
            }
        }
    }
}
</style>
