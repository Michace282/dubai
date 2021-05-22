<template>
    <div class="container">
        <account-head-group/>
        <ApolloQuery
            :query="require('~/graphql/queries/product/basketList.graphql')"
            :variables="{
                first: 25,
                status: 'completed'
            }"
            fetchPolicy="no-cache"
        >
            <template v-slot="{ result: { error, data }, isLoading, query }">
                <transition name="fade" mode="out-in">
                    <div v-if="isLoading || error" class="loading apollo mt-85" key="loader">
                        <loader/>
                    </div>
                    <div v-else-if="data && data.basketList" class="result apollo" key="loader">
                        <div class="mt-45" v-if="data.basketList.edges.length > 0">
                            <div class="row order"
                                 v-for="(basket, index) in data.basketList.edges"
                                 :key="basket.node.uuid"
                            >
                                <div class="col-12 col-lg-5 block-1 pl-0">
                                    <div class="text-black">Order №{{ basket.node.uuid }}</div>
                                    <div class="date"> {{
                                            $moment(basket.node.createdAt).format('DD.MM.YYYY')
                                        }}
                                    </div>
                                </div>
                                <div class="col-12 col-lg-7 block-2 pr-0">
                                    <div class="text-black">Track number: {{ basket.node.codeDelivery }}</div>
                                    <!--                                    <button class="btn btn-outline-black">track</button>-->
                                </div>
                            </div>
                        </div>
                        <div v-else class="no-result apollo" key="404">
                            <h3 class="text-center mt-5">Orders not found :(</h3>
                        </div>
                    </div>
                </transition>
            </template>
        </ApolloQuery>
    </div>
</template>
<script>
    import AccountHeadGroup from '~/components/AccountHeadGroup';
    import Loader from '~/components/Loader.vue';

    export default {
        name: 'previous-orders',
        created() {
            this.$store.commit('set_breadcrumbs', [{route: '', name: 'personal account'}]);
        },
        components: {AccountHeadGroup, Loader},
    };
</script>
<style lang="less" scoped>
    .order {
        justify-content: space-between;
        padding: 15px 30px;
        margin: 0px;

        @media @large {
            padding: 15px 20px 15px 20px;
            margin: 45px -15px 0px -15px;
        }

        &:nth-child(odd) {
            background: @grey3;
        }

        .block-1,
        .block-2 {
            display: flex;
            align-items: center;
        }

        .block-1 {
            justify-content: space-between;

            .date {
                @media (min-width: 1200px) {
                    margin-right: 65px;
                }
            }

            @media @large {
                padding: 0px;
            }
        }

        .block-2 {
            justify-content: space-between;

            @media @large {
                margin-top: 30px;
                padding: 0px;

                .text-black {
                    padding-right: 45px;
                }
            }
        }

        .text-black,
        .date {
            font-family: 'Inter-Medium';
            font-size: 18px;
            line-height: 22px;
            color: @black;

            @media @small {
                font-size: 14px;
                line-height: 17px;
            }
        }

        .date {
            color: @grey4;
        }

        .btn-outline-black {
            padding: 9px 56px 8px 56px;
        }
    }
</style>
