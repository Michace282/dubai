<template>
    <div>
        <the-navbar @showRegModal="showModal = 'reg'" @showBasket="showModal = 'basket'" />
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
                <auth-form
                    v-if="showModal == 'auth'"
                    :key="2"
                    @hide="showModal = false"
                    @showRegModal="showModal = 'reg'"
                />
            </transition>

            <div class="content" :class="{ hide: showModal && showModal != 'basket', opacity: showModal == 'basket' }">
                <div class="container">
                    <div class="breadcrumbs" v-if="breadcrumbs && breadcrumbs.length > 0">
                        <nuxt-link
                            class="breadcrumb mb-0"
                            :to="{ name: breadcrumb.link }"
                            v-for="(breadcrumb, index) in breadcrumbs"
                            :key="index"
                        >
                            {{ breadcrumb.name }}
                            <span class="separator" v-if="index != breadcrumbs.length - 1">/</span>
                        </nuxt-link>
                    </div>
                </div>
                <nuxt />
            </div>
        </div>
        <the-footer />
    </div>
</template>
<script>
    import TheNavbar from '~/components/TheNavbar.vue';
    import TheFooter from '~/components/TheFooter.vue';
    import RegForm from '~/components/auth/RegForm';
    import AuthForm from '~/components/auth/AuthForm';
    import BasketModal from '../components/basket/BasketModal.vue';
    export default {
        components: { TheNavbar, TheFooter, RegForm, AuthForm, BasketModal },
        data() {
            return {
                showModal: false,
            };
        },
        computed: {
            breadcrumbs() {
                return this.$store.state.breadcrumbs;
            },
        },
    };
</script>
<style lang="less" scoped>
    .main {
        position: relative;
        min-height: calc(100vh - 458px);
        padding-bottom: 89px;

        @media @large {
            min-height: calc(100vh - 325px);
        }

        .content {
            transition: opacity 0.3s;

            &.hide {
                opacity: 0;
            }

            &.opacity {
                opacity: 0.5;
            }
        }
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
        right: -1000px;
    }

    .toggle-basket-enter-to,
    .toggle-basket-leave {
        right: 0px;
    }
</style>
