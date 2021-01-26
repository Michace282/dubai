<template>
    <div class="input-box">
        <label v-if="label" :for="label" class="label">{{ label }}</label>
        <input type="text" :id="label" :placeholder="label" :name="name" />
    </div>
</template>
<script>
    export default {
        name: 'BaseInput',
        props: {
            label: {
                type: String,
                required: false,
                default: null,
            },
            name: {
                type: String,
                required: false,
                default: '',
            },
        },
    };
</script>
<style lang="less" scoped>
    @import '../../assets/css/variables.less';

    .input-box {
        display: flex;
        border-bottom: 1px solid @black;
        padding: 0px 0px 7px 0px;

        &.dark {
            border-color: @white;

            input {
                background: @black;
                color: @white;
            }

            .label {
                color: @grey4;
            }
        }

        .label {
            white-space: nowrap;
            font-family: 'Inter-Regular';
            font-size: 14px;
            text-transform: uppercase;
            color: @grey4;
            margin: 0px 30px 0px 0px;

            @media @medium {
                display: none;
            }
        }

        input {
            width: 100%;
            border: none;
            font-family: 'Inter-Regular';
            font-size: 14px;
            text-transform: uppercase;
            background: @grey3;
            color: @black;

            &::placeholder {
                opacity: 0;
                @media @medium {
                    opacity: 1;
                }
            }
        }
    }
</style>
