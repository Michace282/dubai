<template>
    <div>
        <div class="row d-none d-lg-flex">
            <div class="col-auto">
                <client-only>
                    <VueSlickCarousel
                        class="nav-slider"
                        v-bind="slickOptions"
                        ref="nav-slider"
                        :key="images.length"
                        :asNavFor="$refs.c2"
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
                                :alt="name"
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
            <div class="col active-image-group">
                <a href.prevent class="carousel-control" @click="$refs['nav-slider'].prev()"
                    ><img src="~/assets/images/icons/arrow-carousel.svg" alt="arrow"
                /></a>
                <img class="active-image" v-if="images[activeIndex]" :src="images[activeIndex].node.image" :alt="name" />
                <img class="active-image" v-else src="~/assets/images/no-photo.jpg" alt="no photo" />
                <a href.prevent class="carousel-control next" @click="$refs['nav-slider'].next()"
                    ><img src="~/assets/images/icons/arrow-carousel.svg" alt="arrow"
                /></a>
            </div>
        </div>
        <div class="d-block d-lg-none mt-15">
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
                            <img class="d-block img-fluid w-100" :src="image.node.image" alt="New Collection" />
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
            name: ''
        },
        data() {
            return {
                activeIndex: 0,
                slickOptions: {
                    slidesToShow: 5,
                    arrows: true,
                    rows: 1,
                    speed: 0,
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

    .carousel-control {
        left: 32px;

        &.next {
            left: unset;
            right: 32px;
        }
    }

    .active-image-group {
        position: relative;
        height: fit-content;

        .active-image {
            max-width: 500px;
            width: 100%;
        }
    }
</style>
