import auth from '../api/auth';

import {
  PASSWORD_RESET_BEGIN,
  PASSWORD_RESET_CLEAR,
  PASSWORD_RESET_FAILURE,
  PASSWORD_RESET_SUCCESS,
  PASSWORD_EMAIL_BEGIN,
  PASSWORD_EMAIL_CLEAR,
  PASSWORD_EMAIL_FAILURE,
  PASSWORD_EMAIL_SUCCESS,
} from './types';


export const getters = {
  user (state) {
    return state.user
},
loading (state) {
    return state.loading
},
error (state) {
    return state.error
},
success (state) {
    return state.success
}
}


export const state = () => ({
    breadcrumbs: false,
    favorites: {},
    payLink: null,
    windowWidth: null,
    emailCompleted: false,
    emailError: false,
    emailLoading: false,
    resetCompleted: false,
    resetError: false,
    resetLoading: false,
    user: null,
    loading: false,
    error: null,
    success: null
});

export const mutations = {
    setUser (state, payload) {
        state.user = payload
    },
    setLoading (state, payload) {
        state.loading = payload
    },
    setError (state, payload) {
        state.error = payload
    },
    clearError (state) {
        state.error = null
    },
    setSuccess (state, payload) {
        state.success = payload
    },
    clearSuccess (state) {
        state.success = null
    },
    update_favorites(state, el) {
        state.favorites[el.id] = el.isFavorite;
    },
    set_breadcrumbs(state, breadcrumbs) {
        state.breadcrumbs = breadcrumbs;
    },
    set_pay_link(state, link) {
        state.payLink = link;
    },
    set_window_width(state, width) {
        state.windowWidth = width;
    },
    [PASSWORD_RESET_BEGIN](state) {
      state.resetLoading = true;
  },
  [PASSWORD_RESET_CLEAR](state) {
      state.resetCompleted = false;
      state.resetError = false;
      state.resetLoading = false;
  },
  [PASSWORD_RESET_FAILURE](state) {
      state.resetError = true;
      state.resetLoading = false;
  },
  [PASSWORD_RESET_SUCCESS](state) {
      state.resetCompleted = true;
      state.resetError = false;
      state.resetLoading = false;
  },
  [PASSWORD_EMAIL_BEGIN](state) {
      state.emailLoading = true;
  },
  [PASSWORD_EMAIL_CLEAR](state) {
      state.emailCompleted = false;
      state.emailError = false;
      state.emailLoading = false;
  },
  [PASSWORD_EMAIL_FAILURE](state) {
      state.emailError = true;
      state.emailLoading = false;
  },
  [PASSWORD_EMAIL_SUCCESS](state) {
      state.emailCompleted = true;
      state.emailError = false;
      state.emailLoading = false;
  },
};

import user_query from '~/graphql/queries/user.graphql';
import verify_token from '~/graphql/mutations/user/verifyToken.graphql';
import cookieUniversal from 'cookie-universal';

export const actions = {
    restorePassword ({commit}, payload) {
    commit('setLoading', true)
    commit('clearError')

    let url = '/api' + process.env.RESTORE_PASSWORD_PATH
    const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
       email: payload.email
    })
  };
  fetch(url, requestOptions)
      .then(() => {
        commit('setLoading', false)
        commit('setSuccess', ['Further actions have been sent to the email you specified.'])
        this.$router.push('/')
      })
      .catch(error => {
        commit('setLoading', false)
        commit('setError', error)
      })
  },
  restorePasswordConfirm ({commit}, payload) {
    commit('setLoading', true)
    commit('clearError')

    let url = '/api' + process.env.RESTORE_PASSWORD_CONFIRM_PATH

     const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      uid: payload.uid,
      token: payload.token,
      new_password1: payload.new_password1,
      new_password2: payload.new_password2
    })
  };
  fetch(url, requestOptions)
      .then(() => {
        commit('setLoading', false)
        commit('setSuccess', ['New password was set.'])
        this.$router.push('/')
      })
      .catch(error => {
        commit('setLoading', false)
        commit('setError', error)
      })
  },
    resetPassword({ commit }, { uid, token, password1, password2 }) {
      commit(PASSWORD_RESET_BEGIN);
      return auth.resetAccountPassword(uid, token, password1, password2)
      .then(() => commit(PASSWORD_RESET_SUCCESS))
      .catch(() => commit(PASSWORD_RESET_FAILURE));
  },
  sendPasswordResetEmail({ commit }, { email }) {
      commit(PASSWORD_EMAIL_BEGIN);
      return auth.sendAccountPasswordResetEmail(email)
      .then(() => commit(PASSWORD_EMAIL_SUCCESS))
      .catch(() => commit(PASSWORD_EMAIL_FAILURE));
  },
  clearResetStatus({ commit }) {
      commit(PASSWORD_RESET_CLEAR);
  },
  clearEmailStatus({ commit }) {
      commit(PASSWORD_EMAIL_CLEAR);
  },
  async nuxtServerInit({ commit }, context) {
    let client = context.app.apolloProvider.defaultClient;
    let token = context.app.$apolloHelpers.getToken();
    if (token && token != undefined) {
        try {
            await client
            .mutate({
                mutation: verify_token,
                variables: {
                    token: token,
                },
            })
            .then(async (data1) => {
                if (data1.data.verifyToken.payload.exp - 60 < parseInt(new Date().getTime() / 1000)) {
                    const cookie_object = cookieUniversal(context.req, context.res);
                    cookie_object.set('dubai', undefined);
                    context.app.$apolloHelpers.onLogout(client);
                    context.app.$apolloHelpers.onLogout();
                    commit('user/logout');
                    try {
                        client.resetStore();
                    } catch (e) {
                        console.log(e);
                    }
                } else {
                    let user = await client.query({
                        query: user_query,
                    });
                    commit('user/update_user', user.data.user);
                }
            })
            .catch((data) => {
                const cookie_object = cookieUniversal(context.req, context.res);
                cookie_object.set('dubai', undefined);
                context.app.$apolloHelpers.onLogout(client);
                context.app.$apolloHelpers.onLogout();
                commit('user/logout');
                try {
                    client.resetStore();
                } catch (e) {
                    console.log(e);
                }
            });
        } catch (e) {
            const cookie_object = cookieUniversal(context.req, context.res);
            cookie_object.set('dubai', undefined);
            context.app.$apolloHelpers.onLogout(client);
            context.app.$apolloHelpers.onLogout();
            commit('user/logout');
            try {
                client.resetStore();
            } catch (e) {
                console.log(e);
            }
        }
    }
},
};
