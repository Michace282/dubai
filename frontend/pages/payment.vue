<template>
    <div class="container">
        <div class="d-flex justify-content-between">
            <base-title title="payment" />
            <base-title title="&" />
            <base-title title="delivery" />
        </div>
        <div class="payment-box mt-45">
            <div>
                <div class="title">You can use these payment methods</div>
                <div class="payment-group mt-40" >
                    <div class="text-center">
                        <img src="~/assets/images/icons/credit-card.svg" />
                        <div class="caption">Credit or Debit card</div>
                    </div>
                    <div class="text-center">
                        <img src="~/assets/images/icons/cash.svg" />
                        <div class="caption">Cash on Delivery</div>
                    </div>
                    <div class="text-center">
                        <img src="~/assets/images/icons/paypal.svg" />
                        <div class="caption">PayPal</div>
                    </div>
                </div>
            </div>
            <div>
                <div class="title">We are happy to offer you</div>
                <div class="delivery-group">
                    <img src="~/assets/images/icons/delivery-truck.svg" />
                    <div class="caption delivery">Free shipping for all orders within UAE</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'payment',
        created() {
            this.$store.commit('set_breadcrumbs', [
                { link: 'index', name: 'Home' },
                { link: 'payment', name: 'payment & delivery' },
            ]);
        },
    };
</script>
<style lang="less" scoped>
    @import '../assets/css/variables.less';

    .payment-box {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;

        .payment-group {
            display: flex;
            flex-wrap: wrap;

            .text-center {
                &:first-child {
                    margin-right: 40px;
                }
                &:nth-child(2) {
                    margin-right: 90px;
                }
            }
        }

        .title {
            font-family: 'Inter-Regular';
            font-size: 24px;
            color: @black;
        }

        .delivery-group {
            width: fit-content;
            text-align: center;
            margin-top: 40px;
        }

        .caption {
            margin-top: 15px;
            font-family: 'Inter-Light';
            font-size: 18px;
            color: @black;

            &.delivery {
                max-width: 240px;
                margin: 15px auto 0px;
            }
        }
    }
</style>
