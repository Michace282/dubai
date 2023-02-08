<template>
    <div class="mt-45">
        <div class="row categories-mob" v-if="$device.isMobile">
            <div class="col-12 col-md-auto">
                <nuxt-link
                    :to="{ path: '/catalog/ladies',  }"
                    class="category vertical-large mt-0"
                >
                    <div style="overflow: hidden; height: 150px;"><img src='../assets/images/category-ladies.png' alt="Women’s dance clothes" class="my-index-category-img"></div>
                    <div class="name">WOMEN</div>
                </nuxt-link>
            </div>
            <div class="col-12 col-md-auto">
                <nuxt-link :to="{ path: '/catalog/mens',  }" class="category vertical">
                <div style="overflow: hidden; height: 150px; text-align: right;"><img src='../assets/images/category-mans.png' alt="Women’s dance clothes" class="my-index-category-img"></div>
                    <div class="name">MEN</div>
                </nuxt-link>
            </div>
            <div class="col-12 col-md-auto">
                <nuxt-link
                    :to="{ path: '/catalog/dance_shoes',  }"
                    class="category horizontal text-right"
                >
                    <div style="overflow: hidden; height: 150px; width: 49%"><img style="width: 120%;" src='../assets/images/category-danceshoes.png' alt="Women’s dance clothes" class="my-index-category-img"></div>
                    <div class="name">DANCE SHOES</div>
                </nuxt-link>
            </div>
            <div class="col-12 col-md-auto">
                <nuxt-link
                    :to="{ path: '/catalog/accessories',  }"
                    class="category horizontal text-left"
                >
                    <div class="name">ACCESSORIES</div>
                    <div style="overflow: hidden; height: 150px"><img src='../assets/images/category-acessories1.png' alt="Women’s dance clothes" class="my-index-category-img"></div>
                </nuxt-link>
            </div>

            <div class="col-12 col-md-auto">
                <nuxt-link
                    :to="{ path: '/catalog/performance_costumes',  }"
                    class="category horizontal text-left"
                >
                    <div class="name">Competetion Consumes</div>
                </nuxt-link>
            </div>

        </div>
        <div class="row categories-pc" v-else>
            <div class="col-12 col-md-2">
                <nuxt-link
                    :to="{ path: '/catalog/ladies',  }"
                    class="category category-img-ladies"
                >
                    <img src='../assets/images/category-ladies-pc.png' alt="Women’s dance clothes" class="my-index-category-img">
                    <div class="name">WOMEN</div>
                    <div class="sub-name">WOMEN</div>
                </nuxt-link>
            </div>
            <div class="col-12 col-md-2">
                <nuxt-link
                    :to="{ path: '/catalog/dance_shoes',  }"
                    class="category category-img-danceshoes"
                >
                    <img src='../assets/images/category-danceshoe-pc.png' alt="Dance shoes" class="my-index-category-img">
                    <div class="name">DANCE SHOES</div>
                    <div class="sub-name">DANCE SHOES</div>
                </nuxt-link>
            </div>
            <div class="col-12 col-md-2">
                <nuxt-link
                    :to="{ path: '/catalog/accessories',  }"
                    class="category category-img-acessories"
                >
                    <img src='../assets/images/category-acessories-pc.png' alt="Dance accessories" class="my-index-category-img">
                    <div class="name">ACCESSORIES</div>
                    <div class="sub-name">ACCESSORIES</div>
                </nuxt-link>
            </div>
            <div class="col-12 col-md-2">
                <nuxt-link :to="{ path: '/catalog/mens',  }" class="category category-img-mens">
                    <img src='../assets/images/category-mans-pc.png' alt="Men’s dance clothes" class="my-index-category-img">
                    <div class="name">MEN</div>
                    <div class="sub-name">MEN</div>
                </nuxt-link>
            </div>
            <div class="col-12 col-md-2">
                <nuxt-link :to="{ path: '/catalog/performance_costumes',  }" class="category category-performance-costumes">
                    <div class="name">Competetion Consumes</div>
                    <div class="sub-name">Competetion Consumes</div>
                </nuxt-link>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'IndexPageCategories',
    };
</script>
<style>
   .category-performance-costumes {
       WIDTH: 100%;
       HEIGHT: 100%;
   }
   .category-performance-costumes .name {
    -webkit-transform: rotate(-90deg) translate(-100px, -100px);
    -moz-transform: rotate(-90deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
    white-space: nowrap;
    font-size: 20px!important;
   }
</style>
<style lang="less" scoped>
    .categories-pc {
        justify-content: center;

        .col-md-3 {
            padding: 0 5px;
        }

        .category {
            position: relative;
            display: block;
            background: #f3f0ef;
            text-decoration: none !important;
            background-repeat: no-repeat;
            background-size: cover;
            max-height: 530px;
            overflow: hidden;

            @media @medium {
                margin: 30px auto 0px;
            }

            .my-index-category-img {
                object-fit: cover;
                width: 100%;
            }

            .sub-name {
                font-family: 'Inter';
                font-size: 30px;
                line-height: 36px;
                text-transform: uppercase;
                color: @grey2;
                position: absolute;
                top: 20px;
                left: 20px;
                z-index: 1;

                @media @extraLarge {
                    font-size: 25px;
                }
                @media @large {
                    font-size: 21px;
                }

            }

            .name {
                position: absolute;
                top: 40px;
                left: 40px;
                z-index: 1;
                font-family: 'Inter-Medium';
                font-size: 24px;
                line-height: 29px;
                text-transform: uppercase;
                color: @black;
                z-index: 10;

                @media @extraLarge {
                    font-size: 18px;
                }
            }


        }

        // .category-img-mens {
        //     background-image: url('../assets/images/category-mans-pc.png');
        // }

        // .category-img-danceshoes {
        //     background-image: url('../assets/images/category-danceshoe-pc.png');
        // }

        // .category-img-acessories {
        //     background-image: url('../assets/images/category-acessories-pc.png');
        // }

        // .category-img-ladies {
        //     background-image: url('../assets/images/category-ladies-pc.png');
        // }
    }

    .categories-mob {
        justify-content: center;

        .category {
            position: relative;
            display: block;
            background: #f3f0ef;
            text-decoration: none !important;
            background-repeat: no-repeat;
            background-size: cover;

            @media @medium {
                margin: 30px auto 0px;
            }
            
            .my-index-category-img {
                object-fit: cover;
                width: 100%;
            }

            .name {
                font-family: 'Inter-Medium';
                font-size: 24px;
                line-height: 29px;
                text-transform: uppercase;
                color: @black;
                z-index: 10;

                @media @extraLarge {
                    font-size: 18px;
                }

                &:after {
                    position: absolute;
                    z-index: -1;
                    text-transform: uppercase;
                    font-size: 48px;
                    color: @grey2;

                    @media @extraLarge {
                        font-size: 28px;
                    }
                }
            }

            &.vertical {
                width: 255px;
                height: 530px;
                // background-image: url('../assets/images/category-mans.png');

                @media @extraLarge {
                    width: 150px;
                    height: 330px;
                }

                @media @medium {
                    width: 100%;
                    height: 150px;
                    background-size: 272px;
                    background-position: 74px -10px;
                }

                .name {
                    position: absolute;
                    top: 111px;
                    left: 40px;

                    @media @extraLarge {
                        top: 64px;
                        left: 20px;
                    }

                    &:after {
                        content: 'Mens';
                        top: -17px;
                        left: -30px;

                        @media @extraLarge {
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

                @media @extraLarge {
                    width: 270px;
                    height: 150px;
                }

                @media @medium {
                    width: 100%;
                    height: 150px;
                    // background-size: 270px;
                }

                &.text-left {
                    // background-image: url('../assets/images/category-acessories.png');

                    .name {
                        position: relative;
                        margin-left: 40px;

                        @media @extraLarge {
                            margin-left: 20px;
                        }

                        &:after {
                            content: 'Accessories';
                            left: -32px;
                            top: -15px;

                            @media @extraLarge {
                                left: -16px;
                                top: -7px;
                            }
                        }
                    }
                }

                &.text-right {
                    // background-image: url('../assets/images/category-danceshoes.png');
                    justify-content: flex-end;
                    margin-top: 30px;

                    .name {
                        position: relative;
                        margin-right: 60px;

                        @media @extraLarge {
                            margin-right: 17px;
                        }

                        &:after {
                            content: 'Danceshoes';
                            left: -32px;
                            top: -15px;

                            @media @extraLarge {
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

                // background-image: url('../assets/images/category-ladies.png');

                @media @extraLarge {
                    width: 210px;
                    height: 330px;
                }

                @media @medium {
                    width: 100%;
                    height: 150px;
                    // background-size: 160px;
                    background-position: 20px 0px;
                }

                .name {
                    position: absolute;
                    bottom: 110px;
                    right: 60px;

                    @media @extraLarge {
                        bottom: 68px;
                        right: 26px;
                    }

                    &:after {
                        content: 'Ladies';
                        left: -37px;
                        top: -15px;

                        @media @extraLarge {
                            left: -15px;
                            top: -9px;
                        }
                    }
                }
            }
        }
    }
</style>
