<template>
    <div>
        <the-navbar @showRegModal="showModal = 'reg'" @showBasket="showModal = 'basket'" />
        <div class="main">
            <basket-modal
                :class="{ active: showModal == 'basket' }"
                @hide="showModal = false"
                @showRegModal="showModal = 'reg'"
            />
            <reg-form
                :class="{ active: showModal == 'reg' }"
                @hide="showModal = false"
                @showAuthModal="showModal = 'auth'"
            />
            <auth-form
                :class="{ active: showModal == 'auth' }"
                @hide="showModal = false"
                @showRegModal="showModal = 'reg'"
            />
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
        min-height: calc(100vh - 462px);
        padding-bottom: 90px;

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
</style>
