<template>
    <b-card no-body class="filter-card">
        <b-card-header header-tag="header" role="tab">
            <b-button block v-b-toggle="name">{{title}}</b-button>
        </b-card-header>
        <b-collapse :id="name" :accordion="name" role="tabpanel">
            <b-card-body>
                <slot></slot>
            </b-card-body>
        </b-collapse>
    </b-card>
</template>
<script>
    export default {
        name: 'FilterCard ',
        props: {
            title: {
                type: String,
                required: false,
                default: ''
            },
            name: {
                type: String,
                required: true,
                default: null,
            }
        }
    };
</script>
<style lang="less">
    .filter-card {
        border: 0px;

        .card-header {
            padding: 0px;
            border: 0px;
            background-color: unset;
        }

        .card-body {
            margin-top: 15px;
            padding: 0px;
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

            &:after {
                content: url('../../assets/images/icons/arrow-collapse.svg');
                position: absolute;
                display: flex;
                align-items: center;
                height: 15px;
                top: 10px;
                right: 0px;
                transition: all 0.5s;
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
            }
        }
    }
</style>
