<template>
    <div class="product-item-carousel">
        <client-only>
            <VueSlickCarousel class="nav-slider" v-bind="slickOptions" :key="1">
                <div v-for="i in 10" :key="i">
                    <product-item :id="'1'" :name="'123213'" :price="321321" />
                </div>
                <template #prevArrow>
                    <div class="custom-arrow prev"><img src="~/assets/images/icons/arrow-collapse.svg" /></div>
                </template>
                <template #nextArrow>
                    <div class="custom-arrow next"><img src="~/assets/images/icons/arrow-collapse.svg" /></div>
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
        data() {
            return {
                slickOptions: {
                    slidesToShow: 6,
                    arrows: true,
                    rows: 1,
                    initialSlide: 0,
                },
            };
        },
    };
</script>
<style lang="less">
    .product-item-carousel {
        .product {
            .preview {
                max-height: 220px;
            }

            .name,
            .price {
                font-size: 14px;
            }
        }

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
