<template>
    <div class="container">
        <base-title title="Personal account" />
        <ApolloQuery
            :query="require('~/graphql/queries/product/productWishlistList')"
            :variables="{
                guestUuid: $store.state.user.guestUuid,
                first: 18,
            }"
        >
            <template v-slot="{ result: { error, data }, isLoading }">
                <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                <div v-else-if="data && data.productWishlistList" class="result apollo">
                    <div class="row mt-45" v-if="data.productWishlistList.edges.length > 0">
                        <div
                            class="col-2"
                            v-for="product in data.productWishlistList.edges"
                            :key="product.node.product.id"
                        >
                            <product-item
                                class="product-sm"
                                :id="product.node.product.id"
                                :name="product.node.product.name"
                                :price="product.node.product.price"
                                :isWishlist="true"
                                :colorsGroup="product.node.product.productsizecolorSet"
                            />
                        </div>
                    </div>
                    <div v-else class="no-result apollo">
                        <h3 class="text-center mt-5">Products not found :(</h3>
                    </div>
                </div>
            </template>
        </ApolloQuery>
        <div class="bg-gray">
            <div class="text">Would you like to save information about all your orders? Sign Up now!</div>
            <button class="btn btn-black">Sign Up</button>
        </div>
    </div>
</template>
<script>
    import BaseTitle from '../../components/BaseTitle.vue';
    import ProductItem from '../../components/catalog/ProductItem.vue';
    export default {
        name: 'wish-list',
        components: { BaseTitle, ProductItem },
        data() {
            return {
                cursor: null,
            }
        },
        created() {
            this.$store.commit('set_breadcrumbs', [{ route: '', name: 'personal account' }]);
        },
    };
</script>
<style lang="less" scoped>
    .bg-gray {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 60px;
        background: @grey3;
        font-size: 18px;
        line-height: 22px;
        text-transform: uppercase;
        color: @black;
        padding: 32px 30px;

        .btn-black {
            padding: 7px 47px;
        }
    }
</style>
