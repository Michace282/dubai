<template>
    <div class="block-title">
        {{ title }}
        <h1 class="front-title">{{ title }}</h1>
    </div>
</template>
<script>
    export default {
        name: 'BaseTitle',
        props: {
            title: {
                type: String,
                required: true,
                default: '',
            },
        },
    };
</script>
<style lang="less" scoped>

    .block-title {
        position: relative;
        font-size: 64px;
        color: @grey3;
        text-transform: uppercase;

        @media @large {
            font-size: 36px;
        }

        .front-title {
            position: absolute;
            font-family: 'Inter-Medium';
            color: @black;
            left: 0;
            font-size: 36px;
            left: 30px;
            bottom: 5px;

            @media @large {
                font-size: 24px;
                left: 19px;
                bottom: 0px;
            }
        }
    }
</style>
