<template>
    <div class="basket-container">
        <!-- TODO: Убрать скролл во время анимации -->
        <!-- TODO: Скрывать модалки до перехода на другую страницу -->
        <div class="basket-group">
            <a href.prevent class="basket-title" @click="$emit('hide')"
                ><img src="~/assets/images/icons/arrow-collapse.svg" /> Shopping cart</a
            >
            <div class="mt-30">
                <basket-item />
            </div>
            <div class="d-flex justify-content-between mt-30">
                <div class="basket-title">Subtotal</div>
                <div class="basket-title">1590 aed</div>
            </div>
            <div class="d-flex justify-content-between align-items-center mt-30">
                <div>
                    <nuxt-link to="" class="link-grey d-block">Payment & Delivery</nuxt-link>
                    <nuxt-link to="" class="link-grey d-block mt-10">Returns & Refunds</nuxt-link>
                </div>
                <button class="btn btn-black">Place the order</button>
            </div>
            <div class="bg-white">
                <div class="basket-title">Would you like to track your order? Sign Up now!</div>
                <div class="text-right mt-30">
                    <button class="btn btn-outline-black" @click="$emit('showRegModal')">Sign Up</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import BasketItem from './BasketItem';

    export default {
        name: 'BasketModal',
        components: { BasketItem },
    };
</script>
<style lang="less">
    .basket-container {
        position: absolute;
        width: 0px;
        height: 0px;
        right: -100%;
        transition: all 0.5s;
        overflow: hidden;

        &.active {
            width: 100%;
            height: 100%;
            right: 0;
            z-index: 1000;
            overflow: auto;
        }
    }
</style>
<style lang="less" scoped>
    .basket-container {
        display: flex;
        justify-content: flex-end;

        .mt-10 {
            margin-top: 10px;
        }

        .basket-group {
            max-width: 550px;
            width: 100%;
            padding: 30px 45px;
            background: @grey3;

            .btn-black {
                padding: 11px 16px 11px 15px;
                font-size: 14px;
            }

            .bg-white {
                margin-top: 60px;
                padding: 15px;
                background: @white;
                border-radius: 2px;

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
                }
            }
        }
    }
</style>
