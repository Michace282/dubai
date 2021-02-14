<template>
    <div>
        <div v-if="products && products.length > 0" class="items-container">
            <div class="mt-30">
                <basket-item
                    v-for="(product, index) in prodouctsList"
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
                    @remove="removeItem(index, product.basketIndex, prodouctsList)"
                />
            </div>
        </div>
        <div class="mt-30" v-else><h4>The shopping cart is empty :(</h4></div>
        <div class="d-flex justify-content-between mt-30">
            <div class="basket-title">Subtotal</div>
            <div class="basket-title">{{ subtotal }} aed</div>
        </div>
    </div>
</template>
<script>
    import BasketItem from './BasketItem';

    export default {
        name: 'BasketContainer',
        components: { BasketItem },
        data() {
            return {
                ids: null,
                prodouctsList: this.products ? [...this.products] : [],
            };
        },
        computed: {
            products() {
                return this.$store.state.product.basketItems;
            },
            subtotal() {
                let price = 0;
                for (let i in this.products) {
                    price = price + parseInt(this.products[i].price) * parseInt(this.products[i].count);
                }
                return price;
            },
        },
        watch: {
            products: {
                deep: true,
                handler() {
                    this.prodouctsList = this.products ? [...this.products] : [];
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
                this.$store.commit('product/update_item_param', { index: index, param: storeItemParam, val: val });
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
