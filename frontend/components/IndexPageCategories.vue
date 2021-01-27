<template>
    <div class="mt-45">
        <div class="row categories">
            <div class="col-auto">
                <nuxt-link to="#" class="category vertical-large">
                    <div class="name">Ladies</div>
                </nuxt-link>
            </div>
            <div class="col-auto">
                <nuxt-link to="#" class="category horizontal text-left">
                    <div class="name">Accessories</div>
                </nuxt-link>
                <nuxt-link to="#" class="category horizontal text-right">
                    <div class="name">Danceshoes</div>
                </nuxt-link>
            </div>
            <div class="col-auto">
                <nuxt-link to="#" class="category vertical">
                    <div class="name">Mens</div>
                </nuxt-link>
            </div>
            <!-- <b-carousel
                id="carousel-2"
                v-model="slide"
                :interval="4000"
                indicators
                class="index-carousel"
                img-width="1024"
                img-height="480"
            >
                <b-carousel-slide>
                    <template #img>
                        <img
                            class="d-block img-fluid w-100"
                            width="1024"
                            height="480"
                            src="~/assets/images/carouselPhoto.jpg"
                            alt="image slot"
                        />
                    </template>
                    <nuxt-link to="#" class="category vertical-large">
                        <div class="name">Ladies</div>
                    </nuxt-link>
                </b-carousel-slide>
            </b-carousel> -->
        </div>
    </div>
</template>
<script>
    export default {
        name: 'IndexPageCategories',
    };
</script>
<style lang="less" scoped>
    .categories {
        @media (max-width: 1199px) {
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
                &:after {
                    position: absolute;
                    z-index: -1;
                    text-transform: uppercase;
                    font-size: 48px;
                    color: @grey2;
                }
            }

            &.vertical {
                width: 255px;
                height: 530px;

                .name {
                    position: absolute;
                    top: 111px;
                    left: 40px;
                    &:after {
                        content: 'Mens';
                        top: -17px;
                        left: -30px;
                    }
                }
            }

            &.horizontal {
                display: flex;
                align-items: center;
                width: 445px;
                height: 250px;
                overflow: hidden;

                &.text-left {
                    .name {
                        position: relative;
                        margin-left: 40px;

                        &:after {
                            content: 'Accessories';
                            left: -32px;
                            top: -15px;
                        }
                    }
                }

                &.text-right {
                    justify-content: flex-end;
                    margin-top: 30px;
                    .name {
                        position: relative;
                        margin-right: 60px;

                        &:after {
                            content: 'Danceshoes';
                            left: -32px;
                            top: -15px;
                        }
                    }
                }
            }

            &.vertical-large {
                width: 350px;
                height: 530px;

                .name {
                    position: absolute;
                    bottom: 110px;
                    right: 60px;

                    &:after {
                        content: 'Ladies';
                        left: -37px;
                        top: -15px;
                    }
                }
            }
        }
    }
</style>
