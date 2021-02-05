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
                            <div class="col-7"></div>
                            <div class="col">
                                <div class="head-group">
                                    <div>
                                        <div class="bold text-uppercase">{{ data.productDetail.name }}</div>
                                        <div class="rating-group">
                                            <div class="rating">
                                                <svg
                                                    v-for="i in rating"
                                                    :key="i + 'fill'"
                                                    :class="{ 'mr-0': i == rating }"
                                                    width="15"
                                                    height="15"
                                                    viewBox="0 0 15 15"
                                                    fill="none"
                                                    xmlns="http://www.w3.org/2000/svg"
                                                >
                                                    <path
                                                        d="M14.5405 5.37391L10.0383 4.72674L8.01238 0.646688C7.87692 0.366946 7.54031 0.250019 7.26056 0.385528C7.1466 0.440733 7.05455 0.532723 6.9994 0.646688L4.97346 4.72674L0.471314 5.37391C0.258088 5.408 0.0831554 5.56101 0.0211103 5.76783C-0.03361 5.96711 0.01971 6.18049 0.161789 6.3306L3.42583 9.51025L2.66611 13.9842C2.6319 14.199 2.71835 14.4151 2.89123 14.547C3.06148 14.6765 3.29049 14.6983 3.48212 14.6033L7.50589 12.4648L11.5297 14.6033L11.7829 14.6596C11.9061 14.67 12.0282 14.6293 12.1205 14.547C12.2934 14.4151 12.3799 14.199 12.3457 13.9842L11.5859 9.51025L14.85 6.3306C14.9921 6.18049 15.0454 5.96711 14.9907 5.76783C14.9286 5.56107 14.7537 5.408 14.5405 5.37391Z"
                                                        fill="#E6C643"
                                                    />
                                                </svg>

                                                <svg
                                                    v-for="i in 5 - rating"
                                                    :key="i"
                                                    width="15"
                                                    height="15"
                                                    viewBox="0 0 15 15"
                                                    fill="none"
                                                    xmlns="http://www.w3.org/2000/svg"
                                                >
                                                    <path
                                                        d="M14.5405 5.37391L10.0383 4.72674L8.01238 0.646688C7.87692 0.366946 7.54031 0.250019 7.26056 0.385528C7.1466 0.440733 7.05456 0.532723 6.9994 0.646688L4.97346 4.72674L0.471314 5.37391C0.258088 5.408 0.0831554 5.56101 0.0211103 5.76783C-0.03361 5.96711 0.01971 6.18049 0.161789 6.3306L3.42583 9.51025L2.66611 13.9842C2.6319 14.199 2.71835 14.4151 2.89123 14.547C3.06148 14.6765 3.29049 14.6983 3.48212 14.6033L7.50589 12.4648L11.5297 14.6033L11.7829 14.6596C11.9061 14.67 12.0282 14.6293 12.1205 14.547C12.2934 14.4151 12.3799 14.199 12.3457 13.9842L11.5859 9.51025L14.85 6.3306C14.9921 6.18049 15.0454 5.96711 14.9907 5.76783C14.9286 5.56107 14.7537 5.408 14.5405 5.37391ZM10.573 8.91936C10.4578 9.05024 10.4063 9.22533 10.4323 9.39773L11.0513 13.0557L7.75913 11.3393C7.59885 11.2632 7.41293 11.2632 7.25265 11.3393L3.96043 13.0557L4.57948 9.39773C4.60544 9.22533 4.55396 9.05029 4.43881 8.91936L1.76564 6.33065L5.45178 5.796C5.63296 5.76417 5.78904 5.64972 5.87387 5.48647L7.50589 2.16615L9.13791 5.48647C9.22274 5.64972 9.37877 5.76417 9.56 5.796L13.2461 6.33065L10.573 8.91936Z"
                                                        fill="#E6C643"
                                                    />
                                                </svg>
                                            </div>
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
                    </div>
                </div>
            </template>
        </ApolloQuery>
    </div>
</template>
<script>
    export default {
        name: 'product',
        data() {
            return {
                rating: 0,
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
            result(data) {
                if (data && data.data.productDetail) {
                    this.$store.commit('set_breadcrumbs', [
                        { link: 'index', name: 'Home' },
                        { link: 'catalog', name: 'Catalogue' },
                        { link: '', name: data.data.productDetail.name },
                    ]);
                    let feedbacks = data.data.productDetail.feedbackSet.edges;
                    let rating = 0;
                    for (let i in feedbacks) {
                        rating = rating + parseInt(feedbacks[i].node.star.split('STAR')[1]);
                    }
                    this.rating = parseInt(rating / feedbacks.length);
                    this.colorsGroup = data.data.productDetail.productsizecolorSet.edges;
                } else {
                    this.$root.error({ statusCode: 404 });
                }
            },
        },
    };
</script>
<style lang="less" scoped>
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

        .rating-group {
            display: flex;
            align-items: center;
            margin-top: 15px;

            .rating {
                svg {
                    margin-right: 3px;
                }
            }

            .label {
                font-family: 'Inter-Light';
                font-size: 14px;
                line-height: 17px;
                color: @grey4;
                margin-left: 10px;
            }
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
