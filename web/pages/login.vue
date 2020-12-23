<template>
    <section class="section section-shaped section-lg my-0">
        <div class="shape shape-style-1 bg-gradient-default">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
        <div class="container pt-lg-md">
            <div class="row justify-content-center">
                <div class="col-lg-5">
                    <card type="secondary" shadow
                          header-classes="bg-white pb-5"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                        <template>
                            <!-- <div class="text-muted text-center mb-3">
                                <small>Sign in with</small>
                            </div> -->
                            <div class="btn-wrapper text-center">
                                <!-- <base-button type="neutral">
                                    <img slot="icon" src="img/icons/common/github.svg">
                                    Github
                                </base-button> -->

                                <base-button type="neutral">
                                    <img slot="icon" src="img/icons/common/google.svg">
                                    Sign with Google
                                </base-button>
                            </div>
                        </template>
                        <template>
                            <div class="text-center text-muted mb-4">
                                <small>Or sign in with credentials</small>
                            </div>
                            <form role="form">
                                <base-input alternative
                                            v-model="email"
                                            class="mb-3"
                                            placeholder="Email"
                                            addon-left-icon="ni ni-email-83">
                                </base-input>
                                <base-input alternative
                                            v-model="password"
                                            type="password"
                                            placeholder="Password"
                                            addon-left-icon="ni ni-lock-circle-open">
                                </base-input>
                                <base-checkbox>
                                    Remember me
                                </base-checkbox>
                                <div class="text-center">
                                    <base-button type="primary" class="my-4" @click="login">Sign In</base-button>
                                </div>
                            </form>
                        </template>
                    </card>
                    <div class="row mt-3">
                        <div class="col-6">
                            <a href="#" class="text-light">
                                <small>Forgot password?</small>
                            </a>
                        </div>
                        <div class="col-6 text-right">
                            <nuxt-link to="register">
                            <a class="text-light">
                                <small>Create new account</small>
                            </a>
                            </nuxt-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
import busyOverlay from '~/components/busy-overlay'

export default {
    middleware: ['auth'],
    components: {busyOverlay},
    data () {
        return {
            email: '',
            password: '',
            error: null
        }
    },
    computed: {
        strategies: () => [
            { key: 'google', name: 'Google', color: '#4284f4' }
        ],
        redirect () {
            return (
                this.$route.query.redirect &&
                decodeURIComponent(this.$route.query.redirect)
            )
        },
        isCallback () {
            return Boolean(this.$route.query.callback)
        },
        errorMessage () {
            const {error} = this
            if (!error || typeof error === 'string') {
                return error
            }
            let msg = ''
            if (error.message) {
                msg += error.message
            }
            if (error.errors) {
                msg += `(${JSON.stringify(error.errors)
                    .replace(/[{}"[\]]/g, '')
                    .replace(/:/g, ': ')
                    .replace(/,/g, ' ')})`
            }
            return msg
        }
    },
    methods: {
        async login () {
            this.error = null

            return this.$auth
                .loginWith('local', {
                    data: {
                        email: this.email,
                        password: this.password
                    }
                })
                .then(() => {
                    this.$router.push('/secure')
                })
                .catch((e) => {
                    this.error = e.response.data
                })
        }
    }
}
</script>
<style>
</style>
