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
        title: '',
        titleTemplate: '%s - DC&S Dubai',
        meta: [
            {charset: 'utf-8'},
            {name: 'viewport', content: 'width=device-width, initial-scale=1'},
            {hid: 'description', name: 'description', content: ''},
            {property: 'og:title', content: ''},
            {property: 'og:description', content: ''},
            {property: 'og:image', content: ''},
            {name: 'facebook-domain-verification', content: '6nsvljwenn82qxzvx61lbl4t0rowju'},
        ],
        link: [
            {rel: 'shortcut icon', href: '/favicon.ico'},
            {rel: 'icon', type: 'image/vnd.microsoft.icon', href: '/favicon.ico'},
            {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'},
            {rel: 'icon', href: '/favicon.ico'},
        ],
    },
    /*
     ** Customize the progress-bar color
     */
    loading: {color: '#fff'},
    /*
     ** Global CSS
     */
    css: ['~assets/css/fonts.less', '~assets/css/main.less', 'vue-slick-carousel/dist/vue-slick-carousel.css'],

    /*
     ** Plugins to load before mounting the App
     */
    plugins: [
        // '~plugins/axios',
        '~plugins/components.server.js',
        '~/plugins/global-components.js',
        {src: '~/plugins/vuelidate.js'},
        {src: '~plugins/components.client.js', ssr: false},
        {src: '~/plugins/vuejs-paginate.js', ssr: false},
        {src: '~/plugins/vue-slick-carousel.js', ssr: false},
    ],
    /*
     ** Nuxt.js dev-modules
     */
    buildModules: [
        '@nuxtjs/style-resources',
        '@nuxtjs/google-analytics'
    ],

    googleAnalytics: {
        id: 'UA-194963105-1'
    },

    /*
     ** Nuxt.js modules
     */
    modules: [
        'bootstrap-vue/nuxt',
        'cookie-universal-nuxt',
        '@nuxtjs/device',
        '@nuxtjs/apollo',
        '@nuxtjs/dotenv',
        '@nuxtjs/moment',
    ],

    styleResources: {
        less: './assets/css/variables.less',
    },

    moment: {
        locales: ['ru'],
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
    router: {
        extendRoutes(routes, resolve) {
            routes.push({
                name: 'catalog-product',
                path: '/catalog/:product',
                components: {
                    default: resolve(__dirname, 'pages/catalog.vue'),
                },
            });
            routes.push({
                name: 'catalog-product-type',
                path: '/catalog/:product/:type',
                components: {
                    default: resolve(__dirname, 'pages/catalog.vue'),
                },
            });
        }
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
        extend(config, ctx) {
        },
    },
};
