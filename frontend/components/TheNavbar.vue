<template>
    <div class="navbar-box">
        <div class="container">
            <b-navbar toggleable="lg" type="dark">
                <b-navbar-brand to="/"><img src="~/assets/images/logo.png" /></b-navbar-brand>

                <!-- <b-navbar-toggle target="nav-collapse"></b-navbar-toggle> -->
                <b-navbar-toggle target="navbar-toggle-collapse" @click="showIcons = !showIcons">
                    <template>
                        <img v-if="!showIcons" src="~/assets/images/icons/close-icon.svg" />
                        <img v-else src="~/assets/images/icons/burger-menu-icon.svg" />
                    </template>
                </b-navbar-toggle>
                <b-collapse id="navbar-toggle-collapse" is-nav>
                    <b-navbar-nav class="links m-auto">
                        <b-nav-item to="#">New <img class="star" src="../assets/images/icons/star.png" /></b-nav-item>
                        <b-nav-item to="/catalog/">Ladies</b-nav-item>
                        <b-nav-item to="#">Mens</b-nav-item>
                        <b-nav-item to="#">Dance shoes</b-nav-item>
                        <b-nav-item to="#">Accessories</b-nav-item>
                        <b-nav-item to="/about-us/">About us</b-nav-item>
                        <b-nav-item to="/contacts/">Contact us</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
                <b-navbar-nav class="ml-auto icons" :class="{ hide: !showIcons }">
                    <b-nav-item to="#"><img src="../assets/images/icons/heart.svg" /></b-nav-item>
                    <!-- <b-nav-item to="#"><img src="../assets/images/icons/loop.svg" /></b-nav-item> -->
                    <b-nav-item to="#"><img src="../assets/images/icons/basket.svg" /></b-nav-item>
                    <b-nav-item to="#" @click="$emit('showRegModal')"
                        ><img src="../assets/images/icons/account.svg"
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
    };
</script>
<style lang="less">
    .navbar {
        padding: 0px;

        .navbar-brand {
            img {
                width: 135px;

                @media @large {
                    width: 100px;
                }
            }
        }

        .navbar-toggler {
            border: none;
        }

        .icons {
            .nav-item {
                &:not(:last-child) {
                    margin-right: 15px;
                }

                .nav-link {
                    padding: 0px;
                }
            }

            @media @large {
                position: absolute;
                right: 50px;
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
</style>
<style lang="less" scoped>
    .hide {
        display: none;
    }

    .navbar-box {
        background: @black;
    }
</style>
