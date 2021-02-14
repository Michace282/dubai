<template>
    <div class="dropdown-group">
        <div class="label">
            {{ label }}
        </div>
        <div class="dropdown">
            <a href.prevent @click="showDropdown = !showDropdown" :class="{ active: showDropdown }" class="value">{{
                value.name
            }}</a>
            <div class="options" v-if="showDropdown">
                <a
                    href.prevent
                    @click="
                        value = option.node;
                        $emit('input', option.node.id);
                        showDropdown = false;
                    "
                    class="option"
                    v-for="(option, index) in options"
                    :key="index"
                    >{{ option.node.name }}</a
                >
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'DropDonw',
        props: {
            label: {
                type: String,
                required: false,
                default: '',
            },
            options: {
                type: Array,
                required: true,
                default: () => {
                    return [];
                },
            },
        },
        data() {
            return {
                showDropdown: false,
                value: { id: null, name: '' },
            };
        },
        created() {
            if (this.options.length > 0) {
                this.value = this.options[0].node;
                this.$emit('input', this.options[0].node.id);
            }
        },
    };
</script>
<style lang="less" scoped>
    .dropdown-group {
        min-width: 90px;

        .label {
            margin-bottom: 15px;
            font-size: 14px;
            line-height: 17px;
            text-transform: uppercase;
            color: @grey4;

            @media @small {
                margin-bottom: 10px;
            }
        }

        .dropdown {
            position: relative;
            width: 100%;

            .value {
                position: relative;
                display: block;
                font-family: 'Inter-Medium';
                font-size: 18px;
                line-height: 22px;
                text-transform: uppercase;
                color: @black;
                padding-bottom: 10px;
                border-bottom: 1px solid @black;
                cursor: pointer;

                @media @small {
                    font-size: 14px;
                }

                &.active {
                    border-bottom: 0px;

                    &:after {
                        transform: rotate(180deg);
                        bottom: 8px;
                    }
                }

                &:after {
                    content: url('../../assets/images/icons/arrow-collapse.svg');
                    position: absolute;
                    right: 0;
                    bottom: 10px;
                    height: fit-content;
                    transition: all 0.3s;
                }
            }

            .options {
                max-height: 110px;
                overflow: auto;
                position: absolute;
                width: 100%;
                z-index: 100;
                border: 1px solid @black;
                background: @grey3;

                .option {
                    display: block;
                    width: 100%;
                    font-family: 'Inter-Medium';
                    padding: 5px;
                    cursor: pointer;

                    &:hover {
                        background: #00000029;
                    }
                }
            }
        }
    }
</style>
