<template>
    <div>
        <div class="row d-none d-дп-flex">
            <div class="col-auto">
                <client-only>
                    <VueSlickCarousel
                        class="nav-slider"
                        v-bind="slickOptions"
                        :key="images.length"
                        :style="{ 'max-height': '695px' }"
                        @afterChange="
                            (index) => {
                                activeIndex = index;
                            }
                        "
                    >
                        <div v-for="(image, index) in images" :key="index">
                            <img
                                class="carousel-img"
                                :class="{ active: index == activeIndex }"
                                :src="image.node.imageCropping"
                            />
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
            <div class="col">
                <img class="active-image" v-if="images[activeIndex]" :src="images[activeIndex].node.image" />
                <img class="active-image" v-else src="~/assets/images/no-photo.jpg" />
            </div>
        </div>
        <div class="d-block d-дп-none mt-15">
            <client-only>
                <b-carousel
                    id="photo-carousel"
                    :interval="4000"
                    indicators
                    class="index-carousel"
                    img-width="1024"
                    img-height="480"
                >
                    <b-carousel-slide v-for="(image, index) in images" :key="index + 'mobile'">
                        <template #img>
                            <img class="d-block img-fluid w-100" :src="image.node.image" alt="image slot" />
                        </template>
                    </b-carousel-slide>
                </b-carousel>
            </client-only>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'ProductCarousel',
        props: {
            images: {
                type: Array,
                default: () => {
                    return [];
                },
            },
        },
        data() {
            return {
                activeIndex: 0,
                slickOptions: {
                    slidesToShow: 5,
                    arrows: true,
                    rows: 1,
                    vertical: true,
                    verticalSwiping: true,
                    initialSlide: 0,
                    focusOnSelect: true,
                },
            };
        },
        watch: {
            images() {
                this.activeIndex = 0;
            },
        },
    };
</script>
<style lang="less" scoped>
    .nav-slider {
        width: 100px;

        .carousel-img {
            width: 97px;
            height: 130px;
            object-fit: cover;
            box-sizing: border-box;
            border-radius: 2px;

            &.active {
                border: 1px solid @yellow;
            }
        }

        .custom-arrow {
            display: flex;
            justify-content: center;
            position: absolute;
            z-index: 10;
            width: 100%;
            height: 55px;
            cursor: pointer;

            &.prev {
                top: 0px;
                background: linear-gradient(179deg, white, transparent);
                align-items: flex-start;

                img {
                    transform: rotate(180deg);
                }
            }

            &.next {
                bottom: 0px;
                background: linear-gradient(0deg, white, transparent);
                align-items: flex-end;
            }
        }
    }

    .active-image {
        max-width: 500px;
        width: 100%;
    }
</style>
