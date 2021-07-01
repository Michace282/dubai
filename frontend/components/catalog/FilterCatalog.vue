<template>
    <div class="filter">
        <div class="mobile-head">
            <div class="filter-caption">
                Filter
                <img src="~/assets/images/icons/filter.svg"/>
            </div>
            <a href.prevent @click="$emit('closeFilter')">
                <img src="~/assets/images/icons/exit.svg"/>
            </a>
        </div>
        <filter-accordion
            v-for="category in categories"
            :key="category.key"
            class="arrow-descktop-hide"
            :class="{ active: filter.productType == category.key && !filter[category.filterName] }"
            :name="category.label"
            :title="category.label"
            @setCategory="
                filter.productType = category.key;
                filter.ladiesType = null;
                filter.mensType = null;
                filter.accessoriesType = null;
                filter.danceShoesType = null;
                breadcrumbs = [category.label];
            "
            visible
            isLink
        >
            <div class="category-box">
                <ul class="categories">
                    <li
                        class="category"
                        :class="{
                            active:
                                subCategory.key == filter[category.filterName] && filter.productType == category.key,
                        }"
                        @click="
                            filter.ladiesType = null;
                            filter.mensType = null;
                            filter.accessoriesType = null;
                            filter.danceShoesType = null;
                            filter.productType = category.key;
                            filter[category.filterName] = subCategory.key;
                            breadcrumbs = [category.label, subCategory.label];
                        "
                        v-for="subCategory in category.subCategories"
                        :key="subCategory.key"
                    >
                        {{ subCategory.label }}
                    </li>
                </ul>
            </div>
        </filter-accordion>
        <filter-accordion class="mt-30" name="price" title="Price range">
            <div class="d-flex align-items-center">
                <input
                    placeholder="Min"
                    v-model="range.min"
                    @input="
                        range.min * 1 + 0 != range.min ? (range.min = null) : '';
                        range.max && parseInt(range.min) > parseInt(range.max) ? (range.min = range.max) : '';
                        setMinValue(range.min);
                    "
                    type="text"
                    class="filter-input"
                />
                <span class="hyphen">-</span>
                <input
                    placeholder="Max"
                    v-model="range.max"
                    @input="
                        range.max * 1 + 0 != range.max ? (range.max = null) : '';
                        setMaxValue(range.max);
                    "
                    type="text"
                    class="filter-input"
                />
            </div>
        </filter-accordion>
        <filter-accordion class="mt-30" title="Colors" name="colors">
            <div class="colors" v-if="colors && colors.length > 0">
                <div class="color-group" v-for="color in colors" :key="color.id">
                    <input type="checkbox" name="checkbox" v-model="filter.colors" :value="color.id" :id="color.id"/>
                    <label class="label-color" :for="color.id">
                        <div
                            class="color"
                            :style="
                                color.image ? 'background-image: url(' + color.image + ')' : 'background:' + color.color
                            "
                        ></div>
                    </label>
                </div>
            </div>
            <div v-else>No colors</div>
        </filter-accordion>
        <filter-accordion class="mt-30" title="Size" name="size">
            <div class="sizes" v-if="sizes && sizes.length > 0">
                <div class="size-box" v-for="(size, index) in sizes" :key="index">
                    <input
                        type="checkbox"
                        name="sizes"
                        v-model="filter.sizes"
                        :value="size.size.toLowerCase()"
                        :id="index"
                    />
                    <label class="label-size" :for="index">{{ size.size }}</label>
                </div>
            </div>
        </filter-accordion>
        <div class="btn-box">
            <button
                class="btn btn-black w-100 mt-45"
                v-if="$store.state.windowWidth < 992"
                @click="
                    clickFilter();
                    filterProducts();
                    $emit('closeFilter');
                "
            >
                Apply
            </button>
            <button class="btn btn-outline-black w-100 mt-30" @click="clearFilter">reset the filter</button>
        </div>
    </div>
</template>
<script>
import FilterAccordion from './FilterAccordion.vue';

export default {
    name: 'FilterCatalog',
    components: {FilterAccordion},
    props: ['orderBy'],
    data() {
        return {
            colors: null,
            sizes: null,
            breadcrumbs: null,
            timer: null,
            timer2: null,
            range: {
                max: null,
                min: null,
            },
            filter: {
                colors: [],
                sizes: [],
                productType: null,
                ladiesType: null,
                mensType: null,
                    accessoriesType: null,
                    danceShoesType: null,
                    price_Gte: null,
                    price_Lte: null,
                    orderBy: null
                },
                categories: [
                    {
                        key: 'ladies',
                        label: 'Ladies',
                        filterName: 'ladiesType',
                        subCategories: [
                            {key: 'body', label: 'Body'},
                            {key: 'blouses', label: 'Blouses'},
                            {key: 'skirts', label: 'Skirts'},
                            {key: 'dresses', label: 'Dresses'},
                            {key: 'trousers', label: 'Trousers'},
                            {key: 'jumpsuits', label: 'Jumpsuits'},
                            {key: 'tops', label: 'Tops'},
                            {key: 'shorts', label: 'Shorts'},
                        ],
                    },
                    {
                        key: 'mens',
                        label: 'Mens',
                        filterName: 'mensType',
                        subCategories: [
                            {key: 'trousers', label: 'Trousers'},
                            {key: 'waistcoasts', label: 'Waistcoasts'},
                            {key: 'shirts', label: 'Shirts'},
                            {key: 't_shirts', label: 'T-shirts'},
                        ],
                    },
                    {
                        key: 'accessories',
                        label: 'Accessories',
                        filterName: 'accessoriesType',
                        subCategories: [
                            {key: 'shoe_accessories', label: 'Shoe accessories'},
                            {key: 'bags', label: 'Bags'},
                            {key: 'ladies_accessories', label: 'Ladies accessories'},
                        ],
                    },
                    {
                        key: 'dance_shoes',
                        label: 'Dance shoes',
                        filterName: 'danceShoesType',
                        subCategories: [
                            {key: 'ladies', label: 'Ladies'},
                            {key: 'mens', label: 'Mens'},
                        ],
                    },
                ],
            };
        },
        watch: {
            '$route.query'() {
                let f = []
                for (let key in this.$route.query) {
                    f.push(key);
                }

                if (f.length == 1) {
                    this.filter = {
                        colors: [],
                        sizes: [],
                        productType: this.$route.query.productType,
                        ladiesType: null,
                        mensType: null,
                        accessoriesType: null,
                        danceShoesType: null,
                        price_Gte: null,
                        price_Lte: null,
                    };
                    this.range.min = null;
                    this.range.max = null;
                    this.breadcrumbs = null;
                }
            },
            filter: {
                handler() {
                    if (this.$store.state.windowWidth > 991) {
                        this.filterProducts();
                    }
                },
                deep: true,
            },
            orderBy() {
                this.filter.orderBy = this.orderBy
                this.filterProducts();
            }
        },
        created() {
            for (let key in this.$route.query) {
                this.filter[key] = this.$route.query[key];
            }
            this.range.min = this.$route.query.price_Gte;
            this.range.max = this.$route.query.price_Lte;
        },
        methods: {
            clickFilter() {
                window.scrollTo({
                    top: document.getElementsByClassName('navbar-box')[0].clientHeight,
                    behavior: 'smooth'
                });
            },
            filterProducts() {
                let activeFilter = {};
                for (let key in this.filter) {
                    if (Array.isArray(this.filter[key])) {
                        if (this.filter[key].length > 0) {
                            activeFilter[key] = this.filter[key];
                        }
                    } else if (this.filter[key]) {
                        activeFilter[key] = this.filter[key];
                    }
                }
                this.$router.push({query: {...activeFilter}});
                this.$emit('changeFilter', activeFilter);
                this.$emit('setBreadcrumbs', this.breadcrumbs);
            },
            setMinValue(val) {
                let v = this;
                clearTimeout(v.timer);
                v.timer = setTimeout(() => {
                    v.filter.price_Gte = val;
                }, 1000);
            },
            setMaxValue(val) {
                let v = this;
                clearTimeout(v.timer2);
                v.timer2 = setTimeout(() => {
                    v.filter.price_Lte = val;
                }, 1000);
            },
            clearFilter() {
                this.filter = {
                    colors: [],
                    sizes: [],
                    productType: null,
                    ladiesType: null,
                    mensType: null,
                    accessoriesType: null,
                    danceShoesType: null,
                    price_Gte: null,
                    price_Lte: null,
                };
                this.range.min = null;
                this.range.max = null;
                this.breadcrumbs = null;
                this.$emit('setBreadcrumbs', this.breadcrumbs);
                this.$router.push({query: {}});
            },
        },
        apollo: {
            filterParams: {
                query: require('../../graphql/queries/product/filterParams'),
                update(data) {
                    if (data && data.productList) {
                        this.colors = [...data.productList.colorsAvailable];
                        this.sizes = [...data.productList.sizesAvailable];
                    }
                    return data;
                },
            },
        },
    };
</script>
<style lang="less" scoped>
.btn {
    padding: 11px 15px;

    @media @large {
        max-width: 155px;
        margin: 0px;
        font-size: 14px;
        padding: 9px 14px;
    }

    @media (max-width: 320px) {
        max-width: 100%;
        width: 100%;
        &:not(:first-child) {
            margin-top: 20px;
        }
    }
}

.btn-box {
    @media @large {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-direction: row-reverse;
        padding: 0px 20px;
        margin-top: 45px;
    }

    @media (max-width: 320px) {
        display: block;
    }
}

.mobile-head {
    display: none;

    @media @large {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 30px 20px;
    }
}

.color-group {
    margin-right: 14px;
    @media (min-width: 992px) {
        &:nth-child(6n + 6) {
            margin-right: 0px;
        }
    }

    .label-color {
        width: 1.9rem;
        height: 1.9rem;
    }
}

.colors {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: flex-start;
}

.label-size {
    text-transform: uppercase;
}

.filter-input {
    max-width: 110px;
    width: 100%;
    font-family: 'Inter-Light';
    font-size: 14px;
    color: @grey4;
    padding: 4px 10px;
    background: @white;
    border: 1px solid @black;
    box-sizing: border-box;
    border-radius: 2px;

    @media @large {
        max-width: 154px;
    }
}

.hyphen {
    margin: 0px 15px;
    font-weight: bold;
    color: @black;

    @media @large {
        margin: 0px 10px;
    }
}

.category-box {
    margin-top: -15px;

    .categories {
        &:not(:first-child) {
            margin-top: 15px;
        }

        padding-left: 10px;
        text-decoration: none;
        list-style: none;

        .category {
            cursor: pointer;
            margin-top: 5px;
            line-height: 22px;
            font-family: 'Inter-Light';
            font-size: 18px;
            color: @black;

            &.active {
                font-family: 'Inter-Regular';
                color: @yellow;
            }
        }
    }
}
</style>
