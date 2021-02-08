export const state = () => ({
    user: null,
    guestUuid: null,
});

export const mutations = {
    update_guestUuid(state, uuid) {
        state.guestUuid = uuid;
    },
};

import user_query from '~/graphql/mutations/user/user.graphql';
import verify_token from '~/graphql/mutations/user/verifyToken.graphql';

import cookieUniversal from 'cookie-universal';

export const actions = {
    // async nuxtServerInit({commit}, context) {
    //     let client = context.app.apolloProvider.defaultClient;
    //     let token = context.app.$apolloHelpers.getToken();
    //     if (token && token != undefined) {
    //         try {
    //             await client
    //                 .mutate({
    //                     mutation: verify_token,
    //                     variables: {
    //                         token: token
    //                     }
    //                 })
    //                 .then(async (data1) => {
    //                     if (data1.data.verifyToken.payload.exp - 60 < parseInt(new Date().getTime() / 1000)) {
    //                         const cookie_object = cookieUniversal(context.req, context.res);
    //                         cookie_object.set("dubai", undefined);
    //                         context.app.$apolloHelpers.onLogout(client);
    //                         context.app.$apolloHelpers.onLogout();
    //                         commit("logout");
    //                         try {
    //                             client.resetStore();
    //                         } catch (e) {
    //                             console.log(e);
    //                         }
    //                     } else {
    //                         let user = await client
    //                             .query({
    //                                 query: user_query
    //                             })
    //                         commit("login", user.data.user, token);
    //                     }
    //                 })
    //                 .catch((data) => {
    //                     const cookie_object = cookieUniversal(context.req, context.res);
    //                     cookie_object.set("dubai", undefined);
    //                     context.app.$apolloHelpers.onLogout(client);
    //                     context.app.$apolloHelpers.onLogout();
    //                     commit("logout");
    //                     try {
    //                         client.resetStore();
    //                     } catch (e) {
    //                         console.log(e);
    //                     }
    //                 });
    //         } catch (e) {
    //             const cookie_object = cookieUniversal(context.req, context.res);
    //             cookie_object.set("dubai", undefined);
    //             context.app.$apolloHelpers.onLogout(client);
    //             context.app.$apolloHelpers.onLogout();
    //             commit("logout");
    //             try {
    //                 client.resetStore();
    //             } catch (e) {
    //                 console.log(e);
    //             }
    //         }
    //     }
    // }
};
