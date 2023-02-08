<template>
    <div class="navbar-box" id="navbar-mobile">
        <div class="container">
            <b-navbar toggleable="lg" type="dark">
                <b-navbar-toggle target="navbar-toggle-collapse" @click="showIcons = !showIcons">
                    <template>
                        <img v-if="!showIcons" src="~/assets/images/icons/close-icon.svg" alt="nav icon" />
                        <img v-else src="~/assets/images/icons/burger-menu-icon.svg" alt="nav icon" />
                    </template>
                </b-navbar-toggle>
                <b-navbar-brand :to="{ name: 'index' }"><img src="~/assets/images/logo.png" alt="brand logo" /></b-navbar-brand>
                <b-collapse id="navbar-toggle-collapse" is-nav>
                    <b-navbar-nav class="links m-auto">
                        <b-nav-item to="/catalog?isNew=true">New Collection <img class="star"
                                                                                           src="../assets/images/icons/star.png" alt="star" />
                        </b-nav-item>
                        <b-nav-item to="/catalog/ladies">Women’s dancewear</b-nav-item>
                        <b-nav-item to="/catalog/mens">Men’s dancewear</b-nav-item>
                        <b-nav-item to="/catalog/accessories">Dance Accessories</b-nav-item>
                        <b-nav-item to="/catalog/dance_shoes">Dance shoes</b-nav-item>
                        <b-nav-item to="/about-us/">About us</b-nav-item>
                        <b-nav-item to="/contacts/">Contact us</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
                <b-navbar-nav class="ml-auto icons" :class="{ hide: !showIcons }">
                    <b-nav-item to="/account/wish-list"><img src="../assets/images/icons/heart.svg" alt="heart" /></b-nav-item>
                    <b-nav-item @click="$emit('showBasket')">
                        <img src="../assets/images/icons/basket.svg" alt="basket" />
                        <span class="products-count" v-if="productCount > 0">+{{ productCount }}</span>
                    </b-nav-item>
                    <b-nav-item
                        @click="
                            !$store.state.user.user ? $emit('showRegModal') : $router.push({ name: 'account' })
                        "
                    ><img src="../assets/images/icons/account.svg" alt="account"
                    /></b-nav-item>
                </b-navbar-nav>
            </b-navbar>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'TheNavbar',
        data() {
            return {
                showIcons: true,
            };
        },
        computed: {
            user() {
                return this.$store.state.user.user;
            },
            productCount() {
                return this.$store.state.product.itemsCount;
            },
        },
        created() {
            this.$store.commit('product/update_items_count');
        },
    };
</script>
<style lang="less">
    #navbar-mobile {
        .navbar {
            padding: 0px;
            justify-content: left;

            .navbar-brand {
                img {
                    width: 135px;

                    @media @large {
                        width: 100px;
                    }
                }
            }

            .navbar-toggler {
                border: none !important;
                padding: 0;
                box-shadow: none !important;
                margin-right: 15px;
            }

            .icons {
                .products-count {
                    position: absolute;
                    color: @yellow;
                    font-size: 14px;
                    top: -17px;
                    left: 11px;
                    white-space: nowrap;
                }

                .nav-item {
                    &:not(:last-child) {
                        margin-right: 15px;
                    }

                    .nav-link {
                        position: relative;
                        padding: 0px;
                    }
                }

                @media @large {
                    position: absolute;
                    right: 0px;
                    top: 32px;
                    flex-direction: row;
                }
            }

            .links {
                @media @large {
                    padding-bottom: 100px;
                }

                .nav-item {
                    &:not(:last-child) {
                        margin-right: 30px;
                    }

                    @media (max-width: 1200px) {
                        &:not(:last-child) {
                            margin-right: 15px;
                        }
                    }

                    @media @large {
                        &:not(:last-child) {
                            margin-right: 0;
                        }
                    }

                    .nav-link {
                        display: flex;
                        align-items: center;
                        font-family: 'Inter-Light';
                        font-size: 14px;
                        line-height: 17px;
                        padding: 0px;
                        text-transform: uppercase;
                        color: @white !important;

                        @media @large {
                            margin-top: 30px;
                            justify-content: center;
                        }

                        img {
                            margin-left: 10px;
                        }
                    }
                }
            }
        }
    }
</style>
<style lang="less" scoped>
    .hide {
        display: none;
    }

    .navbar-box {
        background: @black;
    }
</style>
