<template>
    <div>
        <TheNavbar />
        <div class="container">
            <div class="breadcrumbs" v-if="breadcrumbs && breadcrumbs.length > 0">
                <nuxt-link
                    class="breadcrumb"
                    :to="{ name: breadcrumb.link }"
                    v-for="(breadcrumb, index) in breadcrumbs"
                    :key="index"
                >
                    {{ breadcrumb.name }}
                    <span class="separator" v-if="index != breadcrumbs.length - 1">/</span>
                </nuxt-link>
            </div>
        </div>
        <nuxt />
        <TheFooter />
    </div>
</template>
<script>
    import TheNavbar from '~/components/TheNavbar.vue';
    import TheFooter from '~/components/TheFooter.vue';
    export default {
        components: { TheNavbar, TheFooter },
        computed: {
            breadcrumbs() {
                return this.$store.state.breadcrumbs;
            },
        },
    };
</script>
<style lang="less" scoped>
    @import '../assets/css/colors.less';

    .breadcrumbs {
        display: flex;
        flex-wrap: wrap;
        margin: 30px 0px 20px 0px;

        .breadcrumb {
            text-decoration: none;
            padding: 0px;
            font-family: 'Inter-ExtraLight';
            background-color: unset;
            font-size: 14px;
            text-transform: uppercase;
            color: @grey4;

            .separator {
                margin: 0px 10px;
            }
        }
    }
</style>
