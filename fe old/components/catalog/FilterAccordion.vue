<template>
    <b-card no-body class="filter-accordion">
        <b-card-header header-tag="header" role="tab" class="header-tab">
            <h2 v-if="isLink" class="btn-block category-name" href.prevent @click="$emit('setCategory')">
                {{ title }}
            </h2>
            <h2 block v-b-toggle="name" v-else class="btn-block category-name">{{ title }}</h2>
            <!-- <b-button block v-b-toggle="name">{{ title }}</b-button> -->
            <b-button block v-b-toggle="name" class="btn-toggler"></b-button>
        </b-card-header>
        <b-collapse :id="name" :accordion="name" role="tabpanel" :visible="visible">
            <b-card-body>
                <slot></slot>
            </b-card-body>
        </b-collapse>
    </b-card>
</template>
<script>
    export default {
        name: 'FilterAccordion',
        props: {
            title: {
                type: String,
                required: false,
                default: '',
            },
            name: {
                type: String,
                required: true,
                default: null,
            },
            visible: {
                type: Boolean,
                required: false,
                default: false,
            },
            isLink: {
                type: Boolean,
                required: false,
                default: false,
            },
        },
    };
</script>
<style lang="less">
    .filter-accordion {
        border: 0px;

        @media @large {
            margin-top: 2px;
        }

        &.active {
            .category-name {
                color: @yellow;
            }
        }

        // &.arrow-descktop-hide {
        //     .btn-block {
        //         // opacity: 0;

        //         &:after {
        //             @media (min-width: 992px) {
        //                 content: none;
        //             }
        //         }

        //         @media @large {
        //             position: relative;
        //             opacity: 1;
        //         }

        //         &.category-name {
        //             position: absolute;
        //             width: fit-content;
        //             height: fit-content;
        //             opacity: 1;
        //             top: 0;
        //             left: 0;
        //             bottom: 0;
        //             margin: auto;
        //             z-index: 50;

        //             @media @large {
        //                 top: unset;
        //             }

        //             &:after {
        //                 @media @large {
        //                     content: none;
        //                 }
        //             }
        //         }
        //     }
        // }

        .card-header {
            position: relative;
            padding: 0px;
            border: 0px;
            background-color: unset;
        }

        .card-body {
            margin-top: 15px;
            padding: 0px;

            @media @large {
                padding: 0px 20px 15px 20px;
            }

            .categories {
                @media @large {
                    padding-left: 20px !important;
                    margin: 0px;
                }
            }
        }

        .btn-block {
            cursor: pointer;
            text-align: left;
            font-family: 'Inter-Medium';
            font-size: 24px;
            color: @black;
            padding: 0px;
            background: none;
            border: 0px;
            color: @black;
            margin: 0px;
            width: 90%;

            @media @large {
                background: @grey3;
                padding: 3px 20px;
                width: 100%;
            }

            &:active,
            &:focus {
                color: @black !important;
                outline: none !important;
                background: @white !important;
                box-shadow: unset !important;

                @media @large {
                    background: @grey3 !important;
                }
            }
        }

        .btn-toggler:after {
            content: url('../../assets/images/icons/arrow-collapse.svg');
            position: absolute;
            display: flex;
            align-items: center;
            height: 15px;
            right: 0px;
            top: 10px;

            transition: all 0.5s;
            transform: rotate(180deg);

            @media @large {
                top: 15px;
                right: 20px;
            }
        }

        .btn-toggler.collapsed {
            font-weight: normal;

            &:after {
                transform: rotate(0deg);
            }
        }
    }
</style>
