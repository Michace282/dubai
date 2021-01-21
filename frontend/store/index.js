export const state = () => ({
    breadcrumbs: false,
});

export const mutations = {
    set_breadcrumbs(state, breadcrumbs) {
        console.log(state.breadcrumbs);
        state.breadcrumbs = breadcrumbs;
    }
};

// export const actions = {};

// export const getters = {};
