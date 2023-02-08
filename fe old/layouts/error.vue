<template>
    <div class="container" v-if="error.statusCode == 404">
        <div class="row content-box">
            <div class="col-12 col-xl-auto">
                <base-title class="code" title="404" />
            </div>
            <div class="col-12 col-xl-auto">
                <div>
                    <div class="title">page not found</div>
                    <div class="desc">
                        The requested page was not found. You may have made a typo in the address or the page was moved
                    </div>
                </div>
            </div>
        </div>
        <div class="photo">
            <img src="~/assets/images/404.png" alt="Error 404" />
        </div>
        <div class="row mt-30 btn-box">
            <div class="col-auto">
                <a class="btn btn-outline-black" href.prevent @click="$router.go(-2)">Back</a>
            </div>
            <div class="col-auto">
                <nuxt-link class="btn btn-black" :to="{ name: 'index' }">Home</nuxt-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'error',
        layout: 'error-layout',
        props: ['error'],
    };
</script>
<style lang="less">
    .block-title {
        &.code {
            width: fit-content;
            font-size: 194px !important;
            line-height: 150px;

            @media @extraLarge {
                font-size: 72px !important;
                line-height: 87px;
            }

            .front-title {
                width: fit-content;
                left: 0 !important;
                right: 0 !important;
                margin: auto;
                bottom: 8px !important;
                line-height: 74px;
                font-size: 96px !important;

                @media @extraLarge {
                    font-size: 48px !important;
                    line-height: 58px;
                }
            }
        }
    }
</style>
<style lang="less" scoped>
    .container {
        position: relative;
        min-height: calc(100vh - 502px);

        @media @extraLarge {
            max-width: 381px;
            margin: 44px auto 90px;
        }

        .btn-box {
            max-width: 660px;
            justify-content: flex-end;

            @media @extraLarge {
                justify-content: flex-start;
            }

            .btn-black {
                padding: 7px 55px;
                @media @xs {
                    padding: 7px 53px;
                }

                @media (max-width: 320px) {
                    padding: 7px 43px;
                }
            }

            .btn-outline-black {
                padding: 9px 60px;

                @media @xs {
                    padding: 9px 58px;
                }

                @media (max-width: 320px) {
                    padding: 9px 48px;
                }
            }
        }

        .photo {
            bottom: 0;
            right: 0;
            position: absolute;

            @media @extraLarge {
                bottom: unset;
                top: -5px;

                img {
                    height: 300px;
                }

                &:after {
                    content: '';
                    width: 180px;
                    position: absolute;
                    right: 0;
                    bottom: -6px;
                    z-index: 10;
                    height: 15px;
                    filter: blur(3px);
                    background: @white;
                    opacity: 0.9;
                }
            }
        }

        .content-box {
            max-width: 735px;
            margin-top: 130px;
            justify-content: flex-end;

            @media @extraLarge {
                margin-top: 0px;
            }

            .title {
                font-family: 'Inter-Medium';
                font-size: 24px;
                line-height: 29px;
                text-transform: uppercase;
                color: @black;

                @media @extraLarge {
                    max-width: 155px;
                    margin-top: 60px;
                    font-size: 18px;
                    line-height: 22px;
                }
            }

            .desc {
                max-width: 240px;
                margin-top: 21px;
                font-family: 'Inter-Light';
                font-size: 18px;
                line-height: 22px;
                color: @black;

                @media @extraLarge {
                    max-width: 155px;
                    font-size: 14px;
                    line-height: 17px;
                }
            }
        }
    }
</style>
