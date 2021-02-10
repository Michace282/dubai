<template>
    <div>
        <ApolloQuery
            :query="require('~/graphql/queries/product/productDetail.graphql')"
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
                                        colorsGroup[colorVal] &&
                                        colorsGroup[colorVal].node.productimageSet.edges.length > 0
                                    "
                                    :images="colorsGroup[colorVal].node.productimageSet.edges"
                                />
                                <img v-else src="~/assets/images/no-photo.jpg" />
                            </div>
                            <div class="col">
                                <div class="head-group">
                                    <div>
                                        <div class="bold text-uppercase">{{ data.productDetail.name }}</div>
                                        <div class="d-flex align-items-end mt-15">
                                            <rating-group :rating="Math.floor(data.productDetail.avgFeedback)" />
                                            <div class="label">
                                                {{ Math.floor(data.productDetail.countFeedback) }} feedbacks
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="bold text-uppercase">{{ data.productDetail.price }} aed</div>
                                        <div class="model">Model №{{ data.productDetail.article }}</div>
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
                                <p
                                    class="size-description"
                                    v-html="data.productDetail.modelDescription"
                                    v-if="data.productDetail.modelDescription"
                                ></p>
                                <div class="row mt-60">
                                    <div class="col-6">
                                        <button class="btn btn-yellow">Add to cart</button>
                                    </div>
                                    <div class="col-6">
                                        <button
                                            class="btn btn-outline-yellow"
                                            @click="
                                                toggleFavouriteMixin($route.params.slug, isFavorite)
                                            "
                                        >
                                            {{ wishListBtnLabel }}
                                        </button>
                                    </div>
                                </div>
                                <div class="row mt-30">
                                    <div class="col-auto">
                                        <nuxt-link class="link" to="/payment/" target="_blank"
                                            >Payment & Delivery
                                        </nuxt-link>
                                    </div>
                                    <div class="col-auto">
                                        <nuxt-link class="link" to="/returns/" target="_blank"
                                            >Returns & Refunds
                                        </nuxt-link>
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
                        <div v-if="data.productDetail.worksBestWith.edges.length > 0">
                            <div class="bold text-uppercase mt-90">Works best with</div>
                            <product-items-carousel class="mt-45" :items="data.productDetail.worksBestWith.edges" />
                        </div>
                        <ApolloQuery
                            :query="require('~/graphql/queries/product/productList')"
                            :variables="{ excludeId: $route.params.slug }"
                        >
                            <template v-slot="{ result: { error, data }, isLoading }">
                                <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                                <div
                                    v-else-if="data && data.productList && data.productList.edges.length > 0"
                                    class="result apollo"
                                >
                                    <div class="bold text-uppercase mt-90">You also may like</div>
                                    <product-items-carousel class="mt-45" :items="data.productList.edges" />
                                </div>
                            </template>
                        </ApolloQuery>
                        <product-items-carousel
                            class="mt-45"
                            v-if="data.productDetail.worksBestWith.edges.length > 0"
                            :items="data.productDetail.worksBestWith.edges"
                        />
                        <div class="bold text-uppercase mt-90">Reviews</div>
                        <comment-form
                            v-if="showForm"
                            class="mt-45"
                            :sizes="data.productDetail.sizeChart.sizeSet.edges"
                            :colors="colors"
                            :productId="$route.params.slug"
                            @hideForm="showForm = false"
                            @error="
                                (error) => {
                                    $bvToast.toast(error, {
                                        title: 'Review',
                                        variant: 'danger',
                                    });
                                }
                            "
                            @success="
                                $bvToast.toast('The review was sent for moderation', {
                                    title: 'Review',
                                    variant: 'success',
                                });
                                showForm = false;
                            "
                        />
                        <div class="d-flex justify-content-between w-100">
                            <comment-group />
                            <div class="right-block mt-30">
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <rating-group :rating="Math.floor(data.productDetail.avgFeedback)" :size="20" />
                                    <div class="bold">{{ Math.floor(data.productDetail.avgFeedback) }}/5</div>
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
                                <button class="btn btn-black" @click="showForm = true" v-if="$store.state.user.user">
                                    Write a rewiew
                                </button>
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
    import CommentForm from '../../components/comment/CommentForm.vue';
    import RatingGroup from '../../components/comment/RatingGroup.vue';
    import ProductCarousel from '../../components/product/ProductCarousel.vue';
    import ProductItemsCarousel from '../../components/product/ProductItemsCarousel.vue';
    import toggleFavouriteMixin from '~/mixins/toggleFavouriteMixin';

    export default {
        name: 'product',
        components: { CommentGroup, RatingGroup, ProductCarousel, ProductItemsCarousel, CommentForm },
        data() {
            return {
                countRatings: [],
                colorVal: 0,
                sizeVal: null,
                colorsGroup: [],
                metaData: null,
                showForm: false,
                isFavorite: null,
            };
        },
        mixins: [toggleFavouriteMixin],
        head() {
            return this.metaData;
        },
        computed: {
            wishListBtnLabel() {
                return this.isFavorite ? 'Remove from wish-list' : 'Add to wish-list';
            },
            colors() {
                if (this.colorsGroup.length > 0) {
                    let colors = [];
                    for (let i in this.colorsGroup) {
                        colors.push({
                            node: {
                                id: this.colorsGroup[i].node.color.id,
                                name: this.colorsGroup[i].node.color.name,
                            },
                        });
                    }
                    return colors;
                }
                return [];
            },
            currentSizes() {
                this.sizeVal = null;
                if (this.colorsGroup.length > 0) {
                    return this.colorsGroup[this.colorVal].node.sizes.edges;
                }
                return null;
            },
        },
        methods: {
            getRatingPrecent(feedbackCount, allFeedbacksCount) {
                return Math.floor((feedbackCount / allFeedbacksCount) * 100);
            },
            result(data) {
                if (data && data.data.productDetail) {
                    this.metaData = {
                        title: data.data.productDetail.name,
                        meta: [
                            {
                                hid: 'description',
                                name: 'description',
                                content: data.data.productDetail.description,
                            },
                        ],
                    };

                    if (this.isFavorite == null) {
                        this.isFavorite = data.data.productDetail.isWishlist;
                    }

                    let breadcrumbs = [
                        { route: '/', name: 'Home' },
                        { route: { name: 'catalog' }, name: 'Catalogue' },
                    ];

                    if (data.data.productDetail.productType && data.data.productProductType) {
                        data.data.productProductType.enumValues.forEach((v) => {
                            if (v.name == data.data.productDetail.productType) {
                                breadcrumbs.push({
                                    route: {
                                        name: 'catalog',
                                        query: { productType: data.data.productDetail.productType.toLowerCase() },
                                    },
                                    name: v.description,
                                });
                            }
                        });
                    }

                    if (data.data.productDetail.ladiesType && data.data.productLadiesType) {
                        data.data.productLadiesType.enumValues.forEach((v) => {
                            if (v.name == data.data.productDetail.ladiesType) {
                                breadcrumbs.push({
                                    route: {
                                        name: 'catalog',
                                        query: {
                                            productType: data.data.productDetail.productType.toLowerCase(),
                                            ladiesType: data.data.productDetail.ladiesType.toLowerCase(),
                                        },
                                    },
                                    name: v.description,
                                });
                            }
                        });
                    }

                    if (data.data.productDetail.mensType && data.data.productMensType) {
                        data.data.productMensType.enumValues.forEach((v) => {
                            if (v.name == data.data.productDetail.mensType) {
                                breadcrumbs.push({
                                    route: {
                                        name: 'catalog',
                                        query: {
                                            productType: data.data.productDetail.productType.toLowerCase(),
                                            mensType: data.data.productDetail.mensType.toLowerCase(),
                                        },
                                    },
                                    name: v.description,
                                });
                            }
                        });
                    }

                    if (data.data.productDetail.accessoriesType && data.data.productAccessoriesType) {
                        data.data.productAccessoriesType.enumValues.forEach((v) => {
                            if (v.name == data.data.productDetail.accessoriesType) {
                                breadcrumbs.push({
                                    route: {
                                        name: 'catalog',
                                        query: {
                                            productType: data.data.productDetail.productType.toLowerCase(),
                                            accessoriesType: data.data.accessoriesType.productType.toLowerCase(),
                                        },
                                    },
                                    name: v.description,
                                });
                            }
                        });
                    }

                    if (data.data.productDetail.danceShoesType && data.data.productDanceShoesType) {
                        data.data.productDanceShoesType.enumValues.forEach((v) => {
                            if (v.name == data.data.productDetail.danceShoesType) {
                                breadcrumbs.push({
                                    route: {
                                        name: 'catalog',
                                        query: {
                                            productType: data.data.productDetail.productType.toLowerCase(),
                                            danceShoesType: data.data.danceShoesType.productType.toLowerCase(),
                                        },
                                    },
                                    name: v.description,
                                });
                            }
                        });
                    }

                    breadcrumbs.push({ route: '', name: data.data.productDetail.name });
                    this.$store.commit('set_breadcrumbs', breadcrumbs);

                    if (data.data.productDetail.countFeedback > 0) {
                        this.countRatings = [];
                        for (let i = 5; i > 0; i--) {
                            this.countRatings.push({
                                label: `${i} stars`,
                                count: data.data.productDetail[`countFeedbackStar${i}`],
                                precent: this.getRatingPrecent(
                                    data.data.productDetail[`countFeedbackStar${i}`],
                                    data.data.productDetail.countFeedback,
                                ),
                            });
                        }
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
        width: 100%;
        color: @yellow;
        background: @white;
        padding: 7px 17px;
        border: 1px solid @yellow;

        &:hover {
            background: #dab20e;
            color: @white;
        }
    }
</style>
