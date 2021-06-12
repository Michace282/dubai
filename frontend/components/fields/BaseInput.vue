<template>
    <div class="input-box">
        <label v-if="label" :for="label" class="label">{{ label }}</label>
        <input
            :type="type"
            v-model="model"
            @input="$emit('input', model)"
            :id="label"
            :placeholder="label"
            :name="name"
        />
        <div class="error-text" v-if="error">{{ error }}</div>
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
            error: {
                type: String,
                required: false,
                default: '',
            },
            type: {
                type: String,
                required: false,
                default: 'text',
            },
            value: {
                default: '',
            },
        },
        data() {
            return {
                model: this.value,
            };
        },
        watch: {
            value() {
                this.model = this.value;
            }
        }
    };
</script>
<style lang="less" scoped>
    .input-box {
        display: flex;
        position: relative;
        border-bottom: 1px solid @black;
        padding: 0px 0px 7px 0px;

        &.error {
            border-color: @red;

            .label {
                color: @red;
            }
        }

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

        .error-text {
            position: absolute;
            color: @red;
            font-size: 12px;
            bottom: -20px;
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
