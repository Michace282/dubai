export const state = () => ({
    basketItems: [],
    itemsCount: 0,
});

export const mutations = {
    update_basket(state, basket) {
        state.basketItems = [...basket];
        state.itemsCount = state.basketItems.length;
    },
    update_item_param(state, item) {
        state.basketItems[item.index][item.param] = item.val;
    },
    update_items_count(state) {
        state.itemsCount = 0;
        for (let i in this.$cookies.get('basket')) {
            state.itemsCount = state.itemsCount + 1;
        }
    },
};
