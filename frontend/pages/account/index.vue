<template>
    <div class="container">
        <base-title title="Personal account" />
        <account-head-group />
    </div>
</template>
<script>
    import AccountHeadGroup from '../../components/AccountHeadGroup';
    export default {
        name: 'index',
        components: { AccountHeadGroup },
        created() {
            this.$store.commit('set_breadcrumbs', [{ route: '', name: 'Personal account' }]);
        },
    };
</script>
<style lang="less" scoped></style>
