<template>
    <div>
        <the-navbar
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
                <auth-form
                    v-if="showModal == 'auth'"
                    :key="2"
                    @hide="showModal = false"
                    @showRegModal="showModal = 'reg'"
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
        created() {
            if (!this.$cookies.get('guestUuid') && !this.$store.state.user.user) {
                this.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/user/questCreate.graphql'),
                    })
                    .then((data) => {
                        if (data && data.data.guestCreate.guest) {
                            this.$cookies.set('guestUuid', data.data.guestCreate.guest.uuid);
                            this.$store.commit('user/update_guestUuid', data.data.guestCreate.guest.uuid);
                        }
                    });
            } else if (this.$store.state.user.user && this.$cookies.get('guestUuid')) {
                this.$store.commit('user/update_guestUuid', null);
            } else if (this.$cookies.get('guestUuid')) {
                this.$store.commit('user/update_guestUuid', this.$cookies.get('guestUuid'));
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
            }

            &.opacity {
                opacity: 0.5;
                overflow: hidden;
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
        right: -100%;
    }

    .toggle-basket-enter-to,
    .toggle-basket-leave {
        right: 0px;
    }
</style>
