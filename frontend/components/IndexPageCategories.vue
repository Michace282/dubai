<template>
    <div class="mt-45">
        <div class="row categories">
            <div class="col-auto">
                <nuxt-link :to="{ name: 'catalog', query: { productType: 'ladies' } }" class="category vertical-large">
                    <div class="name">Ladies</div>
                </nuxt-link>
            </div>
            <div class="col-auto">
                <nuxt-link
                    :to="{ name: 'catalog', query: { productType: 'accessories' } }"
                    class="category horizontal text-left"
                >
                    <div class="name">Accessories</div>
                </nuxt-link>
                <nuxt-link
                    :to="{ name: 'catalog', query: { productType: 'dance_shoes' } }"
                    class="category horizontal text-right"
                >
                    <div class="name">Danceshoes</div>
                </nuxt-link>
            </div>
            <div class="col-auto">
                <nuxt-link :to="{ name: 'catalog', query: { productType: 'mens' } }" class="category vertical">
                    <div class="name">Mens</div>
                </nuxt-link>
            </div>
        </div>
        <client-only>
            <b-carousel id="carousel-2" :interval="4000" indicators class="categories-carousel">
                <b-carousel-slide img-src="~/assets/images/accessories.png">
                    <nuxt-link :to="{ name: 'catalog', query: { productType: 'accessories' } }"></nuxt-link>
                </b-carousel-slide>
                <b-carousel-slide img-src="~/assets/images/danceshoes.png">
                    <nuxt-link :to="{ name: 'catalog', query: { productType: 'dance_shoes' } }"></nuxt-link>
                </b-carousel-slide>
                <b-carousel-slide img-src="~/assets/images/ladies.png">
                    <nuxt-link :to="{ name: 'catalog', query: { productType: 'ladies' } }"></nuxt-link>
                </b-carousel-slide>
                <b-carousel-slide img-src="~/assets/images/mens.png">
                    <nuxt-link :to="{ name: 'catalog', query: { productType: 'mens' } }"></nuxt-link>
                </b-carousel-slide>
            </b-carousel>
        </client-only>
    </div>
</template>
<script>
    export default {
        name: 'IndexPageCategories',
    };
</script>
<style lang="less">
    .categories-carousel {
        display: none;

        @media (max-width: 767px) {
            display: block;
        }

        .carousel-caption,
        .carousel-caption a {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
        }
    }
</style>
<style lang="less" scoped>
    .categories {
        justify-content: center;

        @media (max-width: 767px) {
            display: none;
        }

        .category {
            position: relative;
            display: block;
            background: @grey;
            text-decoration: none !important;

            .name {
                font-family: 'Inter-Medium';
                font-size: 24px;
                line-height: 29px;
                text-transform: uppercase;
                color: @black;
                z-index: 10;

                @media (max-width: 1199px) {
                    font-size: 18px;
                }

                &:after {
                    position: absolute;
                    z-index: -1;
                    text-transform: uppercase;
                    font-size: 48px;
                    color: @grey2;

                    @media (max-width: 1199px) {
                        font-size: 28px;
                    }
                }
            }

            &.vertical {
                width: 255px;
                height: 530px;

                @media (max-width: 1199px) {
                    width: 150px;
                    height: 330px;
                }

                .name {
                    position: absolute;
                    top: 111px;
                    left: 40px;

                    @media (max-width: 1199px) {
                        top: 64px;
                        left: 20px;
                    }

                    &:after {
                        content: 'Mens';
                        top: -17px;
                        left: -30px;

                        @media (max-width: 1199px) {
                            top: -9px;
                            left: -15px;
                        }
                    }
                }
            }

            &.horizontal {
                display: flex;
                align-items: center;
                width: 445px;
                height: 250px;
                overflow: hidden;

                @media (max-width: 1199px) {
                    width: 270px;
                    height: 150px;
                }

                &.text-left {
                    .name {
                        position: relative;
                        margin-left: 40px;

                        @media (max-width: 1199px) {
                            margin-left: 20px;
                        }

                        &:after {
                            content: 'Accessories';
                            left: -32px;
                            top: -15px;

                            @media (max-width: 1199px) {
                                left: -16px;
                                top: -7px;
                            }
                        }
                    }
                }

                &.text-right {
                    justify-content: flex-end;
                    margin-top: 30px;

                    .name {
                        position: relative;
                        margin-right: 60px;

                        @media (max-width: 1199px) {
                            margin-right: 17px;
                        }

                        &:after {
                            content: 'Danceshoes';
                            left: -32px;
                            top: -15px;

                            @media (max-width: 1199px) {
                                left: -15px;
                                top: -7px;
                            }
                        }
                    }
                }
            }

            &.vertical-large {
                width: 350px;
                height: 530px;

                @media (max-width: 1199px) {
                    width: 210px;
                    height: 330px;
                }

                .name {
                    position: absolute;
                    bottom: 110px;
                    right: 60px;

                    @media (max-width: 1199px) {
                        bottom: 68px;
                        right: 26px;
                    }

                    &:after {
                        content: 'Ladies';
                        left: -37px;
                        top: -15px;

                        @media (max-width: 1199px) {
                            left: -15px;
                            top: -9px;
                        }
                    }
                }
            }
        }
    }
</style>
