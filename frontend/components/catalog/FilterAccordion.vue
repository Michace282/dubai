<template>
    <b-card no-body class="filter-accordion">
        <b-card-header header-tag="header" role="tab">
            <b-button block v-b-toggle="name">{{ title }}</b-button>
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
        },
    };
</script>
<style lang="less">
    .filter-accordion {
        border: 0px;

        @media @large {
            margin-top: 2px;
        }

        &.arrow-descktop-hide {
            .btn-block {
                &:after {
                    @media (min-width: 992px) {
                        content: none;
                    }
                }
            }
        }

        .card-header {
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
            text-align: left;
            font-family: 'Inter-Medium';
            font-size: 24px;
            color: @black;
            padding: 0px;
            background: none;
            border: 0px;
            color: @black;

            @media @large {
                background: @grey3;
                padding: 3px 20px;
            }

            &:after {
                content: url('../../assets/images/icons/arrow-collapse.svg');
                position: absolute;
                display: flex;
                align-items: center;
                height: 15px;
                top: 10px;
                right: 0px;
                transition: all 0.5s;

                @media @large {
                    right: 20px;
                }
            }

            &.collapsed {
                font-weight: normal;

                &:after {
                    top: 15px;
                    transform: rotate(180deg);
                }
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
    }
</style>
