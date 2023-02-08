import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _e9b98470 = () => interopDefault(import('../pages/about-us.vue' /* webpackChunkName: "pages/about-us" */))
const _cbd4fa14 = () => interopDefault(import('../pages/account/index.vue' /* webpackChunkName: "pages/account/index" */))
const _4e670e9f = () => interopDefault(import('../pages/catalog.vue' /* webpackChunkName: "pages/catalog" */))
const _12bb0ebd = () => interopDefault(import('../pages/contacts.vue' /* webpackChunkName: "pages/contacts" */))
const _34be80b2 = () => interopDefault(import('../pages/create-order.vue' /* webpackChunkName: "pages/create-order" */))
const _4940a3a6 = () => interopDefault(import('../pages/new.vue' /* webpackChunkName: "pages/new" */))
const _7b9700f2 = () => interopDefault(import('../pages/password-reset.vue' /* webpackChunkName: "pages/password-reset" */))
const _8fb48e0c = () => interopDefault(import('../pages/password-reset-confirm.vue' /* webpackChunkName: "pages/password-reset-confirm" */))
const _2e9f220c = () => interopDefault(import('../pages/payment.vue' /* webpackChunkName: "pages/payment" */))
const _32e472c9 = () => interopDefault(import('../pages/returns.vue' /* webpackChunkName: "pages/returns" */))
const _3c3d9cb0 = () => interopDefault(import('../pages/account/active-orders.vue' /* webpackChunkName: "pages/account/active-orders" */))
const _5c113444 = () => interopDefault(import('../pages/account/contact.vue' /* webpackChunkName: "pages/account/contact" */))
const _a97f85c2 = () => interopDefault(import('../pages/account/previous-orders.vue' /* webpackChunkName: "pages/account/previous-orders" */))
const _71b692b3 = () => interopDefault(import('../pages/account/track-orders.vue' /* webpackChunkName: "pages/account/track-orders" */))
const _3e4fbd28 = () => interopDefault(import('../pages/account/wish-list.vue' /* webpackChunkName: "pages/account/wish-list" */))
const _64a75274 = () => interopDefault(import('../pages/page/_slug.vue' /* webpackChunkName: "pages/page/_slug" */))
const _38639169 = () => interopDefault(import('../pages/pay/_slug.vue' /* webpackChunkName: "pages/pay/_slug" */))
const _9203cc20 = () => interopDefault(import('../pages/product/_slug.vue' /* webpackChunkName: "pages/product/_slug" */))
const _2dfb1658 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/about-us",
    component: _e9b98470,
    name: "about-us"
  }, {
    path: "/account",
    component: _cbd4fa14,
    name: "account"
  }, {
    path: "/catalog",
    component: _4e670e9f,
    name: "catalog"
  }, {
    path: "/contacts",
    component: _12bb0ebd,
    name: "contacts"
  }, {
    path: "/create-order",
    component: _34be80b2,
    name: "create-order"
  }, {
    path: "/new",
    component: _4940a3a6,
    name: "new"
  }, {
    path: "/password-reset",
    component: _7b9700f2,
    name: "password-reset"
  }, {
    path: "/password-reset-confirm",
    component: _8fb48e0c,
    name: "password-reset-confirm"
  }, {
    path: "/payment",
    component: _2e9f220c,
    name: "payment"
  }, {
    path: "/returns",
    component: _32e472c9,
    name: "returns"
  }, {
    path: "/account/active-orders",
    component: _3c3d9cb0,
    name: "account-active-orders"
  }, {
    path: "/account/contact",
    component: _5c113444,
    name: "account-contact"
  }, {
    path: "/account/previous-orders",
    component: _a97f85c2,
    name: "account-previous-orders"
  }, {
    path: "/account/track-orders",
    component: _71b692b3,
    name: "account-track-orders"
  }, {
    path: "/account/wish-list",
    component: _3e4fbd28,
    name: "account-wish-list"
  }, {
    path: "/page/:slug?",
    component: _64a75274,
    name: "page-slug"
  }, {
    path: "/pay/:slug?",
    component: _38639169,
    name: "pay-slug"
  }, {
    path: "/product/:slug?",
    component: _9203cc20,
    name: "product-slug"
  }, {
    path: "/",
    component: _2dfb1658,
    name: "index"
  }, {
    path: "/catalog/:product",
    components: {
      default: _4e670e9f
    },
    name: "catalog-product"
  }, {
    path: "/catalog/:product/:type",
    components: {
      default: _4e670e9f
    },
    name: "catalog-product-type"
  }, {
    path: "password-reset",
    components: {
      default: _7b9700f2
    },
    name: "password-reset"
  }, {
    path: "/password-reset/:uid/:token",
    components: {
      default: _8fb48e0c
    },
    name: "password-reset-token"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
