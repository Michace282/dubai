<template>
    <div class="container">
        <base-title :title="h1" class="mt-15"/>
        <template class="desc">
    <div class="container">
        <ApolloQuery
            :query="require('~/graphql/queries/product/productType.graphql')"
            :variables="{
                productType: h1.charAt(0).toUpperCase() + h1.slice(1).toLowerCase(),
            }"
        >
            <template v-slot="{ result: { error, data }, isLoading }">
                <div v-if="isLoading || error" class="loading apollo mt-85"><loader /></div>
                <div v-else-if="data && data.productTypeDetail" class="result apollo">
                    <div class="row">
                        <div class="col-12">
                            <div class="text-box" v-html="data.productTypeDetail.description"></div>
                        </div>
                    </div>
                </div>
            </template>
        </ApolloQuery>
    </div>
</template>

        <div class="row mt-45">
            <div class="col-12 col-lg-3 filter-group" :class="{ active: showFilter }">
                <filter-catalog
                    :order-by="orderBy"
                    @closeFilter="showFilter = false"
                    @changeFilter="changeFilter"
                    @setBreadcrumbs="
                        (val) => {
                            breadcrumbs = val;
                        }
                    "
                />
            </div>
            <div class="col">
                <div class="prudocts-head">
                    <a href.prevent class="filter-caption" @click="showFilter = !showFilter">
                        Filter
                        <img src="~/assets/images/icons/filter.svg"/>
                    </a>
                    <div class="sort">
                        <div class="label">Sort</div>
                        <div class="select" :class="{ active: showDropdown }">
                            <a href.prevent @click="showDropdown = !showDropdown" class="selected">{{
                                    sortVal.label
                                }}</a>
                            <div class="dropdown">
                                <a
                                    href.prevent
                                    class="item"
                                    v-for="item in sortItems"
                                    :key="item.id"
                                    @click="
                                        sortVal = item;
                                        orderBy = item.id
                                        showDropdown = false;
                                    "
                                >{{ item.label }}</a
                                >
                            </div>
                        </div>
                    </div>
                </div>
                <ApolloQuery
                    :query="require('~/graphql/queries/product/productList.graphql')"
                    :variables="{
                        first: 12,
                        after: cursor,
                        isNew: isNew,
                        ...filter,
                    }"
                    ref="catalog"
                    @result="updateCursors"
                >
                    <template v-slot="{ result: { error, data }, isLoading }">
                        <transition name="fade" mode="out-in">
                            <div v-if="isLoading && loading || error" class="loading apollo mt-85" key="1">
                                <loader/>
                            </div>
                            <div v-else-if="data && data.productList" class="result apollo" key="2">
                                <div class="row" v-if="data.productList.edges.length > 0">
                                    <div
                                        class="col-6 col-md-4"
                                        v-for="product in data.productList.edges"
                                        :key="product.node.id"
                                    >
                                        <product-item
                                            :id="product.node.id"
                                            :name="product.node.name"
                                            :price="product.node.price"
                                            :priceSale="product.node.priceSale"
                                            :isWishlist="product.node.isWishlist"
                                            :colorsGroup="product.node.productsizecolorSet"
                                        />
                                    </div>
                                </div>
                                <div v-else class="no-result apollo" key="3">
                                    <h3 class="text-center mt-5">Product not found :(</h3>
                                </div>
                            </div>
                        </transition>
                    </template>
                </ApolloQuery>
                <pagination
                    v-if="!loading && pagesCursor && pagesCursor.length > 1"
                    :pageCursor="pagesCursor"
                    @changeCursor="(val) => (cursor = val)"
                    @changePage="(activeCursor) => (cursor = activeCursor)"
                />
            </div>
        </div>
    </div>
</template>
<script>

    import { computed, defineComponent, ref } from "vue";
    import ProductItem from '../components/catalog/ProductItem.vue';
    import FilterCatalog from '../components/catalog/FilterCatalog.vue';
    import Pagination from '../components/catalog/Pagination';
    import Loader from '../components/Loader.vue';

    export default {
        components: {ProductItem, FilterCatalog, Pagination, Loader},
        name: 'catalog',
        data() {

    

            let sortItems = [
                {id: 'created_at', label: 'Oldest to Newest'},
                {id: 'price', label: 'Price, low to high'},
                {id: '-price', label: 'Price, high to low'},
                {id: '-selling', label: 'Best Selling'},
                {id: '-created_at', label: 'Newest to Oldest'},
            ]

            let sortVal = null;
            let orderBy = null;

            if (this.$route.query.orderBy) {
                sortItems.forEach((v) => {
                    if (v.id == this.$route.query.orderBy) {
                        sortVal = v;
                        orderBy = v.id
                    }
                })
            }

            if (sortVal == null) {
                sortVal = sortItems[4];
            }

            let isNew = null;  
            
            if (this.$route.query.isNew)
                isNew = true

            return {
                breadcrumbs: [],
                pagesCursor: null,
                orderBy: orderBy,
                cursor: null,
                showDropdown: false,
                sortVal: sortVal,
                isNew: isNew,
                showFilter: false,
                sortItems: sortItems,
                filter: {},
                loading: true,
                h1: '',
                title: '',
                description: '',
                keywords: ''
            };
        },
        head() {
            return {
                title: this.title,
                meta: [
                    {
                        hid: 'description',
                        name: 'description',
                        content: this.description,
                    },
                    {
                        hid: 'keywords',
                        name: 'keywords',
                        content: this.keywords,
                    },
                ],
            };
        },
        methods: {
            changeFilter(f) {
                this.cursor = null;
                this.filter = f;
                this.loading = true;
            },
            updateCursors(data) {
                if (data.data && data.data.productList) {
                    this.loading = false;
                    this.pagesCursor = data.data.productList.pagesCursor;
                    let breadcrumbs = [
                        {route: '/', name: 'Home'},
                        {route: '/catalog', name: 'Catalogue'},
                    ]

                    let url = ''

                    if (this.breadcrumbs) {
                        this.breadcrumbs.forEach((v) => {
                            url += '/' + v.key
                            breadcrumbs.push({route: '/catalog' + url, name: v.label})
                            this.h1 = v.label;

                            if (v.meta) {
                                this.h1 = v.meta.h1;
                                this.title = v.meta.title;
                                this.description = v.meta.description;
                                this.keywords = v.meta.keywords;
                            }
                        })
                    }
                    if (breadcrumbs.length == 2) {
                        this.h1 = 'Catalogue';
                    }

                    this.$store.commit('set_breadcrumbs', breadcrumbs);
                } else {
                    this.pagesCursor = null;
                    this.loading = false;
                }
            },
        },
        watch: {
            breadcrumb(nv) {
                let breadcrumbs = [
                    {route: '/', name: 'Home'},
                    {route: '/catalog', name: 'Catalogue'},
                ]

                let url = ''

                if (nv) {
                    nv.forEach((v) => {
                        url += '/' + v.key
                        breadcrumbs.push({route: '/catalog' + url, name: v.label})

                        this.h1 = v.label;
                    })
                }

                if (breadcrumbs.length == 2) {
                    this.h1 = 'Catalogue';
                }

                this.$store.commit('set_breadcrumbs', breadcrumbs);

            }
        }
    };


</script>
<style>
row.mt-45 {
    clear: both;
}
.block-title {
    width: 100%;
}
.block-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 8px;
  padding: 24px 20px;
  background-color: skyblue;
  border-radius: 8px;
}
.block-content__paragraph {
  color: white;
}
.block-content__button {
  color: white;
  text-decoration: underline;
}
</style>
<style lang="less">
    .filter-group {
        @media @large {
            position: fixed;
            top: 0px;
            bottom: 0;
            right: 0;
            width: 100%;
            height: 100%;
            padding: 0px;
            z-index: 1000;
            left: -1000px;
            opacity: 0;
            background: #00000096;
            transition: opacity 0.1s;

            &.active {
                left: 0px;
                opacity: 1;

                .filter {
                    left: 0;
                }
            }
        }

        .filter {
            @media @large {
                position: absolute;
                max-width: 375px;
                width: 100%;
                height: 100%;
                left: -1000px;
                background: @white;
                transition: left 0.5s;
                padding-bottom: 20px;
                overflow: auto;
            }
        }
    }


</style>

<style lang="less" scoped>
    .prudocts-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 30px;

        .breadcrumbs {
            padding: 0px;

            @media @large {
                display: none;
            }

            .breadcrumb {
                text-transform: none;
                margin: 0px;
            }

            .separator {
                font-size: 14px;
                margin: 0px 10px;
                color: @grey4;
            }
        }

        .sort {
            display: flex;
            align-items: center;

            .label {
                font-size: 14px;
                color: @black;
                margin-right: 5px;

                @media @large {
                    font-size: 18px;
                }
            }

            .select {
                position: relative;
                min-width: 135px;
                width: 100%;

                &.active {
                    background: @grey3;

                    .dropdown {
                        display: block;
                    }
                }

                .selected {
                    padding: 10px;
                    font-size: 14px;
                    text-decoration: underline;
                    color: @black;
                }

                a {
                    cursor: pointer;
                }

                .dropdown {
                    display: none;
                    position: absolute;
                    z-index: 200;
                    padding: 10px;
                    background: @grey3;

                    .item {
                        display: block;
                        font-size: 14px;
                        color: @black;

                        &:not(:first-child) {
                            margin-top: 10px;
                        }

                        &:hover {
                            text-decoration: underline;
                        }
                    }
                }
            }
        }
    }

    .block-title {
       float: left;
    }
</style>
