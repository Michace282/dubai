<template>
    <div class="product">
        <a hrev.prevent class="favorites-icon"><img src="~/assets/images/icons/favorites-icon.svg" /></a>
        <client-only v-if="activePreviewImages && activePreviewImages.length > 0">
            <b-carousel
                :interval="0"
                indicators
                v-model="slide"
                class="product-carousel"
                :class="{ 'white-mode': false }"
                img-width="255"
                img-height="300"
            >
                <b-carousel-slide v-for="(img, index) in activePreviewImages" :key="index">
                    <template #img>
                        <img class="d-block img-fluid w-100 preview" :src="img.image" :alt="index" />
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
                default: null
            },
        },
        data() {
            return {
                activeColor: 0,
                slide: 0,
            };
        },
        computed: {
            activePreviewImages() {
                if (
                    this.colorsGroup &&
                    this.colorsGroup.edges[this.activeColor] &&
                    this.colorsGroup.edges[this.activeColor].node.color &&
                    this.colorsGroup.edges[this.activeColor].node.color.productsizecolorSet.edges
                ) {
                    let imagesGroup = this.colorsGroup.edges[this.activeColor].node.color.productsizecolorSet.edges;
                    let images = [];
                    this.slide = 0;
                    for (let i in imagesGroup) {
                        if (imagesGroup[i].node.productimageSet.edges.length > 0) {
                            for (let j in imagesGroup[i].node.productimageSet.edges) {
                                images.push(imagesGroup[i].node.productimageSet.edges[j].node);
                            }
                        }
                    }

                    return images;
                }
                return null;
            },
        },
    };
</script>

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
