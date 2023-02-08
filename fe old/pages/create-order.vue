<template>
    <div class="container">
        <div class="order-group">
            <div class="basket-group">
                <div class="basket-title">Your order</div>
                <basket-container />
            </div>
            <div class="form-group">
                <contact-form btnName="buy" @buy="createOrder" :showCreateOrderFields="true">
                    <div class="subtitle" v-if="!$store.state.user.user">
                        Would you like to save this information for the next time??
                        <!--TODO: По клику на ссылку открыть модалку -->
                        <a href.prevent class="link" @click="$nuxt.$emit('show-reg-modal')">Sign Up!</a>
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
            createOrder(formInfo) {
                let productsBasket = [];
                let basketCreate = {
                    firstName: formInfo.firstName,
                    lastName: formInfo.lastName,
                    country: formInfo.country,
                    city: formInfo.city,
                    address: formInfo.address,
                    postalCode: formInfo.postalCode,
                    email: formInfo.email,
                    phone: formInfo.phone,
                    description: formInfo.message,
                    pay: formInfo.payment ? 'card' : 'delivery',
                };
                let cookieBasket = this.$cookies.get('basket');
                for (let i in cookieBasket) {
                    productsBasket.push({
                        product: cookieBasket[i].product,
                        color: cookieBasket[i].color,
                        size: cookieBasket[i].size,
                        count: cookieBasket[i].count,
                    });
                }
                this.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/order/basketCreate.graphql'),
                        variables: {
                            code: formInfo.promo,
                            guestUuid: this.$store.state.user.guestUuid,
                            productsBasket: productsBasket,
                            basketCreate: basketCreate,
                        },
                    })
                    .then((data) => {
                        if (data && data.data.basketCreate.errors.length == 0) {
                            this.$store.commit('product/update_basket', []);
                            this.$cookies.set('basket', {});
                            if (data.data.basketCreate.urlPay) {
                                this.$store.commit('set_pay_link', data.data.basketCreate.urlPay);
                                this.$router.push({ name: 'pay-slug' });
                            } else if (!data.data.basketCreate.urlPay && formInfo.payment) {
                                this.$bvToast.toast('Something went wrong, try again later.', {
                                    title: 'Create order',
                                    variant: 'danger',
                                });
                            } else {
                                this.$nuxt.$emit(
                                    'show-confirm-modal',
                                    'Your order has been placed! In the near future, our Manager will contact you.',
                                );
                            }
                        } else {
                            this.$bvToast.toast(data.data.basketCreate.errors[0].messages[0], {
                                title: 'Create order',
                                variant: 'danger',
                            });
                        }
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
