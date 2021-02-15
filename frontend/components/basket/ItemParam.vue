<template>
    <div class="row mt-15">
        <div class="col-auto pr-0" :class="{ 'pr-1': showChangeBlock }">
            <div class="label">{{ label }}</div>
        </div>
        <div :class="{ col: showChangeBlock, 'col-auto d-flex pl-2 pl-sm-3': !showChangeBlock }">
            <slot name="activeItem" v-if="!showChangeBlock"></slot>
            <div class="bg-gray w-100" v-if="showChangeBlock">
                <slot name="options"></slot>
                <div class="text-right mt-15">
                    <button
                        class="btn btn-black"
                        @click="!isAvailable ? ($emit('save'), (showChangeBlock = false)) : ''"
                        :disabled="isAvailable"
                    >
                        Apply
                    </button>
                </div>
            </div>
        </div>
        <div class="col-auto pl-0 pl-sm-3 pr-0">
            <a href.prevent class="link-grey" v-if="!showChangeBlock" @click="showChangeBlock = true">{{ linkName }}</a>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'ItemParam',
        props: {
            label: {
                type: String,
                required: true,
                default: '',
            },
            linkName: {
                type: String,
                required: false,
                default: '',
            },
            isAvailable: {
                type: Boolean,
                default: true,
            },
        },
        data() {
            return {
                showChangeBlock: false,
            };
        },
    };
</script>
<style lang="less" scoped>
    .bg-gray {
        background: @grey3;
        padding: 11px 11px 9px 9px;
        border-radius: 2px;

        @media @xs {
            position: absolute;
            left: 9px;
            max-width: 120px;
            z-index: 100;
        }

        .btn-black {
            font-size: 12px;
            padding: 0px 5px;
        }
    }
</style>
