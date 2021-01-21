<template>
    <div class="container">
        <div class="row caption-group">
            <div class="col-auto head-caption">
                <img src="~/assets/images/icons/truck.svg" />
                Free shipping within UAE
            </div>
            <div class="col-auto head-caption">
                <img src="~/assets/images/icons/present.svg" />
                Get your present!
            </div>
            <div class="col-auto head-caption">
                <img src="~/assets/images/icons/line.svg" />
                Size charts
            </div>
        </div>
        <b-carousel
            id="carousel-1"
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
                <div>
                    <nuxt-link to="" class="carousel-link">Dress Damiana Grey</nuxt-link>
                    <div class="caption">200 AED <img src="~/assets/images/icons/arrow-right.svg" /></div>
                </div>
            </b-carousel-slide>
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
            </b-carousel-slide>
        </b-carousel>
        <div class="row mt-45">
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
        </div>
        <div class="advantages-group">
            <base-title title="Our advantages" />
            <div class="advantages">
                <div class="advantage" v-for="(advantage, index) in advantages" :key="index">
                    <img :src="require(`~/assets/images/icons/${advantage.icon}`)" />
                    <div class="name">
                        {{ advantage.name }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'index',
        data() {
            return {
                advantages: [
                    {
                        icon: 'laptop.svg',
                        name: 'Wide range of products',
                    },
                    {
                        icon: 'calendar.svg',
                        name: 'Monthly update of collections',
                    },
                    {
                        icon: 'dimond.svg',
                        name: 'High quality material',
                    },
                    {
                        icon: 'sale.svg',
                        name: 'Affordable price',
                    },
                    {
                        icon: 'crown.svg',
                        name: 'Comfortable & Stylish',
                    },
                    {
                        icon: 'pen.svg',
                        name: 'We can arrange custom orders according to your measurements',
                    },
                ],
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', null);
        },
    };
</script>

<style lang="less">
    @import '../assets/css/colors';

    .index-carousel {
        .carousel-caption {
            right: 90px;
            bottom: 30px;
            left: unset;
            text-align: left;

            .carousel-link {
                font-family: 'Inter-ExtraLight';
                font-size: 14px;
                text-decoration-line: underline;
                color: @white;
            }

            .caption {
                font-family: 'Inter-ExtraLight';
                display: flex;
                align-items: center;
                margin-top: 5px;
                font-size: 10px;
                color: @pink_light;

                img {
                    margin-left: 15px;
                }
            }
        }
    }

    .carousel-indicators {
        display: flex;
        align-items: center;
        li {
            width: 15px;
            height: 5px;
            opacity: 1;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 5px;
            border: 0px;
            transition: all 0.5s;

            &.active {
                width: 30px;
                height: 7px;
                background: @black;
            }
        }
    }
</style>

<style lang="less" scoped>
    @import '../assets/css/colors';

    .advantages-group {
        margin-top: 90px;

        .advantages {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            margin-top: 45px;

            .advantage {
                display: flex;
                flex-direction: column;
                align-items: center;

                .name {
                    max-width: 135px;
                    margin-top: 15px;
                    text-align: center;
                }
            }
        }
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

    .caption-group {
        width: fit-content;
        margin: 0 auto;
        padding: 15px 0px;

        .head-caption {
            display: flex;
            align-items: center;
            font-size: 14px;

            &:last-child {
                margin-right: 22px;
            }

            img {
                margin-right: 15px;
            }
        }
    }
</style>
