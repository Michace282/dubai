<template>
    <div class="basket-container">
        <div class="basket-group">
            <a href.prevent class="basket-title fs-24" @click="$emit('hide')"
                ><img src="~/assets/images/icons/arrow-collapse.svg" alt="arrow collapse" /> Shopping cart</a
            >
            <basket-container />
            <div class="d-flex justify-content-between align-items-center mt-30">
                <div>
                    <nuxt-link to="/payment/" class="link-grey d-block">Payment & Delivery</nuxt-link>
                    <nuxt-link to="/returns/" class="link-grey d-block mt-10">Returns & Refunds</nuxt-link>
                </div>
                <nuxt-link to="/create-order/" class="btn btn-black" v-if="showBuyBtn"> Place the order </nuxt-link>
            </div>
            <div class="sign-up-group" v-if="!$store.state.user.user">
                <div class="basket-title">Would you like to track your order? Sign Up now!</div>
                <div class="text-right mt-30">
                    <button class="btn btn-outline-black" @click="$emit('showRegModal')">Sign Up</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import BasketContainer from './BasketContainer.vue';

    export default {
        name: 'BasketModal',
        components: { BasketContainer },
        computed: {
            showBuyBtn() {
                return this.$store.state.product.itemsCount;
            },
        },
    };
</script>
<style lang="less">
    .basket-container {
        position: absolute;
        right: 0px;
        top: 0px;
        width: 100%;
        height: 100%;
        z-index: 1000;
        overflow: auto;
        transition: all 0.5s ease;
    }
</style>
<style lang="less" scoped>
    .basket-container {
        display: flex;
        justify-content: flex-end;

        .mt-10 {
            margin-top: 10px;
        }

        .fs-24 {
            font-size: 24px !important;
        }

        .basket-group {
            max-width: 550px;
            width: 100%;
            padding: 30px 45px;
            background: @grey3;
            overflow-x: hidden;

            @media @xs {
                padding: 30px 20px;
                background: @white;
            }

            .btn-black {
                padding: 11px 16px 11px 15px;
                font-size: 14px;

                @media @xs {
                    padding: 11px 13px;
                }
            }

            .sign-up-group {
                margin-top: 60px;
                padding: 15px;
                background: @white;
                border-radius: 2px;

                @media @xs {
                    padding: 15px 20px;
                    margin: 90px -20px 0px -20px;
                    background: @grey3;
                }

                .title {
                    font-size: 18px;
                }

                .btn-outline-black {
                    padding: 11px 51px 11px 51px;
                    font-size: 14px;
                    text-align: right;
                }
            }

            .basket-title {
                display: flex;
                align-items: center;
                width: fit-content;

                img {
                    margin-right: 35px;
                    transform: rotate(270deg);

                    @media @xs {
                        height: 10px;
                        margin-right: 15px;
                    }
                }
            }
        }
    }
</style>
