<template>
    <div class="container">
        <base-title title="Catalogue" class="mt-15" />
        <div class="row mt-45">
            <div class="col-3">
                <filter-catalog />
            </div>
            <div class="col-9">
                <div class="prudocts-head">
                    <div class="breadcrumbs">

                    </div>
                    <div class="sort">

                    </div>
                </div>
                <div class="row">
                    <div class="col-4">
                        <product-item name="Body Merelyn" :price="900"/>
                    </div>
                    <div class="col-4">
                        <product-item name="Body Alexa" :price="900" />
                    </div>
                    <div class="col-4">
                        <product-item name="Body Addison" :price="800"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import ProductItem from '../components/catalog/ProductItem.vue';
    import FilterCatalog from '../components/catalog/FilterCatalog.vue';
    export default {
        components: { ProductItem, FilterCatalog },
        name: 'catalog',
        created() {
            this.$store.commit('set_breadcrumbs', [
                { link: 'index', name: 'Home' },
                { link: 'caatlog', name: 'Catalogue' },
            ]);
        },
    };
</script>
<style lang="less" scoped></style>
