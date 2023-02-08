<template>
    <div class="container">
        <ApolloQuery
            :query="require('~/graphql/queries/page/pageDetail.graphql')"
            :variables="{
                slug: $route.params.slug,
            }"
            @result="update"
        >
            <template v-slot="{ result: { error, data }, isLoading }">
                <div v-if="isLoading || error" class="loading apollo mt-85"><loader /></div>
                <div v-else-if="data && data.pageDetail" class="result apollo">
                    <div class="row">
                        <div class="col-12">
                            <base-title :title="data.pageDetail.name" class="mt-30" />
                            <div class="text-box" v-html="data.pageDetail.text"></div>
                        </div>
                    </div>
                </div>
            </template>
        </ApolloQuery>
    </div>
</template>
<script>
    import Loader from '../../components/Loader.vue';
    export default {
        components: { Loader },
        name: '_slug',
        data() {
            return {
                metaData: null,
            };
        },
        head() {
            return this.metaData;
        },
        methods: {
            update(data) {
                if (data.data && data.data.pageDetail) {
                    let content = '';
                    if(data.data.pageDetail.slug == 'privacy_policy') content = "The DC&S Company Privacy Notice."
                    if(data.data.pageDetail.slug == 'terms_condition') content = "Terms and conditions of online shopping at dcsdubai.com"
                    this.metaData = {
                        title: data.data.pageDetail.name,
                        meta: [
                            {
                                hid: 'description',
                                name: 'description',
                                content,
                            },
                        ],
                    };
                    this.$store.commit('set_breadcrumbs', [
                        { route: '/', name: 'Home' },
                        {
                            route: { name: 'page-slug', params: { slug: data.data.pageDetail.slug } },
                            name: data.data.pageDetail.name,
                        },
                    ]);
                }
            },
        },
    };
</script>
<style lang="less" scoped>
    .text-box {
        display: block;
        justify-content: space-between;
        margin-top: 60px;

        @media @large {
            width: fit-content;
            flex-direction: column;
            justify-content: flex-start;
            margin-top: 45px;
        }

        .text {
            max-width: 530px;
            font-family: 'Inter-Light';
            font-size: 18px;
            color: @black;

            @media @medium {
                line-height: 22px;
            }

            &.mr-60 {
                @media (min-width: 992px) {
                    margin-right: 60px;
                }
            }
        }

        .photo {
            @media @large {
                width: fit-content;
                margin: 0px auto 45px;
            }

            img {
                @media (max-width: 450px) {
                    width: 240px;
                }

                @media (min-width: 992px) {
                    width: 100%;
                }
            }
        }
    }
</style>
