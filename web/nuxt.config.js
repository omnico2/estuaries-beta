export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
   head: {
    title: 'Estuaries',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  loading: { color: '#fff' },
  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
      '~assets/argon/vendor/nucleo/css/nucleo.css',
      '~assets/argon/vendor/font-awesome/css/font-awesome.css',
      '~assets/argon/scss/argon.scss',
      'bootstrap-vue/dist/bootstrap-vue.css'
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: ['~/plugins/vAvatar.js'
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
  ],
  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/pwa',
    '@nuxt/content',
  ],
  render: {
  // HTTP2: https://nuxtjs.org/api/configuration-render/#http2
    http2: {
      push: true,
      pushAssets: (req, res, publicPath, preloadFiles) =>
        preloadFiles
          .filter(f => f.asType === 'script' && f.file === 'runtime.js')
          .map(f => `<${publicPath}${f.file}>; rel=preload; as=${f.asType}`)
    }
  },
  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
      proxy: true,
  },
  proxy: {
      '/server/': {
          target: 'https://omnico2.pythonanywhere.com/api/',
          pathRewrite: { '/server/': '' },
      },
  },
  auth: {
      cookie: true,
      redirect: {
          callback: '/callback',
          logout: '/signed-out',
          home: false,
          secure: false,
      },
      strategies: {
          local: {
              tokenType: 'JWT',
              endpoints: {
                  login: { url: '/server/rest-auth/login/', method: 'post', propertyName: 'token' },
                  user: { url: '/server/rest-auth/user/', method: 'get', propertyName: '' }
              }
          },
          google: {
              client_id: 'YOUR_GOOGLE_CLIENT_ID',
              response_type: 'code token',
              scope: ['email', 'profile'],
              userinfo_endpoint: '/server/rest-auth/user/'
          },
          facebook: {
              clientId: 'FACEBOOK_KEY',
              responseType: 'code token',
              scope: ['public_profile', 'email', 'user_birthday'],
              userinfo_endpoint: '/server/rest-auth/user/'
          }
      }
  },
  // Content module configuration (https://go.nuxtjs.dev/config-content)
  content: {},
  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    loaders: {
      cssModules: {
        modules: {
          localIdentName: '[hash:base64:4]'
        }
      }
    }
  },
}
