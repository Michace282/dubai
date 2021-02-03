<template>
    <div class="container" v-if="error.statusCode == 404">
        <div class="row content-box">
            <div class="col-12 col-md-auto">
                <base-title class="code" title="404" />
            </div>
            <div class="col-12 col-md-auto">
                <div>
                    <div class="title">page not found</div>
                    <div class="desc">
                        The requested page was not found. You may have made a typo in the address or the page was moved
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-30 justify-content-center">
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

            .front-title {
                width: fit-content;
                left: 0 !important;
                right: 0 !important;
                margin: auto;
                bottom: 8px !important;
                line-height: 74px;
                font-size: 96px !important;
            }
        }
    }
</style>
<style lang="less" scoped>
    .container {
        min-height: calc(100vh - 462px);
        .btn-outline-black {
            padding: 9px 60px;
        }

        .btn-black {
            padding: 7px 55px;
        }

        .content-box {
            margin-top: 130px;
            .title {
                font-family: 'Inter-Medium';
                font-size: 24px;
                line-height: 29px;
                text-transform: uppercase;
                color: @black;
            }

            .desc {
                max-width: 240px;
                margin-top: 21px;
                font-family: 'Inter-Light';
                font-size: 18px;
                line-height: 22px;
                color: @black;
            }
        }
    }
</style>
