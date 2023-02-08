<template>
    <div class="container">
        <div class="row caption-group">
            <div class="col-auto head-caption">
                <img src="~/assets/images/icons/truck.svg" alt="truck icon"/>
                Free shipping within UAE
            </div>
            <ApolloQuery :query="require('~/graphql/queries/gift/giftNewDetail.graphql')"
                         @result="giftNewDetail">
                <template v-slot="{ result: { error, data }, isLoading }">
                    <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                    <div v-else-if="data && data.giftNewDetail" class="col-auto head-caption">
                        <a href.prevent v-b-modal.present-modal
                        ><img src="~/assets/images/icons/present.svg" alt="present"/>
                            Get your present!
                        </a>
                    </div>
                </template>
            </ApolloQuery>
<!--            <div class="col-auto head-caption">-->
<!--                <img src="~/assets/images/icons/line.svg"/>-->
<!--                Size charts-->
<!--            </div>-->
        </div>
        <h1 class="d-none">Dance Clothes & Shoes Company</h1>
        <ApolloQuery :query="require('~/graphql/queries/stock/stockList.graphql')">
            <template v-slot="{ result: { error, data }, isLoading }">
                <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                <div v-else-if="data && data.stockList" class="result apollo">
                    <div class="row" v-if="data.stockList.edges.length > 0">
                        <div class="col-12">
                            <client-only>
                                <b-carousel
                                    id="carousel-1"
                                    :interval="4000"
                                    indicators
                                    class="index-carousel"
                                    img-width="1024"
                                    img-height="480"
                                >
                                    <b-carousel-slide v-for="stock in data.stockList.edges" :key="stock.node.id">
                                        <template #img>
                                            <img
                                                class="d-block img-fluid w-100"
                                                width="1024"
                                                height="480"
                                                :src="stock.node.imageCropping"
                                                alt="New Collection"
                                            />
                                        </template>
                                        <div class="box" v-if="stock.node.product">
                                            <nuxt-link
                                                :to="{ name: 'product-slug', params: { slug: stock.node.product.id } }"
                                                class="carousel-link"
                                            >
                                                {{
                                                    stock.node.productName
                                                        ? stock.node.productName
                                                        : stock.node.product.name
                                                }}
                                            </nuxt-link>
                                            <div class="caption">
                                                {{ stock.node.product.price }} AED
                                                <img src="~/assets/images/icons/arrow-right.svg" alt="right"/>
                                            </div>
                                        </div>
                                    </b-carousel-slide>
                                </b-carousel>
                            </client-only>
                        </div>
                    </div>
                </div>
            </template>
        </ApolloQuery>
        <index-page-categories/>
        <div class="advantages-group">
            <base-title title="Our advantages"/>
            <div class="row mt-45">
                <div class="col-6 col-sm-4 col-lg advantage" v-for="(advantage, index) in advantages" :key="index">
                    <img :src="require(`~/assets/images/icons/${advantage.icon}`)" alt="icon"/>
                    <div class="name">
                        {{ advantage.name }}
                    </div>
                </div>
            </div>
        </div>
        <b-modal id="present-modal" hide-footer centered v-if="giftNewText">
            <template #modal-header="{ close }">
                <h5 class="title">Get your present!</h5>
                <a href.prevent @click="close()">
                    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M8.32868 7.501L14.8284 1.00127C15.0572 0.772428 15.0572 0.401413 14.8284 0.172605C14.5996 -0.0562035 14.2285 -0.0562328 13.9997 0.172605L7.49999 6.67234L1.00029 0.172605C0.771451 -0.0562328 0.400436 -0.0562328 0.171628 0.172605C-0.0571801 0.401442 -0.0572094 0.772457 0.171628 1.00127L6.67133 7.50097L0.171628 14.0007C-0.0572094 14.2295 -0.0572094 14.6006 0.171628 14.8294C0.286032 14.9438 0.436003 15.001 0.585973 15.001C0.735943 15.001 0.885885 14.9438 1.00032 14.8294L7.49999 8.32966L13.9997 14.8294C14.1141 14.9438 14.2641 15.001 14.414 15.001C14.564 15.001 14.714 14.9438 14.8284 14.8294C15.0572 14.6005 15.0572 14.2295 14.8284 14.0007L8.32868 7.501Z"
                            fill="#808080"
                        />
                    </svg>
                </a>
            </template>
            <p>
                {{ giftNewText }}
            </p>
            <div class="text-right">
                <nuxt-link to="/catalog/" class="btn btn-black">Start buying</nuxt-link>
            </div>
        </b-modal>
    </div>
</template>

<script>
    import IndexPageCategories from '../components/IndexPageCategories.vue';

    export default {
        name: 'index',
        components: {IndexPageCategories},
        data() {
            return {
                giftNewText: null,
                advantages: [
                    {
                        icon: 'laptop.svg',
                        name: 'Wide range of products',
                    },
                    {
                        icon: 'calendar.svg',
                        name: 'Monthly update of collections',
                    },
                    {
                        icon: 'dimond.svg',
                        name: 'High quality material',
                    },
                    {
                        icon: 'sale.svg',
                        name: 'Affordable price',
                    },
                    {
                        icon: 'crown.svg',
                        name: 'Comfortable & Stylish',
                    },
                    {
                        icon: 'pen.svg',
                        name: 'We can arrange custom orders according to your measurements',
                    },
                ],
            };
        },
        head() {
            return {
                title: 'Dance Clothes & Shoes Company| DC&S Dubai',
                meta: [
                    {
                        hid: 'description',
                        name: 'description',
                        content: 'Stunning collection of beautiful dance costumes, dance shoes and accessories. Free shipping within the UAE. From classic and elegant to chic and sexy'
                    },
                    {
                        hid: 'keywords',
                        name: 'keywords',
                        content: 'Dancewear, Dance clothes, Ballroom dancewear, women shoes, women clothes, women clothing, dance accessories, shop luxury fashion online, shop luxury designers online, free shipping'
                    }
                ],
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', null);
        },
        methods: {
            giftNewDetail(data) {
                if (data.data && data.data.giftNewDetail) {
                    this.giftNewText = data.data.giftNewDetail.description
                }
            }
        }
    };
</script>
<style lang="less" scoped>
.advantages-group {
    margin-top: 90px;

    .advantage {
        display: flex;
        flex-direction: column;
        align-items: center;

        &:first-child {
            .name {
                margin-top: 9px;
            }
        }

        @media @large {
            margin-bottom: 30px;
        }

        .name {
            max-width: 140px;
            margin-top: 15px;
            text-align: center;

            @media @large {
                line-height: 22px;
            }
        }
    }
}

.caption-group {
    width: fit-content;
    margin: 0 auto;
    padding: 15px 0px;

    @media @medium {
        max-width: 235px;
        overflow-x: auto;
        display: flex;
        flex-wrap: nowrap;
    }

    .head-caption {
        display: flex;
        align-items: center;
        font-size: 14px;

        &:nth-child(2) {
            cursor: pointer;
        }

        &:last-child {
            margin-right: 22px;
        }

        img {
            margin-right: 15px;
        }
    }
}
</style>
