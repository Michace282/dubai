<template>
    <div class="block-title">
        <div class="title-shadow">{{ title }}</div>
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
        font-size: 62px;
        color: @grey3;
        text-transform: uppercase;
        
        
        .title-shadow {
            @media @medium {
                display: none;
            }  
        }

        @media @large {
            font-size: 39px;
        }
        @media @medium {
            margin: 60px 0;
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
                bottom: -2px;
            }
            @media @medium {
                left: 0;
                // margin: 20px 0;
            }    
        }
    }
</style>
