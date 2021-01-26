// require('dotenv').config()
const isDev = process.env.NODE_ENV !== 'production';
export default {
    mode: 'universal',
    ...(!isDev && {
        modern: 'client',
    }),
    /*
     ** Headers of the page
     */
    head: {
        title: process.env.npm_package_name || '',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' },
            { property: 'og:title', content: '' },
            { property: 'og:description', content: '' },
            { property: 'og:image', content: '' },
        ],
        link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },
    /*
     ** Customize the progress-bar color
     */
    loading: { color: '#fff' },
    /*
     ** Global CSS
     */
    css: ['~assets/css/fonts.less', '~assets/css/main.less'],

    /*
     ** Plugins to load before mounting the App
     */
    plugins: [
        // '~plugins/axios',
        '~plugins/components.server.js',
        '~plugins/components.client.js',
        '~/plugins/global-components.js',
    ],
    /*
     ** Nuxt.js dev-modules
     */
    buildModules: [],

    /*
     ** Nuxt.js modules
     */
    modules: ['bootstrap-vue/nuxt', 'cookie-universal-nuxt', '@nuxtjs/device', '@nuxtjs/apollo', '@nuxtjs/dotenv'],

    styleResources: {
        less: './assets/css/variables.less',
    },

    apollo: {
        tokenName: 'jwt_token',
        cookieAttributes: {
            expires: 6,
            path: '/',
        },
        errorHandler: '~/plugins/apollo-error-handler.js',
        includeNodeModules: true,
        $query: {
            loadingKey: 'loading',
        },
        authenticationType: 'JWT',
        clientConfigs: {
            default: '~/plugins/apollo.js',
        },
    },
    watchers: {
        webpack: {
            aggregateTimeout: 300,
            poll: 1000,
        },
    },
    devServer: {
        public: process.env.DOCKER_URL || 'localhost:3000',
    },
    /*
     ** Build configuration
     */
    build: {
        /*
         ** You can extend webpack config here
         */
        extend(config, ctx) {},
    },
};
