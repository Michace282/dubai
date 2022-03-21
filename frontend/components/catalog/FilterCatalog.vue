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
                breadcrumbs = [{key:category.key, label:category.label}];
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
                            breadcrumbs = [{key: category.key, label:category.label}, {key:subCategory.key, label:subCategory.label}];
                        "
                        v-for="subCategory in category.subCategories"
                        :key="subCategory.key"
                    >
                        <h2>{{ subCategory.label }}</h2>
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
                breadcrumbs: [],
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
                        label: 'Women dancewear',
                        meta: {
                            title: 'Women dancewear. Dance outfit for ladies| DC&S Dubai',
                            description: 'We are happy to present you our stunning dancewear collection for ladies. Here you can find dancing leotards, skirts, pants, dresses, crop-tops, blouses, jumpsuits etc.',
                            keywords: "Wonem's dancewear. Dance outfit for ladies.",
                            h1: "Women's dancewear"
                        },
                        filterName: 'ladiesType',
                        subCategories: [
                            {
                                key: 'leotards', label: 'Leotards',
                                meta: {
                                    title: 'Dancing leotard. Dancing bodies. Dance body Dubai| DC&S Dubai',
                                    description: 'Large collection of dance bodysuits/leotards. Classic bodies, latin bodies, many different colors and designs. Big size range. Availeble for order online and at our partners stores.',
                                    keywords: 'Dance bodysuit. Dance leotards. Dancing bodies.',
                                    h1: 'WOMENS DANCE LEOTARDS',
                                }
                            },
                            {
                                key: 'blouses', label: 'Blouses', meta: {
                                    title: 'Long sleeved dance tops, tunic dance tops. Dancing blouses| DC&S Dubai',
                                    description: 'Beautiful collection of dance blouses, long sleeve dance tops and tunics. Different designs, colors and all sizes are available for order online and at our partners stores.',
                                    keywords: 'Dancing blouses. Long sleeve dance top.',
                                    h1: 'WOMENS DANCE BLOUSES',
                                }
                            },
                            {
                                key: 'skirts', label: 'Skirts', meta: {
                                    title: 'Dancewear dance skirts. Ballroom dancing skirt. Latin skirt| DC&S Dubai',
                                    description: 'Your welcome to chose any dancing skirt from our big collection: ballroom dancing skirts, latin skirts, wrap dance skirts, black dance skirts.',
                                    keywords: 'Dancing skirts. Dancewer skirts.Ballroom dancing skirts.',
                                    h1: 'WOMENS DANCE SKIRT',
                                }
                            },
                            {
                                key: 'dresses', label: 'Dresses', meta: {
                                    title: 'Dacewear dresses. Latin, Salsa & Ballroom dancing dresses| DC&S Dubai',
                                    description: 'Unique dresses for Ballroom, Latin, Salsa dances. Extensive assortment - dresses with fringe, classic ballroom or exotic dance dresses.',
                                    keywords: 'Dancewear dresses. Dancing dresses. Dresses for dancers.',
                                    h1: 'WOMENS DANCE DRESSES',
                                }
                            },
                            {
                                key: 'pants', label: 'Pants', meta: {
                                    title: 'Women\'s dancing pants. Leggings for dance| DC&S Dubai',
                                    description: 'Many lovely variants of women\'s dancing pants for Latin and Ballroom dance. Leggings for any kind of dance and fitness in unique designs are available for online order and at partners stores.',
                                    keywords: 'Dancing pants. Leggings dance outfit. Women\'s dance pants.',
                                    h1: 'WOMENS DANCE PANTS',
                                }
                            },
                            {
                                key: 'jumpsuits', label: 'Jumpsuits', meta: {
                                    title: 'Dancing jumpsuits. Best jumpsuits for dance| DC&S Dubai',
                                    description: 'Perfect jumpsuits for dance lovers, super comfortable designs and high quality materials make you feel and look amazing in our jumpsuits. Available for order online and at our partners stores.',
                                    keywords: 'Jumpsuit for dancing. Jumpsuit dance costume.',
                                    h1: 'WOMENS DANCE JUMPSUITS',
                                }
                            },
                            {
                                key: 'tops', label: 'Tops', meta: {
                                    title: 'Dancewear tops, bra tops. Dancing crop top| DC&S Dubai',
                                    description: 'Beautiful lady\'s tops and bra tops for dancing or other activities at many different colors and designs available for order online or at our sale representor\'s stores.',
                                    keywords: 'Dancewear tops. Dancing crop tops.',
                                    h1: 'WOMENS DANCE TOPS',
                                }
                            },
                            {
                                key: 'shorts', label: 'Shorts', meta: {
                                    title: 'Women\'s dancewear shorts | DC&S Dubai',
                                    description: 'Women\'s dancing shorts. Shorts under dress/skirt, high waist shorts. Dance shop in Dubai| DC&S Company',
                                    keywords: 'Dancewear shorts women\'s',
                                    h1: 'WOMENS DANCE SHORTS',
                                }
                            },
                        ],
                    },
                    {
                        key: 'mens',
                        label: 'Mens dancewear',
                        filterName: 'mensType',
                        meta: {
                            title: 'Men\'s dancewear. Ballroom dance costume for male| DC&S Dubai',
                            description: 'We have a massive collection of dancewear for men. Dance pants, ballroom shirts, T-shirts, turtlenecks, long sleeves, shoes. All sizes are available.',
                            keywords: 'Men\'s dancewear. Male ballroom dance costumes.',
                            h1: 'MENS DANCEWEAR',
                        },
                        subCategories: [
                            {
                                key: 'trousers', label: 'Trousers', meta: {
                                    title: 'Dance trousers mens. Ballroom dance pants for man| DC&S Dubai',
                                    description: 'Classic Ballroom and Latin dance trousers for men. Dance trousers for practicing. All sizes are available for order online and at our sale representors stores.',
                                    keywords: 'Mens ballroom dance trousers',
                                    h1: 'MENS DANCE TROUSERS',
                                }
                            },
                            {
                                key: 'waistcoasts', label: 'Waistcoasts', meta: {
                                    title: 'Waistcoat for men. Waistcoat for dance| DC&S Dubai',
                                    description: 'Classic men\'s waistcoats a perfect chose for special occasions or dance events high quality material and unique design. Available for order online or at our partners stores.',
                                    keywords: 'Waistcoats for men',
                                    h1: 'MENS WAISTCOATS',
                                }
                            },
                            {
                                key: 'shirts', label: 'Shirts', meta: {
                                    title: 'Shirts for dance. Men\'s dance shirts. Dance shirts for guys| DC&S Dubai',
                                    description: 'The largest collection of dance shirts for guys in UAE. Distinct designs and wide sizes range let you choose a shirt perfectly matched your individuality.',
                                    keywords: 'Shirts for dance. Dance shorts for guys.',
                                    h1: 'MENS DANCE SHIRTS',
                                }
                            },
                            {
                                key: 't_shirts', label: 'T-shirts', meta: {
                                    title: 'T-shirts for dance. Dance T-shirts online| DC&S Dubai',
                                    description: 'Ultra comfortable and stylish T-shirts for any type of dances are available at all sizes and  colors for order online or at our partners stores.',
                                    keywords: 'Dance t-shirts. Dancers t-shirts.',
                                    h1: 'MENS DANCE T-SHIRTS',
                                }
                            },
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


                if (f.length == 0) {
                    this.filter = {
                        colors: [],
                        sizes: [],
                        productType: this.$route.params.product,
                        ladiesType: this.$route.params.product == 'ladies' ? this.$route.params.type : null,
                        mensType: this.$route.params.product == 'mens' ? this.$route.params.type : null,
                        accessoriesType: this.$route.params.product == 'accessories' ? this.$route.params.type : null,
                        danceShoesType: this.$route.params.product == 'dance_shoes' ? this.$route.params.type : null,
                        price_Gte: null,
                        price_Lte: null,
                    };
                    this.range.min = null;
                    this.range.max = null;
                    this.breadcrumbs = [];

                    if (this.$store.state.windowWidth <= 991) {
                        this.filterProducts();
                    }
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

            if (this.$route.params.product) {
                this.filter.productType = this.$route.params.product;
                let products = this.categories.filter((v) => v.key == this.filter.productType)

                if (products.length > 0) {
                    this.filter[products[0].filterName] = this.$route.params.type;
                }
            }

            this.range.min = this.$route.query.price_Gte;
            this.range.max = this.$route.query.price_Lte;

            if (this.$store.state.windowWidth <= 991) {
                this.filterProducts();
            }
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
                let queryFilter = {};
                for (let key in this.filter) {

                    if (Array.isArray(this.filter[key])) {
                        if (this.filter[key].length > 0) {
                            activeFilter[key] = this.filter[key];
                            if (['colors', 'sizes', 'price_Gte', 'price_Lte'].indexOf(key) != -1) {
                                queryFilter[key] = this.filter[key];
                            }
                        }
                    } else if (this.filter[key]) {
                        activeFilter[key] = this.filter[key];
                        if (['colors', 'sizes', 'price_Gte', 'price_Lte'].indexOf(key) != -1) {
                            queryFilter[key] = this.filter[key];
                        }
                    }

                }

                let breadcrumbs = []

                let url = '/catalog'

                if (this.filter.productType) {
                    let products = this.categories.filter((v) => v.key == this.filter.productType)
                    url += '/' + this.filter.productType
                    if (products.length > 0) {
                        breadcrumbs.push({
                            key: products[0].key,
                            label: products[0].label,
                            meta: products[0].meta,
                        })
                        if (this.filter[products[0].filterName]) {
                            let subCategories = products[0].subCategories.filter((v) => v.key == this.filter[products[0].filterName])
                            url += '/' + this.filter[products[0].filterName]

                            if (subCategories.length > 0) {
                                breadcrumbs.push({
                                    key: subCategories[0].key,
                                    label: subCategories[0].label,
                                    meta: subCategories[0].meta,
                                })
                            }
                        }
                    }
                }

                console.log(url);

                this.breadcrumbs = breadcrumbs;

                this.$router.push({path: url, query: {...queryFilter}});
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
                this.breadcrumbs = [];
                this.$emit('setBreadcrumbs', this.breadcrumbs);
                this.$router.push({path: '/catalog', query: {}});
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
                h2 {
                    cursor: pointer;
                    margin-top: 5px;
                    line-height: 22px;
                    font-family: 'Inter-Light';
                    font-size: 18px;
                    color: @black;
                    margin-bottom: 0;
                }

                &.active {
                    h2 {
                        font-family: 'Inter-Regular';
                        color: @yellow;
                    }
                }
            }
        }
    }
</style>
