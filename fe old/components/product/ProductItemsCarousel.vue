<template>
    <div class="product-item-carousel">
        <client-only>
            <VueSlickCarousel class="nav-slider" v-bind="slickOptions" :key="1">
                <div v-for="(product, index) in items" :key="index">
                    <product-item
                        class="product-sm"
                        :id="product.node.id"
                        :name="product.node.name"
                        :price="product.node.price"
                        :isWishlist="product.node.isWishlist"
                        :colorsGroup="product.node.productsizecolorSet"
                    />
                </div>
                <template #prevArrow>
                    <div class="custom-arrow prev"><img src="~/assets/images/icons/arrow-collapse.svg" alt="prev" /></div>
                </template>
                <template #nextArrow>
                    <div class="custom-arrow next"><img src="~/assets/images/icons/arrow-collapse.svg" alt="next" /></div>
                </template>
            </VueSlickCarousel>
        </client-only>
    </div>
</template>
<script>
    import ProductItem from '../catalog/ProductItem.vue';
    export default {
        name: 'ProductItemCarousel',
        components: {
            ProductItem,
        },
        props: {
            items: {
                type: Array,
                required: true,
                default: () => {
                    return [];
                },
            },
        },
        data() {
            return {
                slickOptions: {
                    slidesToShow: 6,
                    slidesToScroll: 1,
                    arrows: true,
                    rows: 1,
                    initialSlide: 0,
                    responsive: [
                        {
                            breakpoint: 1199,
                            settings: {
                                slidesToShow: 4,
                            },
                        },
                        {
                            breakpoint: 991,
                            settings: {
                                slidesToShow: 3,
                            },
                        },
                        {
                            breakpoint: 767,
                            settings: {
                                slidesToShow: 2,
                            },
                        },
                    ],
                },
            };
        },
    };
</script>
<style lang="less">
    .product-item-carousel {
        .custom-arrow {
            display: flex;
            align-items: center;
            width: 80px;
            max-height: 220px;
            height: 100%;
            position: absolute;
            top: 0;
            margin: auto;
            cursor: pointer;
            z-index: 100;

            &.prev {
                left: 0px;
                background: linear-gradient(90deg, white, transparent);

                img {
                    transform: rotate(90deg);
                }
            }

            &.next {
                right: 0px;
                background: linear-gradient(-90deg, white, transparent);
                justify-content: flex-end;

                img {
                    transform: rotate(-90deg);
                }
            }
        }
    }
</style>
