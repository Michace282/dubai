<template>
    <div>
        <div v-if="products && products.length > 0" class="items-container">
            <div class="mt-30">
                <basket-item
                    v-for="(product, index) in productList"
                    :key="product.basketIndex"
                    :name="product.name"
                    :price="product.price"
                    :color="product.activeColor"
                    :size="product.activeSize"
                    :count="product.count"
                    :colorsGroup="product.productsizecolorSet"
                    @setColor="
                        (color) => {
                            updateBasket('color', color, product.basketIndex, index, 'activeColor');
                        }
                    "
                    @setSize="
                        (size) => {
                            updateBasket('size', size, product.basketIndex, index, 'activeSize');
                        }
                    "
                    @setCount="
                        (count) => {
                            updateBasket('count', count, product.basketIndex, index, 'count');
                        }
                    "
                    @remove="removeItem(index, product.basketIndex, productList)"
                />
            </div>
        </div>
        <div class="mt-30" v-else><h4>The shopping cart is empty :(</h4></div>
        <div class="d-flex justify-content-between mt-30" v-if="!subtotal_discount">
            <div class="basket-title">Subtotal</div>
            <div class="basket-title">{{ subtotal }} aed</div>
        </div>
        <div class="d-flex justify-content-between mt-30 discount" v-if="subtotal_discount">
            <div class="basket-title">Subtotal</div>
            <div class="basket-title">{{ subtotal }} aed</div>
        </div>
        <div class="d-flex justify-content-between mt-15 discount" v-if="subtotal_discount">
            <div class="basket-title">Discount</div>
            <div class="basket-title">{{ subtotal_discount }} aed</div>
        </div>
        <div class="d-flex justify-content-between mt-30" v-if="subtotal_discount">
            <div class="basket-title">Total</div>
            <div class="basket-title">{{ subtotal - subtotal_discount }} aed</div>
        </div>

    </div>
</template>
<script>
    import BasketItem from './BasketItem';

    export default {
        name: 'BasketContainer',
        components: {BasketItem},
        data() {
            return {
                ids: null,
                productList: this.products ? [...this.products] : [],
            };
        },
        computed: {
            products() {
                return this.$store.state.product.basketItems;
            },
            subtotal_count() {
                let count = 0;
                for (let i in this.products) {
                    count += parseInt(this.products[i].count)
                }
                return count;
            },
            discountProducts() {
                let subtotal_count = parseInt(this.subtotal_count / 2)
                let k = 0;
                let productList = this.productList.sort(function (a, b) {
                    return a.price - b.price;
                })

                for (let i in productList) {
                    this.productList[i].priceDiscount = 0;
                    for (let j = 0; j < productList[i].count; j++) {
                        if (k < subtotal_count) {
                            // if (productList[i].priceDiscount) {
                            //     productList[i].priceDiscount += parseInt(productList[i].price / 100 * 30);
                            // } else {
                            //     productList[i].priceDiscount = parseInt(productList[i].price / 100 * 30);
                            // }
                            // k += 1;
                        } else {
                            break;
                        }
                    }
                }
                return productList;
            },
            subtotal() {
                let price = 0;
                for (let i in this.discountProducts) {
                    price = price + parseInt(this.discountProducts[i].price) * parseInt(this.discountProducts[i].count);
                }
                return price;
            },
            subtotal_discount() {
                let discount = 0;
                for (let i in this.discountProducts) {
                    if (this.discountProducts[i].priceDiscount) {
                        discount = discount + parseInt(this.discountProducts[i].priceDiscount);
                    }
                }
                return discount;
            },
        },
        watch: {
            products: {
                deep: true,
                handler() {
                    this.productList = this.products ? [...this.products] : [];
                },
            },
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
            removeItem(index, basketIndex, data) {
                let basket = this.$cookies.get('basket');
                delete basket[basketIndex];
                this.$cookies.set('basket', JSON.stringify(basket));
                data.splice(index, 1);
                this.$emit('toggleBuyBtn', data.length > 0);
                this.$store.commit('product/update_basket', data);
            },
            updateBasket(cookieItemParam, val, basketIndex, index, storeItemParam) {
                let basket = this.$cookies.get('basket');
                basket[basketIndex][cookieItemParam] = val;
                this.$cookies.set('basket', JSON.stringify(basket));
                this.$store.commit('product/update_item_param', {index: index, param: storeItemParam, val: val});
            },
        },
        apollo: {
            products: {
                query: require('~/graphql/queries/product/productList'),
                skip() {
                    return !this.ids || this.ids.length == 0;
                },
                variables() {
                    return {
                        ids: this.ids,
                    };
                },
                update(data) {
                    if (data && data.productList.edges.length > 0) {
                        let products = data.productList.edges;
                        let activeProducts = [];
                        let basket = this.$cookies.get('basket');
                        for (let j in basket) {
                            for (let i = 0; i < products.length; i++) {
                                if (basket[j].product == products[i].node.id) {
                                    let product = {...products[i].node};
                                    product['activeColor'] = basket[j].color;
                                    product['activeSize'] = basket[j].size;
                                    product['count'] = basket[j].count;
                                    product['basketIndex'] = j;
                                    activeProducts.push(product);
                                    break;
                                }
                            }
                        }
                        this.$store.commit('product/update_basket', activeProducts);
                    } else {
                        this.$store.commit('product/update_basket', []);
                    }
                    return data;
                },
            },
        },
    };
</script>
<style lang="less" scoped>
    .items-container {
        max-height: 650px;
        overflow: auto;
    }
</style>
