<template>
    <div class="container">
        <base-title title="Catalogue" class="mt-15" />
        <div class="row mt-45">
            <div class="col-12 col-lg-3 filter-group" :class="{ active: showFilter }">
                <filter-catalog @closeFilter="showFilter = false" />
            </div>
            <div class="col">
                <div class="prudocts-head">
                    <a href.prevent class="filter-caption" @click="showFilter = !showFilter">
                        Filter
                        <img src="~/assets/images/icons/filter.svg" />
                    </a>
                    <div class="breadcrumbs">
                        <div class="breadcrumb">Ladies</div>
                        <span class="separator">/</span>
                        <div class="breadcrumb">Body</div>
                    </div>
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
                                        showDropdown = false;
                                    "
                                    >{{ item.label }}</a
                                >
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 col-sm-4">
                        <product-item name="Body Merelyn" :price="900" />
                    </div>
                    <div class="col-6 col-sm-4">
                        <product-item name="Body Alexa" :price="900" />
                    </div>
                    <div class="col-6 col-sm-4">
                        <product-item name="Body Addison" :price="800" />
                    </div>
                </div>
                <pagination :pageCursor="5" />
            </div>
        </div>
    </div>
</template>
<script>
    import ProductItem from '../components/catalog/ProductItem.vue';
    import FilterCatalog from '../components/catalog/FilterCatalog.vue';
    import Pagination from '../components/catalog/Pagination';
    export default {
        components: { ProductItem, FilterCatalog, Pagination },
        name: 'catalog',
        data() {
            return {
                showDropdown: false,
                sortVal: { id: 1, label: 'Oldest to Newest' },
                showFilter: false,
                sortItems: [
                    { id: 1, label: 'Oldest to Newest' },
                    { id: 2, label: 'Price, low to high' },
                    { id: 3, label: 'Price, high to low' },
                    { id: 4, label: 'Best Selling' },
                    { id: 5, label: 'Newest to Oldest' },
                ],
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', [
                { link: 'index', name: 'Home' },
                { link: 'catatlog', name: 'Catalogue' },
            ]);
        },
    };
</script>
<style lang="less">
    .filter-group {
        @media @large {
            position: absolute;
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
</style>
