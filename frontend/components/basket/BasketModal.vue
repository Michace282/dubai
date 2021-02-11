<template>
    <div class="basket-container">
        <!-- TODO: Скрывать модалки до перехода на другую страницу -->
        <div class="basket-group">
            <a href.prevent class="basket-title fs-24" @click="$emit('hide')"
                ><img src="~/assets/images/icons/arrow-collapse.svg" /> Shopping cart</a
            >
            <ApolloQuery
                :query="require('~/graphql/queries/product/productList')"
                :variables="{ ids: ids }"
                :update="updateProducts"
            >
                <template v-slot="{ result: { error, data }, isLoading }">
                    <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                    <div v-else-if="data && data.length > 0" class="result apollo">
                        <div class="mt-30">
                            <basket-item
                                v-for="(product, index) in data"
                                :key="index"
                                :index="index"
                                :name="product.name"
                                :price="product.price"
                                :color="product.activeColor"
                                :size="product.activeSize"
                                :count="product.count"
                                :colorsGroup="product.productsizecolorSet"
                                @setColor="
                                    (color) => {
                                        product.activeColor = color;
                                        updateBasket('color', color, product.basketIndex);
                                    }
                                "
                                @setSize="
                                    (size) => {
                                        product.activeSize = size;
                                        updateBasket('size', size, product.basketIndex);
                                    }
                                "
                                @setCount="
                                    (count) => {
                                        product.count = count;
                                        updateBasket('count', count, product.basketIndex);
                                    }
                                "
                            />
                        </div>
                    </div>
                </template>
            </ApolloQuery>

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
    import BasketItem from './BasketItem';

    export default {
        name: 'BasketModal',
        components: { BasketItem },
        data() {
            return {
                ids: null,
            };
        },
        created() {
            let basket = this.$cookies.get('basket');
            if (basket) {
                this.ids = [];
                for (let i in basket) {
                    this.ids.push(basket[i].product);
                }
            }
        },
        methods: {
 
            updateBasket(param, val, index) {
                let basket = this.$cookies.get('basket');
                basket[index][param] = val;
                this.$cookies.set('basket', JSON.stringify(basket));
            },
            updateProducts(data) {
                console.log(123);
                if (data && data.productList.edges.length > 0) {
                    let products = data.productList.edges;
                    let activeProducts = [];
                    let basket = this.$cookies.get('basket');
                    console.log(basket);
                    for (let j in basket) {
                        for (let i = 0; i < products.length; i++) {
                            if (basket[j].product == products[i].node.id) {
                                let product = { ...products[i].node };
                                product['activeColor'] = basket[j].color;
                                product['activeSize'] = basket[j].size;
                                product['count'] = basket[j].count;
                                product['basketIndex'] = j;
                                activeProducts.push(product);
                                break;
                            }
                        }
                    }
                    return activeProducts;
                }
                return [];
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
