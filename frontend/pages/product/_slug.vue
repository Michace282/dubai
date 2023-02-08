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
                <div v-if="isLoading || error" class="loading apollo mt-85">
                    <loader/>
                </div>
                <div v-else-if="data && data.productDetail" class="result apollo">
                    <div class="container">
                        <div class="row">
                            <div class="col-12 col-lg-7">
                                <div class="head-group d-block d-lg-none">
                                    <h1 class="bold text-uppercase">
                                        {{ data.productDetail.name }}
                                    </h1>
                                    <div class="model mt-15">Model №{{ data.productDetail.article }}</div>
                                </div>
                                <product-carousel
                                    v-if="
                                        colorsGroup[colorVal] &&
                                        colorsGroup[colorVal].node.productimageSet.edges.length > 0
                                    "
                                    :images="colorsGroup[colorVal].node.productimageSet.edges"
                                    :name="data.productDetail.name"
                                />
                                <img v-else src="~/assets/images/no-photo.jpg" alt="no photo"/>
                            </div>
                            <div class="col">
                                <div class="head-group mt-3 mt-lg-0 align-items-center align-items-lg-start">
                                    <div>
                                        <h1 class="bold text-uppercase d-none d-lg-block">
                                            {{ data.productDetail.name }}
                                        </h1>
                                        <div class="d-flex align-items-end mt-0 mt-lg-3">
                                            <rating-group :rating="Math.floor(data.productDetail.avgFeedback)"/>
                                            <div class="label">
                                                {{ Math.floor(data.productDetail.countFeedback) }} feedbacks
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="bold text-uppercase">{{ data.productDetail.price }} aed</div>
                                        <div class="model d-none d-lg-block">
                                            Model №{{ data.productDetail.article }}
                                        </div>
                                    </div>
                                </div>
                                <div class="description" v-html="data.productDetail.description"></div>
                                <div class="mt-30">
                                    <h2 class="bold">Available colors</h2>
                                    <div class="colors mt-15">
                                        <div
                                            class="color-group"
                                            v-for="(colorGroup, index) in colorsGroup"
                                            :key="'color' + index"
                                        >
                                            <input
                                                type="radio"
                                                v-model="colorVal"
                                                name="colors"
                                                :value="index"
                                                :id="colorGroup.node.color.id"
                                            />
                                            <label class="label-color mb-0" :for="colorGroup.node.color.id"
                                                   v-b-tooltip.hover :title="colorGroup.node.color.name">
                                                <div
                                                    class="color"
                                                    :style="
                                                        colorGroup.node.color.image
                                                            ? 'background-image: url(' +
                                                              colorGroup.node.color.image +
                                                              ')'
                                                            : 'background:' + colorGroup.node.color.color
                                                    "
                                                ></div>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                                <div class="mt-30">
                                    <h2 class="bold">Sizes</h2>
                                    <div class="sizes mt-15" v-if="currentSizes && currentSizes.length > 0">
                                        <div
                                            class="size-box"
                                            v-for="(size, index) in currentSizes"
                                            v-if="size.node.isAvailable"
                                            :key="'size' + index"
                                        >
                                            <input
                                                type="radio"
                                                name="sizes"
                                                v-model="sizeVal"
                                                :value="index"
                                                :id="size.node.size.id"
                                                :disabled="size.node.count == 0"
                                            />
                                            <label class="label-size" :for="size.node.size.id">{{
                                                    size.node.size.name
                                                }}</label>
                                        </div>
                                        <a
                                            href.prevent
                                            class="modal-label mb-2"
                                            v-if="data.productDetail.sizeChart.table"
                                            v-b-modal.size-chart-modal
                                        >Size charts</a
                                        >
                                    </div>
                                </div>
                                <p
                                    class="size-description"
                                    v-html="data.productDetail.modelDescription"
                                    v-if="data.productDetail.modelDescription"
                                ></p>
                                <div class="row mt-60">
                                    <div class="col-6" v-if="isAvailableSizes && data.productDetail.productType.toLowerCase() !== 'performance_costumes'">
                                        <button
                                            class="btn btn-yellow"
                                            @click="
                                                colorsGroup && colorsGroup[colorVal].node.isAvailable
                                                    ? addToBasket()
                                                    : ''
                                            "
                                            :disabled="!colorsGroup || !colorsGroup[colorVal].node.isAvailable"
                                        >
                                            Add to cart
                                        </button>
                                    </div>
                                    <div class="col-6" v-if="data.productDetail.productType.toLowerCase() == 'performance_costumes'">
                                        <button
                                            class="btn btn-black"
                                            @click="showModalPurchase(data.productDetail.name)"
                                        >
                                           Request a purchase
                                        </button>
                                    </div>
                                    <div class="col-6" v-else>
                                        <button
                                            class="btn btn-disabled"
                                            :disabled="true"
                                        >
                                            Coming again soon
                                        </button>
                                    </div>
                                    <div class="col-6">
                                        <button
                                            class="btn btn-outline-yellow"
                                            @click="toggleFavouriteMixin($route.params.slug, isFavorite)"
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
                                <img src="~/assets/images/icons/delivery-truck.svg" alt="delivery"/>
                                <div class="text mw-290">Free shipping for all orders within UAE</div>
                            </div>
                            <div class="col-auto text-center">
                                <img src="~/assets/images/icons/cash.svg" alt="cash"/>
                                <div class="text mw-310">
                                    We shall be happy to refund or exchange any items that aren't right for you. See our
                                    Returns & Refunds section for details
                                </div>
                            </div>
                            <div class="col-auto text-center comment-block">
                                <img src="~/assets/images/icons/comment.svg" alt="comment"/>
                                <div class="text mw-290">If you have any questions please contact us</div>
                            </div>
                        </div>
                        <div v-if="data.productDetail.worksBestWith.edges.length > 0">
                            <div class="bold text-uppercase mt-90">Works best with</div>
                            <product-items-carousel class="mt-45" :items="data.productDetail.worksBestWith.edges"/>
                        </div>
                        <ApolloQuery
                            :query="require('~/graphql/queries/product/productList')"
                            :variables="{ excludeId: $route.params.slug, first: 10}"
                        >
                            <template v-slot="{ result: { error, data }, isLoading }">
                                <div v-if="isLoading || error" class="loading apollo mt-85"></div>
                                <div
                                    v-else-if="data && data.productList && data.productList.edges.length > 0"
                                    class="result apollo"
                                >
                                    <div class="bold text-uppercase mt-90">You also may like</div>
                                    <product-items-carousel class="mt-45" :items="data.productList.edges"/>
                                </div>
                            </template>
                        </ApolloQuery>
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
                        <button
                            class="btn btn-black d-block d-lg-none mt-15"
                            @click="showForm = true"
                            v-if="$store.state.user.user && !showForm"
                        >
                            Write a rewiew
                        </button>
                        <div class="d-flex justify-content-between w-100">
                            <comment-group :id="$route.params.slug" />
                            <div class="right-block mt-30 d-none d-lg-block">
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <rating-group :rating="Math.floor(data.productDetail.avgFeedback)" :size="20"/>
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
                    <b-modal id="size-chart-modal" hide-footer centered>
                        <template #modal-header="{ close }">
                            <h5 class="title">Size charts for ladies clothing</h5>
                            <a href.prevent @click="close()">
                                <svg
                                    width="15"
                                    height="15"
                                    viewBox="0 0 15 15"
                                    fill="none"
                                    xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path
                                        d="M8.32868 7.501L14.8284 1.00127C15.0572 0.772428 15.0572 0.401413 14.8284 0.172605C14.5996 -0.0562035 14.2285 -0.0562328 13.9997 0.172605L7.49999 6.67234L1.00029 0.172605C0.771451 -0.0562328 0.400436 -0.0562328 0.171628 0.172605C-0.0571801 0.401442 -0.0572094 0.772457 0.171628 1.00127L6.67133 7.50097L0.171628 14.0007C-0.0572094 14.2295 -0.0572094 14.6006 0.171628 14.8294C0.286032 14.9438 0.436003 15.001 0.585973 15.001C0.735943 15.001 0.885885 14.9438 1.00032 14.8294L7.49999 8.32966L13.9997 14.8294C14.1141 14.9438 14.2641 15.001 14.414 15.001C14.564 15.001 14.714 14.9438 14.8284 14.8294C15.0572 14.6005 15.0572 14.2295 14.8284 14.0007L8.32868 7.501Z"
                                        fill="#808080"
                                    />
                                </svg>
                            </a>
                        </template>
                        <div v-html="data.productDetail.sizeChart.table"></div>
                    </b-modal>
                </div>
            </template>
        </ApolloQuery>
        <b-modal
                id="purchase-modal"
                ref="purchase-modal"
                hide-footer
                centered
            >
                <template #modal-header="{ close }">
                    <h5 class="title purchace-title" ref="purchaseTitle" v-html="confirmModalText"></h5>
                    <a href.prevent @click="close()">
                        <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M8.32868 7.501L14.8284 1.00127C15.0572 0.772428 15.0572 0.401413 14.8284 0.172605C14.5996 -0.0562035 14.2285 -0.0562328 13.9997 0.172605L7.49999 6.67234L1.00029 0.172605C0.771451 -0.0562328 0.400436 -0.0562328 0.171628 0.172605C-0.0571801 0.401442 -0.0572094 0.772457 0.171628 1.00127L6.67133 7.50097L0.171628 14.0007C-0.0572094 14.2295 -0.0572094 14.6006 0.171628 14.8294C0.286032 14.9438 0.436003 15.001 0.585973 15.001C0.735943 15.001 0.885885 14.9438 1.00032 14.8294L7.49999 8.32966L13.9997 14.8294C14.1141 14.9438 14.2641 15.001 14.414 15.001C14.564 15.001 14.714 14.9438 14.8284 14.8294C15.0572 14.6005 15.0572 14.2295 14.8284 14.0007L8.32868 7.501Z"
                                fill="#808080"
                            />
                        </svg>
                    </a>
                </template>
                <purchase-form btnName="purchace" @buy="requestPurchace">
                </purchase-form>
            </b-modal>
    </div>
</template>
<script>
    import CommentGroup from '../../components/comment/CommentGroup.vue';
    import CommentForm from '../../components/comment/CommentForm.vue';
    import RatingGroup from '../../components/comment/RatingGroup.vue';
    import ProductCarousel from '../../components/product/ProductCarousel.vue';
    import ProductItemsCarousel from '../../components/product/ProductItemsCarousel.vue';
    import toggleFavouriteMixin from '~/mixins/toggleFavouriteMixin';
    import Loader from '../../components/Loader.vue';
    import PurchaseForm from '../../components/PurchaseForm.vue';

    export default {
        name: 'product',
        components: {CommentGroup, RatingGroup, ProductCarousel, ProductItemsCarousel, CommentForm, PurchaseForm, Loader},
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
                    let sizes = this.colorsGroup[this.colorVal].node.productsizecolorsizeSet.edges;
                    for (let i in sizes) {
                        if (sizes[i].node.count > 0 && sizes[i].node.isAvailable) {
                            this.sizeVal = i;
                            break;
                        }
                    }
                    return sizes;
                }
                return null;
            },
            isAvailableSizes() {
                let isAvailable = false;
                for (let i in this.currentSizes) {
                    if (this.currentSizes[i].node.isAvailable && this.currentSizes[i].node.count > 0) {
                        isAvailable = true;
                        break;
                    }
                }
                return isAvailable
            }
        },
        methods: {
            showModalPurchase(name) {
                let v = this;
                v.confirmModalText = 'Request Purchace of ' + name;
                v.$refs['purchase-modal'].show();
            },

            requestPurchace(formInfo) {
                let v = this;
                let purchaseRequest = {
                    productName: v.$refs['purchaseTitle'].innerText, 
                    firstName: formInfo.firstName,
                    lastName: formInfo.lastName,
                    email: formInfo.email,
                    phone: formInfo.phone,
                };
                this.$apollo
                    .mutate({
                        mutation: require('~/graphql/mutations/order/purchaseRequest.graphql'),
                        variables: {
                            purchaseRequest: purchaseRequest
                        },
                    })
                    .then((data) => {
                        v.$bvToast.toast('Your request has been placed! In the near future, our Manager will contact you.', {
                            title: 'Request purchase',
                            variant: 'success',
                        });
                        v.$refs['purchase-modal'].hide();
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
            addToBasket() {
                let v = this;
                if (v.colorVal != null && v.sizeVal != null) {
                    let basket = v.$cookies.get('basket') ? v.$cookies.get('basket') : {};
                    let product = {
                        id: `${v.$route.params.slug}_${v.colorsGroup[v.colorVal].node.color.id}_${
                            v.currentSizes[v.sizeVal].node.size.id
                        }`,
                        color: v.colorsGroup[v.colorVal].node.color.id,
                        size: v.currentSizes[v.sizeVal].node.size.id,
                        product: this.$route.params.slug,
                        count: 1,
                    };
                    if (basket[product.id] && basket[product.id].count < v.currentSizes[v.sizeVal].node.count) {
                        basket[product.id].count += 1;
                    } else if (basket[product.id]) {
                        v.$bvToast.toast('You have added the maximum number of products available', {
                            title: 'Add to cart',
                            variant: 'danger',
                        });
                        return 0;
                    } else {
                        basket[product.id] = product;
                    }
                    v.$cookies.set('basket', JSON.stringify(basket));
                    v.$store.commit('product/update_items_count');
                    v.$bvToast.toast('The product was successfully added to the cart', {
                        title: 'Add to cart',
                        variant: 'success',
                    });
                } else {
                    v.$bvToast.toast('Failed to add the item to your cart', {
                        title: 'Add to cart',
                        variant: 'danger',
                    });
                }
            },
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
                        {route: '/', name: 'Home'},
                        {route: {name: 'catalog'}, name: 'Catalogue'},
                    ];

                    if (data.data.productDetail.productType && data.data.productProductType) {
                        data.data.productProductType.enumValues.forEach((v) => {
                            if (v.name == data.data.productDetail.productType) {
                                breadcrumbs.push({
                                    route: {
                                        name: 'catalog-product',
                                        params: {product: data.data.productDetail.productType.toLowerCase()},
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
                                        name: 'catalog-product-type',
                                        params: {
                                            product: data.data.productDetail.productType.toLowerCase(),
                                            type: data.data.productDetail.ladiesType.toLowerCase(),
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
                                        name: 'catalog-product-type',
                                        params: {
                                            product: data.data.productDetail.productType.toLowerCase(),
                                            type: data.data.productDetail.mensType.toLowerCase(),
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
                                        name: 'catalog-product-type',
                                        params: {
                                            product: data.data.productDetail.productType.toLowerCase(),
                                            type: data.data.productDetail.accessoriesType.toLowerCase(),
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
                                        name: 'catalog-product-type',
                                        params: {
                                            product: data.data.productDetail.productType.toLowerCase(),
                                            type: data.data.productDetail.danceShoesType.toLowerCase(),
                                        },
                                    },
                                    name: v.description,
                                });
                            }
                        });
                    }

                    breadcrumbs.push({route: '', name: data.data.productDetail.name});
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
                    this.$root.error({statusCode: 404});
                }
                return data;
            },
        },
    };
</script>
<style lang="less">
    .tooltip.b-tooltip{
        opacity: 1;
    }
    .tooltip-inner {
        font-family: Inter;
        background: #FFFFFF;
        border: 1px solid #E6E6E6;
        border-radius: 2px;
        font-weight: 300;
        font-size: 12px;
        line-height: 15px;
        color: rgba(0, 0, 0, 0.5);
    }

    .bs-tooltip-top .arrow::before {
        border-top-color: #E6E6E6;
    }


    #size-chart-modal {
        background: @grey_opacity;

        .modal-dialog {
            max-width: 790px;

            .modal-content {
                background: @grey3;
                border: none;
                border-radius: unset;

                table {
                    border: none;

                    tr {
                        &:nth-child(odd) {
                            background: @white;
                        }

                        td {
                            border: none;
                            padding: 9px 10px;
                            text-align: center;
                            font-family: 'Inter-Light';
                            font-size: 18px;
                            line-height: 22px;
                            color: @black;
                        }
                    }
                }

                .modal-header {
                    padding: 30px;
                    border: 0px;

                    a {
                        cursor: pointer;
                    }

                    h5 {
                        font-size: 24px;
                        line-height: 29px;
                        text-transform: uppercase;
                        color: @black;
                    }
                }

                .modal-body {
                    padding: 0px 30px 30px 30px;
                }
            }
        }
    }
</style>
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

        @media @extraLarge {
            justify-content: center;
        }

        @media @large {
            padding: 30px 20px;
        }

        @media @small {
            justify-content: space-between;
        }

        .col-auto {
            &:nth-child(2) {
                @media @large {
                    margin-top: 35px;
                    order: 3;
                }
            }

            @media @small {
                padding: 0px;
            }
        }

        img {
            @media @large {
                width: 30px;
            }
        }

        .mw-290 {
            max-width: 290px;

            @media @large {
                max-width: 155px;
            }
        }

        .mw-310 {
            max-width: 310px;
        }

        .text {
            margin-top: 15px;

            @media @large {
                font-size: 12px;
                margin-top: 5px;
            }
        }

        .comment-block {
            @media @extraLarge {
                margin-top: 35px;
            }

            @media @large {
                margin-top: 0px;
            }
        }
    }

    .head-group {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;

        .label {
            font-family: 'Inter-Light';
            font-size: 14px;
            color: @grey4;
            margin-left: 10px;
            line-height: 14px;
        }

        .model {
            margin-top: 12px;
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
        cursor: pointer;
    }

    .btn-yellow {
        width: 100%;
        color: @white;
        background: @yellow;
        padding: 7px 10px;
        border: 1px solid @yellow;

        &:hover {
            background: #dab20e;
        }
    }

    .btn-disabled {
        width: 100%;
        color: @white;
        background: rgba(128, 128, 128, 0.5);
        padding: 7px 10px;
        border: 1px solid rgba(128, 128, 128, 0.5);
        text-transform: uppercase;
    }

    .btn-outline-yellow {
        width: 100%;
        color: @yellow;
        background: @white;
        padding: 7px 17px;
        border: 1px solid @yellow;

        &:not(:disabled):hover {
            background: #dab20e;
            color: @white;
        }
    }
</style>
