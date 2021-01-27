<template>
    <div class="position-relative">
        <a hrev.prevent class="favorites-icon"><img src="~/assets/images/icons/favorites-icon.svg" /></a>
        <b-carousel
            :interval="3000"
            v-model="slide"
            indicators
            class="product-carousel"
            :class="{ 'white-mode': images[slide].type == 1 }"
            img-width="255"
            img-height="300"
        >
            <b-carousel-slide v-for="(img, index) in images" :key="index">
                <template #img>
                    <img
                        class="d-block img-fluid w-100"
                        width="1024"
                        height="480"
                        :src="require(`~/assets/images/${img.url}`)"
                        alt="image"
                    />
                </template>
            </b-carousel-slide>
        </b-carousel>
        <div class="colors">
            <div class="color-box">
                <div class="color"></div>
            </div>
        </div>
        <nuxt-link to="" class="link-to-product">
            <span class="name">{{ name }}</span>
            <span class="price">{{ price }} AED</span>
        </nuxt-link>
    </div>
</template>
<script>
    export default {
        name: 'ProductItem',
        props: {
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
        },
        data() {
            return {
                slide: 0,
                images: [
                    {
                        url: 'product-preview.png',
                        type: 0,
                    },
                    {
                        url: 'product-preview2.png',
                        type: 1,
                    },
                ],
            };
        },
    };
</script>

<style lang="less" scoped>
    @import '../../assets/css/variables';

    .link-to-product {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        color: @black;
        font-style: normal;
        margin-top: 10px;

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
        margin-top: 15px;

        .color-box {
            width: 20px;
            height: 20px;
            padding: 2px;
            border-radius: 50%;
            border: 1px solid @grey2;
            margin-right: 10px;

            .color {
                background: red;
                border-radius: 50%;
            }
        }
    }

    .favorites-icon {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 100;
        cursor: pointer;
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

                &.active {
                    width: 15px;
                    height: 5px;
                    background: rgba(0, 0, 0, 0.6);
                }
            }
        }
    }
</style>
