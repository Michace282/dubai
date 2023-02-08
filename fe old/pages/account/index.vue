<template>
    <div class="container">
        <account-head-group />
    </div>
</template>
<script>
    import AccountHeadGroup from '../../components/AccountHeadGroup';
    export default {
        name: 'index',
        components: { AccountHeadGroup },
        head() {
            return {
                title: 'Personal Account'
            };
        },
        created() {
            this.$store.commit('set_breadcrumbs', [{ route: '', name: 'Personal account' }]);
            if (this.$route.params && this.$route.params.userInfoUpdated == 'showToast') {
                this.$bvToast.toast('Update CONTACT INFORMATION', {
                    title: 'Update CONTACT INFORMATION',
                    variant: 'success',
                });
            }
        },
    };
</script>
<style lang="less" scoped></style>
