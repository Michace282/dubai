<template>
    <div class="container">
        <div class="order-group">
            <div class="basket-group">
                <div class="basket-title">Your order</div>
                <basket-container />
            </div>
            <div class="form-group">
                <contact-form btnName="buy" @buy="createOrder">
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
    import BasketContainer from '../components/basket/BasketContainer.vue';
    import ContactForm from '../components/ContactForm.vue';

    export default {
        components: { BasketContainer, ContactForm },
        name: 'create-order',
        created() {
            this.$store.commit('set_breadcrumbs', null);
        },
        methods: {
            createOrder() {
                let productsBasket = [];
                let cookieBasket = this.$cookies.get('basket');
                for (let i in cookieBasket) {
                    productsBasket.push({
                        product: cookieBasket[i].product,
                        color: cookieBasket[i].color,
                        size: cookieBasket[i].size,
                        count: cookieBasket[i].count,
                    });
                }
                console.log(cookieBasket);
                console.log(productsBasket);
                this.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/order/basketCreate.graphql'),
                        variables: {
                            guestUuid: this.$store.state.user.guestUuid,
                            productsBasket: productsBasket,
                        },
                    })
                    .then((data) => {
                        if (data && data.data.basketCreate.errors.length == 0) {
                            console.log(123);
                            this.$store.commit('product/update_basket', []);
                            this.$cookies.set('basket', {});
                        } else {
                            this.$bvToast.toast(data.data.basketCreate.errors[0].messages[0], {
                                title: 'Create order',
                                variant: 'danger',
                            });
                        }
                        console.log(data);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
        },
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
