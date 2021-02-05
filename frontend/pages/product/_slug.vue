<template>
    <div>
        <ApolloQuery
            :query="require('~/graphql/queries/product/productDetail')"
            :variables="{
                id: $route.params.slug,
            }"
            @result="result"
        >
            <template v-slot="{ result: { error, data }, isLoading }">
                <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                <div v-else-if="data && data.productDetail" class="result apollo">
                    <div class="container">
                        <div class="row">
                            <div class="col-7">
                                <product-carousel
                                    v-if="
                                        data.productDetail.productsizecolorSet.edges[colorVal] &&
                                        data.productDetail.productsizecolorSet.edges[colorVal].node.color
                                            .productsizecolorSet.edges.length > 0 &&
                                        data.productDetail.productsizecolorSet.edges[colorVal].node.color
                                            .productsizecolorSet.edges[0].node.productimageSet.edges.length > 0
                                    "
                                    :images="
                                        data.productDetail.productsizecolorSet.edges[colorVal].node.color
                                            .productsizecolorSet.edges[0].node.productimageSet.edges
                                    "
                                />
                            </div>
                            <div class="col">
                                <div class="head-group">
                                    <div>
                                        <div class="bold text-uppercase">{{ data.productDetail.name }}</div>
                                        <div class="d-flex align-items-end mt-15">
                                            <rating-group :rating="rating" />
                                            <div class="label">
                                                {{ data.productDetail.feedbackSet.edges.length }} feedbacks
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="bold text-uppercase">{{ data.productDetail.price }} aed</div>
                                        <div class="model">modal012031230</div>
                                    </div>
                                </div>
                                <div class="description">{{ data.productDetail.description }}</div>
                                <div class="mt-30">
                                    <div class="bold">Available colors</div>
                                    <div class="colors mt-15">
                                        <div
                                            class="color-group"
                                            v-for="(colorGroup, index) in colorsGroup"
                                            :key="index"
                                        >
                                            <input
                                                type="radio"
                                                v-model="colorVal"
                                                name="colors"
                                                :value="index"
                                                :id="colorGroup.node.color.id"
                                            />
                                            <label class="label-color mb-0" :for="colorGroup.node.color.id">
                                                <div
                                                    class="color"
                                                    :style="`background: ${colorGroup.node.color.color}`"
                                                ></div>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                                <div class="mt-30">
                                    <div class="bold">Sizes</div>
                                    <div class="sizes mt-15" v-if="currentSizes && currentSizes.length > 0">
                                        <div class="size-box" v-for="(size, index) in currentSizes" :key="index">
                                            <input
                                                type="radio"
                                                name="sizes"
                                                v-model="sizeVal"
                                                :value="size.node.id"
                                                :id="size.node.id"
                                            />
                                            <label class="label-size" :for="size.node.id">{{ size.node.name }}</label>
                                        </div>
                                        <a href.prevent class="modal-label mb-2">Size charts</a>
                                    </div>
                                </div>
                                <p class="size-description">
                                    The model is available in size S.<br />
                                    The parameters of the model:<br />
                                    Growth - 170 <br />
                                    Chest - 84<br />
                                    Waist - 61<br />
                                    Hips - 86<br />
                                </p>
                                <div class="row mt-60">
                                    <div class="col-6">
                                        <button class="btn btn-yellow">Add to cart</button>
                                    </div>
                                    <div class="col-6">
                                        <button class="btn btn-outline-yellow">Add to wishlist</button>
                                    </div>
                                </div>
                                <div class="row mt-30">
                                    <div class="col-auto">
                                        <nuxt-link class="link" to="/payment/" target="_blank"
                                            >Payment & Delivery</nuxt-link
                                        >
                                    </div>
                                    <div class="col-auto">
                                        <nuxt-link class="link" to="/returns/" target="_blank"
                                            >Returns & Refunds</nuxt-link
                                        >
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row bg-gray">
                            <div class="col-auto text-center">
                                <img src="~/assets/images/icons/delivery-truck.svg" />
                                <div class="text mw-290">Free shipping for all orders within UAE</div>
                            </div>
                            <div class="col-auto text-center">
                                <img src="~/assets/images/icons/cash.svg" />
                                <div class="text mw-310">
                                    We shall be happy to refund or exchange any items that aren't right for you. See our
                                    Returns & Refunds section for details
                                </div>
                            </div>
                            <div class="col-auto text-center">
                                <img src="~/assets/images/icons/comment.svg" />
                                <div class="text mw-290">If you have any questions please contact us</div>
                            </div>
                        </div>
                        <div class="bold text-uppercase mt-90">Reviews</div>
                        <div class="d-flex justify-content-between w-100">
                            <comment-group :id="data.productDetail.id" />
                            <div class="right-block mt-30">
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <rating-group :rating="rating" :size="20" />
                                    <div class="bold">{{ rating }}/5</div>
                                </div>
                                <template v-if="countRatings && countRatings.length > 0">
                                    <div
                                        class="feedback-count-group"
                                        v-for="(ratingGroup, index) in countRatings"
                                        :key="index"
                                    >
                                        <div class="label">{{ ratingGroup.label }}</div>
                                        <div class="progress">
                                            <div
                                                class="active-progress"
                                                :style="`width: ${ratingGroup.precent}%`"
                                            ></div>
                                        </div>
                                        <div class="label">{{ ratingGroup.count }}</div>
                                    </div>
                                </template>
                                <button class="btn btn-black">Write a rewiew</button>
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </ApolloQuery>
    </div>
</template>
<script>
    import CommentGroup from '../../components/comment/CommentGroup.vue';
    import RatingGroup from '../../components/comment/RatingGroup.vue';
    // import { Hooper, Slide } from 'hooper';
    import ProductCarousel from '../../components/product/ProductCarousel.vue';

    export default {
        name: 'product',
        components: { CommentGroup, RatingGroup, ProductCarousel },
        data() {
            return {
                rating: 0,
                countRatings: [],
                colorVal: 0,
                sizeVal: null,
                colorsGroup: [],
            };
        },
        computed: {
            currentSizes() {
                this.sizeVal = null;
                if (this.colorsGroup.length > 0) {
                    return this.colorsGroup[this.colorVal].node.sizes.edges;
                }
                return null;
            },
        },
        methods: {
            getRatingPrecent(feedbacks, rating) {
                return {
                    count: feedbacks.filter((obj) => obj.node.star == rating).length,
                    precent: Math.floor(
                        (parseInt(feedbacks.filter((obj) => obj.node.star == rating).length) /
                            parseInt(feedbacks.length)) *
                            100,
                    ),
                };
            },
            result(data) {
                if (data && data.data.productDetail) {
                    this.$store.commit('set_breadcrumbs', [
                        { link: 'index', name: 'Home' },
                        { link: 'catalog', name: 'Catalogue' },
                        { link: '', name: data.data.productDetail.name },
                    ]);
                    let feedbacks = data.data.productDetail.feedbackSet.edges;
                    if (feedbacks && feedbacks.length > 0) {
                        let rating = 0;

                        this.countRatings = [
                            { label: '5 stars', ...this.getRatingPrecent(feedbacks, 'STAR5') },
                            { label: '4 stars', ...this.getRatingPrecent(feedbacks, 'STAR4') },
                            { label: '3 stars', ...this.getRatingPrecent(feedbacks, 'STAR3') },
                            { label: '2 stars', ...this.getRatingPrecent(feedbacks, 'STAR2') },
                            { label: '1 star', ...this.getRatingPrecent(feedbacks, 'STAR1') },
                        ];

                        for (let i in feedbacks) {
                            rating = rating + parseInt(feedbacks[i].node.star.split('STAR')[1]);
                        }

                        this.rating = parseInt(rating / feedbacks.length);
                    }

                    this.colorsGroup = data.data.productDetail.productsizecolorSet.edges;
                } else {
                    this.$root.error({ statusCode: 404 });
                }
                return data;
            },
        },
    };
</script>
<style lang="less" scoped>
    .mt-90 {
        margin-top: 90px;
    }

    .bold {
        font-family: 'Inter-Medium';
        font-size: 24px;
        line-height: 29px;
        color: @black;
    }

    .mt-60 {
        margin-top: 60px;
    }

    .link {
        font-size: 14px;
        line-height: 17px;
        text-decoration: underline;
        color: @grey4;
    }

    .right-block {
        .bold {
            line-height: 15px;
            font-size: 18px;
        }

        .feedback-count-group {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 10px;

            .label {
                font-weight: 'Inter-Light';
                font-size: 12px;
                line-height: 14px;
                color: @black;
            }

            .progress {
                position: relative;
                width: 120px;
                height: 5px;
                background: @grey2;
                margin: 0px 5px;

                .active-progress {
                    position: absolute;
                    height: 100%;
                    left: 0;
                    background: @yellow;
                }
            }
        }

        .btn-black {
            width: 100%;
            margin-top: 30px;
            padding: 10px 27px;
        }
    }

    .bg-gray {
        display: flex;
        justify-content: space-between;
        padding: 30px 45px;
        margin-top: 60px;
        background: @grey3;

        .mw-290 {
            max-width: 290px;
        }

        .mw-310 {
            max-width: 310px;
        }

        .text {
            margin-top: 15px;
        }
    }

    .head-group {
        display: flex;
        justify-content: space-between;

        .label {
            font-family: 'Inter-Light';
            font-size: 14px;
            color: @grey4;
            margin-left: 10px;
            line-height: 14px;
        }

        .model {
            margin-top: 15px;
            font-family: 'Inter-Light';
            font-size: 14px;
            color: @grey4;
            line-height: 23px;
        }
    }

    .description {
        margin-top: 30px;
        font-family: 'Inter-Light';
        font-size: 18px;
        line-height: 22px;
        color: @black;
    }

    .colors {
        display: flex;
        flex-wrap: wrap;
        align-items: center;

        .color-group {
            margin-right: 20px;
        }
    }

    .size-description {
        margin: 25px 0px 0px 0px;
        font-size: 18px;
        line-height: 22px;
    }

    .modal-label {
        font-family: 'Inter-Light';
        font-size: 14px;
        line-height: 17px;
        text-decoration: underline;
        color: @grey4;
    }

    .btn-yellow {
        color: @white;
        background: @yellow;
        padding: 7px 60px;
        border: 1px solid @yellow;

        &:hover {
            background: #dab20e;
        }
    }

    .btn-outline-yellow {
        color: @yellow;
        background: @white;
        padding: 7px 47px;
        border: 1px solid @yellow;

        &:hover {
            background: #dab20e;
            color: @white;
        }
    }
</style>
