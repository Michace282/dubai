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
        <b-modal
            id="confirm-order-modal"
            ref="confirm-order-modal"
            @hidden="$router.push({ name: 'index' })"
            hide-footer
            centered
        >
            <template #modal-header="{ close }">
                <h5 class="title">successful order processing</h5>
                <a href.prevent @click="close()">
                    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M8.32868 7.501L14.8284 1.00127C15.0572 0.772428 15.0572 0.401413 14.8284 0.172605C14.5996 -0.0562035 14.2285 -0.0562328 13.9997 0.172605L7.49999 6.67234L1.00029 0.172605C0.771451 -0.0562328 0.400436 -0.0562328 0.171628 0.172605C-0.0571801 0.401442 -0.0572094 0.772457 0.171628 1.00127L6.67133 7.50097L0.171628 14.0007C-0.0572094 14.2295 -0.0572094 14.6006 0.171628 14.8294C0.286032 14.9438 0.436003 15.001 0.585973 15.001C0.735943 15.001 0.885885 14.9438 1.00032 14.8294L7.49999 8.32966L13.9997 14.8294C14.1141 14.9438 14.2641 15.001 14.414 15.001C14.564 15.001 14.714 14.9438 14.8284 14.8294C15.0572 14.6005 15.0572 14.2295 14.8284 14.0007L8.32868 7.501Z"
                            fill="#808080"
                        />
                    </svg>
                </a>
            </template>
            <p>Your order has been placed! In the near future, our Manager will contact you.</p>
            <div class="text-right">
                <nuxt-link to="/" class="btn btn-black btn-home">Home</nuxt-link>
            </div>
        </b-modal>
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
                            this.$refs['confirm-order-modal'].show();
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
    .btn-home {
        padding: 11px 58px !important;
    }

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
