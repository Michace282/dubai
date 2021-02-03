<template>
    <client-only>
        <paginate
            :page-count="pageCursor.length"
            :clickHandler="
                (page) => {
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
        name: 'Pagination',
        props: {
            pageCursor: {
                type: Array,
                required: true,
                deafault: () => {
                    return [];
                },
            },
        },
    };
</script>
<style lang="less">
    .pagination {
        width: fit-content;
        margin: 45px auto 0px auto;
        justify-content: space-between;
        align-items: center;
        li {
            width: 30px;
            height: 30px;
            margin-right: 15px;

            &:not(.break) {
                display: flex;
                align-items: center;
                justify-content: center;
                background: @white;
                border: 1px solid @black;
                box-sizing: border-box;
                border-radius: 2px;
                cursor: pointer;
            }

            &.break {
                position: relative;

                &:after {
                    content: url('../../assets/images/icons/ellipsis.svg');
                    position: absolute;
                    bottom: -5px;
                }

                a {
                    display: none;
                }
            }

            &.prev,
            &.next {
                display: none;
            }

            &.active,
            &:hover:not(.break) {
                background: @black;
                a {
                    color: @white;
                    font-weight: 600;
                }
            }

            a {
                width: 100%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-style: normal;
                font-weight: normal;
                font-size: 14px;
                line-height: 16px;
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
