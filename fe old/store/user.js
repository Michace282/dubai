export const state = () => ({
    user: null,
    guestUuid: null,
});

export const mutations = {
    update_guestUuid(state, uuid) {
        state.guestUuid = uuid;
    },
    update_user(state, user) {
        state.user = user;
    },
    logout(state) {
        state.user = null;
    }
};
