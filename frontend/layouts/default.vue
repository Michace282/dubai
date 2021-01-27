<template>
    <div>
        <TheNavbar @showRegModal="showRegForm = true" />
        <div class="position-relative">
            <RegForm
                :class="{ active: showRegForm }"
                @hide="showRegForm = false"
                @showAuthModal="
                    showRegForm = false;
                    showAuthForm = true;
                "
            />
            <AuthForm
                :class="{ active: showAuthForm }"
                @hide="showAuthForm = false"
                @showRegModal="
                    showAuthForm = false;
                    showRegForm = true;
                "
            />
            <div class="content" :class="{ hide: showRegForm || showAuthForm }">
                <div class="container">
                    <div class="breadcrumbs" v-if="breadcrumbs && breadcrumbs.length > 0">
                        <nuxt-link
                            class="breadcrumb mb-0"
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
            </div>
        </div>
        <TheFooter />
    </div>
</template>
<script>
    import TheNavbar from '~/components/TheNavbar.vue';
    import TheFooter from '~/components/TheFooter.vue';
    import RegForm from '~/components/auth/RegForm';
    import AuthForm from '~/components/auth/AuthForm';
    export default {
        components: { TheNavbar, TheFooter, RegForm, AuthForm },
        data() {
            return {
                showRegForm: false,
                showAuthForm: false,
            };
        },
        computed: {
            breadcrumbs() {
                return this.$store.state.breadcrumbs;
            },
        },
    };
</script>
<style lang="less" scoped>
    .breadcrumbs {
        display: flex;
        flex-wrap: wrap;
        padding: 30px 0px 20px 0px;

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

    .content {
        transition: opacity 0.3s;
        &.hide {
            opacity: 0;
        }
    }
</style>
