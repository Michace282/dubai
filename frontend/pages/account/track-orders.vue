<template>
    <div class="container">
        <account-head-group />
<!--        <div class="mt-45">-->
<!--            <div class="row order">-->
<!--                <div class="col-12 col-lg-5 block-1 pl-0">-->
<!--                    <div class="text-black">Order №5745769350</div>-->
<!--                    <div class="date">01.01.2021</div>-->
<!--                </div>-->
<!--                <div class="col-12 col-lg-7 block-2 pr-0">-->
<!--                    <div class="text-black">Track number: Rt215165165651CX</div>-->
<!--                    <button class="btn btn-outline-black">track</button>-->
<!--                </div>-->
<!--            </div>-->
<!--        </div>-->
    </div>
</template>
<script>
    import AccountHeadGroup from '~/components/AccountHeadGroup';

    export default {
        name: 'track-orders',
        components: { AccountHeadGroup },
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
                @media(min-width: 1200px) {
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
