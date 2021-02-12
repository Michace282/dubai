<template>
    <div class="container">
        <account-head-group />
        <ApolloQuery
            :query="require('~/graphql/queries/product/productWishlistList')"
            :variables="{
                guestUuid: $store.state.user.guestUuid,
                first: 18,
                after: cursor,
            }"
            @result="updateCursors"
            fetchPolicy="no-cache"
        >
            <template v-slot="{ result: { error, data }, isLoading, query }">
                <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                <div v-else-if="data && data.productWishlistList" class="result apollo">
                    <div class="row mt-45" v-if="data.productWishlistList.edges.length > 0">
                        <div
                            class="col-2"
                            v-for="(product, index) in data.productWishlistList.edges"
                            :key="product.node.product.id"
                        >
                            <product-item
                                class="product-sm"
                                :id="product.node.product.id"
                                :name="product.node.product.name"
                                :price="product.node.product.price"
                                :isWishlist="true"
                                :colorsGroup="product.node.product.productsizecolorSet"
                                @remove="data.productWishlistList.edges.splice(index, 1)"
                            />
                        </div>
                    </div>
                    <div v-else class="no-result apollo">
                        <h3 class="text-center mt-5">Products not found :(</h3>
                    </div>
                </div>
            </template>
        </ApolloQuery>
        <pagination
            v-if="pagesCursor && pagesCursor.length > 1"
            @changeCursor="(val) => (cursor = val)"
            :pageCursor="pagesCursor"
        />
        <div class="bg-gray" v-if="!$store.state.user.user">
            <div class="text">Would you like to save information about all your orders? Sign Up now!</div>
            <button class="btn btn-black" @click="$nuxt.$emit('show-reg-modal')">Sign Up</button>
        </div>
    </div>
</template>
<script>
    import BaseTitle from '~/components/BaseTitle.vue';
    import ProductItem from '~/components/catalog/ProductItem.vue';
    import Pagination from '~/components/catalog/Pagination';
    import AccountHeadGroup from '~/components/AccountHeadGroup';

    export default {
        name: 'wish-list',
        components: { BaseTitle, ProductItem, Pagination, AccountHeadGroup },
        data() {
            return {
                cursor: null,
                pagesCursor: null,
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', [{ route: '', name: 'personal account' }]);
        },
        methods: {
            updateCursors(data) {
                if (data.data && data.data.productWishlistList) {
                    this.pagesCursor = data.data.productWishlistList.pagesCursor;
                } else {
                    this.pagesCursor = null;
                }
            },
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

    .no-result {
        padding: 60px 0px;
    }
</style>
