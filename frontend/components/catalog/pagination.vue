<template>
    <client-only>
        <paginate
            :page-count="pageCursor.length"
            :clickHandler="
                (page) => {
                    $scrollTo('#top');
                    $emit('changeCursor', pageCursor[page - 1].cursor);
                }
            "
            prev-text="prev"
            next-text="next"
            prev-class="prev"
            next-class="next"
            container-class="pagination"
            break-view-class="break"
        >
        </paginate>
    </client-only>
</template>
<script>
    export default {
        name: 'pagination',
        props: ['pageCursor'],
    };
</script>
<style lang="less">
    @import '../assets/css/color';

    .pagination {
        width: fit-content;
        margin: 100px auto 0px auto;
        justify-content: space-between;
        align-items: center;
        li {
            margin-right: 40px;
            &.active,
            &:hover {
                a {
                    color: @black;
                    font-weight: 500;
                }
            }
            a {
                font-style: normal;
                font-weight: normal;
                font-size: 14px;
                line-height: 16px;
                color: @grey_dark3;
                cursor: pointer;
                text-decoration: none;
            }
            &:first-child {
                margin-right: 90px;
            }
            &:last-child {
                margin-left: 50px;
                margin-right: 0px;
            }
        }
        .prev,
        .next {
            position: relative;
            width: 10px;
            height: 20px;
            cursor: pointer;
            &.disabled {
                opacity: 0.5;
            }
            &:before {
                content: url('/images/pagination-arrow.svg');
                position: absolute;
                top: 0px;
                z-index: -1;
            }
            a {
                user-select: none;
                color: transparent !important;
            }
        }

        .next {
            &:before {
                top: -4px;
                transform: rotate(180deg);
            }
        }

        @media (max-width: 450px) {
            & li {
                margin-right: 10px;
            }

            & li:first-child {
                margin-right: 10px;
            }

            & li:last-child {
                margin-left: 0;
            }
        }
    }
</style>
