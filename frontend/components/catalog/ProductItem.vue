<template>
    <div class="product">
        <a hrev.prevent class="favorites-icon" @click="toggleFavourite(id)">
            <img src="~/assets/images/icons/favorites-fill.svg" v-if="isFavourite" />
            <img src="~/assets/images/icons/favorites-icon.svg" v-else />
        </a>
        <client-only v-if="colorsGroup && colorsGroup.edges[activeColor].node.productimageSet.edges.length > 0">
            <b-carousel
                :interval="0"
                indicators
                v-model="slide"
                class="product-carousel"
                :class="{ 'white-mode': false }"
                img-width="255"
                img-height="300"
            >
                <b-carousel-slide
                    v-for="(img, index) in colorsGroup.edges[activeColor].node.productimageSet.edges"
                    :key="index"
                >
                    <template #img>
                        <img class="d-block img-fluid w-100 preview" :src="img.node.image" :alt="index" />
                    </template>
                </b-carousel-slide>
            </b-carousel>
        </client-only>
        <img class="preview" src="~/assets/images/no-photo.jpg" v-else />
        <div class="colors" v-if="colorsGroup && colorsGroup.edges.length > 0">
            <div class="color-group" v-for="(colorGroup, index) in colorsGroup.edges" :key="index">
                <input type="radio" v-model="activeColor" :value="index" :id="colorGroup.node.id" />
                <label class="label-color" :for="colorGroup.node.id">
                    <div class="color" :style="`background: ${colorGroup.node.color.color}`"></div>
                </label>
            </div>
        </div>
        <nuxt-link :to="{ name: 'product-slug', params: { slug: id } }" class="link-to-product">
            <span class="name">{{ name }}</span>
            <span class="price">{{ price }} AED</span>
        </nuxt-link>
    </div>
</template>
<script>
    export default {
        name: 'ProductItem',
        props: {
            id: {
                type: String,
                required: true,
                default: '',
            },
            name: {
                type: String,
                required: true,
                default: '',
            },
            price: {
                type: Number,
                required: true,
                default: null,
            },
            colorsGroup: {
                type: Object,
                required: false,
                default: null,
            },
            isWishlist: {
                type: Boolean,
                required: true,
                default: false,
            },
        },
        data() {
            return {
                isFavourite: this.isWishlist,
                activeColor: 0,
                slide: 0,
            };
        },
        mounted() {
            if (sessionStorage.getItem('isFavorite' + this.id) == 'false') {
                this.isFavourite = false;
            } else if (sessionStorage.getItem('isFavorite' + this.id) == 'true') {
                this.isFavourite = true;
            }
        },
        methods: {
            toggleFavourite(id) {
                if (this.isFavourite) {
                    this.$apollo
                        .mutate({
                            mutation: require('~/graphql/mutations/favourite/productWishlistDelete.graphql'),
                            variables: {
                                guestUuid: this.$store.state.user.guestUuid,
                                product: id,
                            },
                        })
                        .then((data) => {
                            if (data && data.data.productWishlistDelete.errors.length == 0) {
                                this.isFavourite = false;
                                sessionStorage.setItem('isFavorite' + this.id, false);
                                this.$emit('refetch');
                            } else {
                                this.$bvToast.toast(data.data.productWishlistDelete.errors[0].messages, {
                                    title: 'Favourites',
                                    variant: 'danger',
                                });
                            }
                        });
                } else {
                    this.$apollo
                        .mutate({
                            mutation: require('~/graphql/mutations/favourite/productWishlistCreate.graphql'),
                            variables: {
                                guestUuid: this.$store.state.user.guestUuid,
                                product: id,
                            },
                        })
                        .then((data) => {
                            if (data && data.data.productWishlistCreate.errors.length == 0) {
                                this.isFavourite = true;
                                sessionStorage.setItem('isFavorite' + this.id, true);
                            } else {
                                this.$bvToast.toast(data.data.productWishlistCreate.errors[0].messages, {
                                    title: 'Favourites',
                                    variant: 'danger',
                                });
                            }
                        });
                }
            },
        },
    };
</script>
<style lang="less" scoped>
    .product {
        &.product-sm {
            .preview {
                max-height: 220px;
            }

            .name,
            .price {
                font-size: 14px;
            }

            .colors {
                .color-group {
                    width: 18px;
                    height: 18px;
                }
            }
        }
    }
</style>
<style lang="less" scoped>
    .product {
        position: relative;
        margin-bottom: 30px;

        .preview {
            width: 100%;
            height: 300px;
            object-fit: cover;

            @media (max-width: 767px) {
                height: 230px;
            }
        }

        .link-to-product {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            color: @black;
            font-style: normal;
            margin-top: 10px;

            @media @medium {
                font-size: 13px;
            }

            .name {
                font-family: 'Inter-Light';
            }

            .price {
                font-family: 'Inter-Light';
                font-weight: 600;
            }
        }

        .colors {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 10px;

            .color-group {
                width: 22px;
                height: 22px;
                margin-right: 10px;

                .label-color {
                    width: 100%;
                    height: 100%;
                }

                @media @medium {
                    width: 13px;
                    height: 13px;
                }
            }
        }

        .favorites-icon {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 100;
            cursor: pointer;

            img {
                width: 20px;
            }

            @media @medium {
                top: 5px;
                right: 5px;
            }
        }
    }
</style>

<style lang="less">
    .product-carousel {
        &.white-mode {
            .carousel-indicators {
                li {
                    background: rgba(255, 255, 255, 0.3);

                    &.active {
                        background: rgba(255, 255, 255, 0.6);
                    }
                }
            }
        }

        .carousel-indicators {
            li {
                width: 10px;
                height: 4px;
                margin: 0px 2px;
                border-radius: 5px;
                background: rgba(0, 0, 0, 0.3);
                @media @small {
                    width: 7px;
                    height: 2px;
                }

                &.active {
                    width: 15px;
                    height: 5px;
                    background: rgba(0, 0, 0, 0.6);

                    @media @small {
                        width: 14px;
                        height: 3px;
                    }
                }
            }
        }
    }
</style>
