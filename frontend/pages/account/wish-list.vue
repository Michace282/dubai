<template>
    <div class="container">
        <base-title title="Personal account" />
        <div class="row mt-45">
            <div class="col-2">
                <product-item class="product-sm" :id="'1'" :name="'123213'" :price="321321" />
            </div>
        </div>
        <div class="bg-gray">
            <div class="text">Would you like to save information about all your orders? Sign Up now!</div>
            <button class="btn btn-black">Sign Up</button>
        </div>
    </div>
</template>
<script>
    import BaseTitle from '../../components/BaseTitle.vue';
    import ProductItem from '../../components/catalog/ProductItem.vue';
    export default {
        name: 'wish-list',
        components: { BaseTitle, ProductItem },
        created() {
            this.$store.commit('set_breadcrumbs', [{ route: '', name: 'personal account' }]);
        },
    };
</script>
<style lang="less" scoped>
    .bg-gray {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 60px;
        background: @grey3;
        font-size: 18px;
        line-height: 22px;
        text-transform: uppercase;
        color: @black;
        padding: 32px 30px;

        .btn-black {
            padding: 7px 47px;
        }
    }
</style>
