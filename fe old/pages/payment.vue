<template>
    <div class="container vh">
        <div class="payment-box">
            <div>
                <base-title title="payment"/>
                <div class="title">You can use these payment methods</div>
                <div class="payment-group mt-40">
                    <div class="text-center">
                        <img src="~/assets/images/icons/credit-card.svg" alt="credit card"/>
                        <div class="caption">Credit or Debit card</div>
                    </div>
                    <div class="text-center">
                        <img src="~/assets/images/icons/cash.svg" alt="cash" />
                        <div class="caption">Cash on Delivery</div>
                    </div>
                </div>
            </div>
            <base-title title="&" class="icon d-none d-lg-block"/>
            <div class="mt-70">
                <base-title title="delivery"/>
                <div class="title">We are happy to offer you</div>
                <div class="delivery-group">
                    <img src="~/assets/images/icons/delivery-truck.svg" alt="delivery"/>
                    <div class="caption delivery">Free shipping for all orders within UAE</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'payment',
        head() {
            return {
                title: 'Payment',
                meta: [
                    {
                        hid: 'description',
                        name: 'description',
                        content: 'Payment',
                    },
                ],
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', [
                {route: '/', name: 'Home'},
                {route: {name: 'payment'}, name: 'payment & delivery'},
            ]);
        },
    };
</script>
<style lang="less" scoped>
.payment-box {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;

    .icon {
        height: fit-content;
        margin-right: 50px;
    }

    .mt-70 {
        @media @large {
            margin-top: 70px;
        }
    }

    .payment-group {
        display: flex;
        flex-wrap: wrap;

        .text-center {
            margin-bottom: 20px;

            &:first-child {
                margin-right: 40px;
                @media (max-width: 470px) {
                    margin-right: 25px;
                }
            }
        }
    }

    .title {
        margin-top: 45px;
        font-family: 'Inter-Regular';
        font-size: 24px;
        color: @black;

        @media @medium {
            font-size: 18px;
        }
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

            @media @medium {
                max-width: 155px;
            }
        }
    }
}
</style>
