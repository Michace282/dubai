<template>
    <div>
        <the-navbar
            class="navbar-mobile"
            @showRegModal="showModal = 'reg'"
            @showBasket="$route.name != 'create-order' ? (showModal = 'basket') : ''"
        />
        <the-navbar-p-c
            class="navbar-pc"
            @showRegModal="showModal = 'reg'"
            @showBasket="$route.name != 'create-order' ? (showModal = 'basket') : ''"
        />
        <div class="main">
            <transition name="toggle-basket">
                <basket-modal
                    v-if="showModal == 'basket'"
                    @hide="showModal = false"
                    @showRegModal="showModal = 'reg'"
                />
            </transition>
            <transition name="toggle-modal">
                <reg-form
                    v-if="showModal == 'reg'"
                    :key="1"
                    @hide="showModal = false"
                    @showAuthModal="showModal = 'auth'"
                />
                <reset-form
                    v-if="showModal == 'reset'"
                    :key="1"
                    @hide="showModal = false"
                    @showAuthModal="showModal = 'auth'"
                    @showResetModal="showModal = 'reset'"
                    @showResetConfirmModal="showModal = 'confirm'"
                />
                <confirm-form
                    v-if="showModal == 'confirm'"
                    :key="1"
                    @hide="showModal = false"
                    @showAuthModal="showModal = 'auth'"
                    @showResetModal="showModal = 'reset'"
                    @showResetPassModal="showModal = 'pass'"
                />
                <pass-form
                    v-if="showModal == 'pass'"
                    :key="1"
                    @hide="showModal = false"
                    @showAuthModal="showModal = 'auth'"
                    @showResetModal="showModal = 'reset'"
                    @showResetPassModal="showModal = 'pass'"
                />
                <auth-form
                    v-if="showModal == 'auth'"
                    :key="2"
                    @hide="showModal = false"
                    @showRegModal="showModal = 'reg'"
                    @showResetModal="showModal = 'reset'"
                />
            </transition>
            <div class="content" :class="{ hide: showModal && showModal != 'basket', opacity: showModal == 'basket' }">
                <div class="container">
                    <div class="breadcrumbs" v-show="breadcrumbs && breadcrumbs.length > 0">
                        <div v-for="(breadcrumb, index) in breadcrumbs" :key="index">
                            <nuxt-link class="breadcrumb mb-0" :to="breadcrumb.route" v-if="breadcrumb.route">
                                {{ breadcrumb.name }}
                                <span class="separator" v-if="index != breadcrumbs.length - 1">/</span>
                            </nuxt-link>
                            <span class="breadcrumb" v-else>{{ breadcrumb.name }}</span>
                        </div>
                    </div>
                </div>
                <nuxt/>
            </div>
            <b-modal
                id="confirm-order-modal"
                ref="confirm-order-modal"
                @hidden="$router.push({ name: 'index', query: {} })"
                hide-footer
                centered
            >
                <template #modal-header="{ close }">
                    <h5 class="title">successful order processing</h5>
                    <a href.prevent @click="close()">
                        <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M8.32868 7.501L14.8284 1.00127C15.0572 0.772428 15.0572 0.401413 14.8284 0.172605C14.5996 -0.0562035 14.2285 -0.0562328 13.9997 0.172605L7.49999 6.67234L1.00029 0.172605C0.771451 -0.0562328 0.400436 -0.0562328 0.171628 0.172605C-0.0571801 0.401442 -0.0572094 0.772457 0.171628 1.00127L6.67133 7.50097L0.171628 14.0007C-0.0572094 14.2295 -0.0572094 14.6006 0.171628 14.8294C0.286032 14.9438 0.436003 15.001 0.585973 15.001C0.735943 15.001 0.885885 14.9438 1.00032 14.8294L7.49999 8.32966L13.9997 14.8294C14.1141 14.9438 14.2641 15.001 14.414 15.001C14.564 15.001 14.714 14.9438 14.8284 14.8294C15.0572 14.6005 15.0572 14.2295 14.8284 14.0007L8.32868 7.501Z"
                                fill="#808080"
                            />
                        </svg>
                    </a>
                </template>
                <p v-html="confirmModalText"></p>
                <div class="text-right">
                    <nuxt-link to="/" class="btn btn-black btn-home">Home</nuxt-link>
                </div>
            </b-modal>

            <b-modal
                id="confirm-reset-send-email-modal"
                ref="confirm-reset-send-email-modal"
                @hidden="$router.push({ name: 'index', query: {} })"
                hide-footer
                centered
            >
                <template #modal-header="{ close }">
                    <h5 class="title">Restore Password</h5>
                    <a href.prevent @click="close()">
                        <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M8.32868 7.501L14.8284 1.00127C15.0572 0.772428 15.0572 0.401413 14.8284 0.172605C14.5996 -0.0562035 14.2285 -0.0562328 13.9997 0.172605L7.49999 6.67234L1.00029 0.172605C0.771451 -0.0562328 0.400436 -0.0562328 0.171628 0.172605C-0.0571801 0.401442 -0.0572094 0.772457 0.171628 1.00127L6.67133 7.50097L0.171628 14.0007C-0.0572094 14.2295 -0.0572094 14.6006 0.171628 14.8294C0.286032 14.9438 0.436003 15.001 0.585973 15.001C0.735943 15.001 0.885885 14.9438 1.00032 14.8294L7.49999 8.32966L13.9997 14.8294C14.1141 14.9438 14.2641 15.001 14.414 15.001C14.564 15.001 14.714 14.9438 14.8284 14.8294C15.0572 14.6005 15.0572 14.2295 14.8284 14.0007L8.32868 7.501Z"
                                fill="#808080"
                            />
                        </svg>
                    </a>
                </template>
                <p v-html="confirmModalText"></p>
            </b-modal>
        </div>
        <the-footer/>
    </div>
</template>
<script>
    import TheNavbar from '~/components/TheNavbar.vue';
    import TheFooter from '~/components/TheFooter.vue';
    import RegForm from '~/components/auth/RegForm';
    import AuthForm from '~/components/auth/AuthForm';
    import ResetForm from '~/components/auth/ResetForm';
    import ConfirmForm from '~/components/auth/ConfirmForm';
    import PassForm from '~/components/auth/PassForm';
    import BasketModal from '../components/basket/BasketModal.vue';
    import TheNavbarPC from "~/components/TheNavbarPC";

    export default {
        components: {TheNavbarPC, TheNavbar, TheFooter, RegForm, AuthForm, ResetForm, ConfirmForm, PassForm, BasketModal},
        data() {
            return {
                showModal: false,
                confirmModalText: '',
            };
        },
        created() {
            let v = this;
            if (!v.$cookies.get('guestUuid') && !v.$store.state.user.user) {
                v.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/user/questCreate.graphql'),
                    })
                    .then((data) => {
                        if (data && data.data.guestCreate.guest) {
                            v.$cookies.set('guestUuid', data.data.guestCreate.guest.uuid);
                            v.$store.commit('user/update_guestUuid', data.data.guestCreate.guest.uuid);
                        }
                    });
            } else if (v.$store.state.user.user && v.$cookies.get('guestUuid')) {
                v.$store.commit('user/update_guestUuid', null);
            } else if (v.$cookies.get('guestUuid')) {
                v.$store.commit('user/update_guestUuid', v.$cookies.get('guestUuid'));
            }
            v.$nuxt.$on('show-reg-modal', () => {
                v.showModal = 'reg';
            });
            v.$nuxt.$on('show-conf-modal', () => {
                v.showModal = 'confirm';
            });
            v.$nuxt.$on('show-pass-modal', () => {
                v.showModal = 'pass';
            });
            v.$nuxt.$on('show-confirm-modal', (text) => {
                v.confirmModalText = text;
                v.$refs['confirm-order-modal'].show();
            });
            v.$nuxt.$on('show-reset-send-email-modal', (text) => {
                v.confirmModalText = text;
                v.$refs['confirm-reset-send-email-modal'].show();
            });
        },
        mounted() {
            let v = this;
            if (v.$route.query.success) {
                v.confirmModalText = 'Your order has been placed! In the near future, our Manager will contact you.';
                v.$refs['confirm-order-modal'].show();
            }
            if (process.client) {
                v.$store.commit('set_window_width', document.body.clientWidth);
                window.addEventListener('resize', () => {
                    v.$store.commit('set_window_width', document.body.clientWidth);
                });
            }
        },
        watch: {
            $route() {
                this.showModal = false;
            },
        },
        computed: {
            breadcrumbs() {
                return this.$store.state.breadcrumbs;
            },
        },
    };
</script>
<style lang="less" scoped>

    .navbar-mobile {
        display: none;
        @media @large {
            display: block;
        }
    }

    .navbar-pc {
        display: block;
        @media @large {
            display: none;
        }
    }

    .main {
        position: relative;
        min-height: calc(100vh - 458px);
        padding-bottom: 89px;
        overflow: hidden;

        @media @large {
            min-height: calc(100vh - 325px);
        }

        .content {
            transition: opacity 0.3s;

            &.hide {
                opacity: 0.1;
                max-height: 90vh;
                min-height: 90vh;
                overflow: hidden;

                @media @medium {
                    min-height: auto;
                    max-height: initial;
                    overflow: auto;
                }
            }

            &.opacity {
                opacity: 0.5;
                overflow: hidden;
            }
        }
    }

    .btn-home {
        padding: 11px 58px !important;
    }

    .toggle-modal-enter,
    .toggle-modal-leave-to {
        top: -1000px;
    }

    .toggle-modal-enter-to,
    .toggle-modal-leave {
        top: 0px;
    }

    .toggle-basket-enter,
    .toggle-basket-leave-to {
        right: -100%;
    }

    .toggle-basket-enter-to,
    .toggle-basket-leave {
        right: 0px;
    }
</style>
