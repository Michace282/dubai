<template>
    <div class="loader">
        <div class="blick"></div>
        <img src="~/assets/images/loader.png" alt="loader" />
    </div>
</template>
<script>
    export default {
        name: 'Loader',
    };
</script>
<style lang="less" scoped>
    .loader {
        width: 100%;
        height: 100%;
        // position: absolute;
        // top: 0;
        // left: 0;
        display: flex;
        align-items: flex-start;
        justify-content: center;
        z-index: 1000;
        background: @white;

        .blick {
            width: 30px;
            height: 300px;
            transform: rotate(45deg);
            background: #ffffffad;
            position: absolute;
            top: 0;
            animation: slide 2s ease infinite;
            filter: blur(7px);
        }

        img {
            margin-top: 50px;
        }
    }

    @keyframes slide {
        from {
            left: 0px;
        }
        to {
            left: 1000px;
        }
    }
</style>
