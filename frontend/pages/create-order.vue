<template>
    <div class="container">
        <div class="order-group">
            <div class="basket-group">
                <div class="basket-title">Your order</div>
                <basket-item class="mt-30" />
                <basket-item />
                <div class="d-flex justify-content-between mt-30">
                    <div class="basket-title">Subtotal</div>
                    <div class="basket-title">1590 aed</div>
                </div>
            </div>
            <div class="form-group">
                <contact-form btnName="buy">
                    <div class="subtitle" v-if="!$store.state.user.user">
                        Would you like to save this information for the next time??
                        <!--TODO: По клику на ссылку открыть модалку -->
                        <a href.prevent class="link">Sign Up!</a>
                    </div>
                </contact-form>
            </div>
        </div>
    </div>
</template>
<script>
    import BasketItem from '../components/basket/BasketItem.vue';
    import ContactForm from '../components/ContactForm.vue';
    export default {
        components: { BasketItem, ContactForm },
        name: 'create-order',
    };
</script>
<style lang="less">
    .form-group {
        .form-title {
            margin: 0px;

            @media (min-width: 991px) {
                white-space: nowrap;
            }
        }
    }
</style>
<style lang="less" scoped>
    .order-group {
        display: flex;
        justify-content: flex-start;
        overflow: hidden;

        .basket-group {
            max-width: 550px;
            width: 100%;
            background: @grey3;
            padding: 30px 45px;

            @media (max-width: 1024px) {
                padding: 30px 15px;
            }

            @media @large {
                display: none;
            }
        }

        .form-group {
            max-width: 540px;
            padding-left: 50px;
            margin-top: 75px;

            @media (max-width: 1024px) {
                padding-left: 10px;
                max-width: 480px;
            }

            @media @large {
                max-width: unset;
                margin: 30px auto;
                padding: 0px;
            }
        }

        .subtitle {
            margin-top: 30px;
            font-family: 'Inter-Medium';
            font-size: 14px;
            text-transform: uppercase;
            color: @black;

            .link {
                text-decoration: underline;
                cursor: pointer;
            }
        }
    }
</style>
