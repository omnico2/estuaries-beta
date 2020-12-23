<template>
    <header class="header-global">
        <base-nav class="navbar-main" type="" transparent effect="dark" expand>
            <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
                Estuaries
            </router-link>

            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <a href="/">
                        Estuaries
                    </a>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>
            <ul class="navbar-nav  navbar-nav-hover ml-lg-auto">
                <base class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="/listings/add" class="nav-link">
                        <i class="ni ni-ui-04 d-lg-none"></i>
                        <button type="button" class="btn btn-warning">Add Listing</button>
                    </a>
                   <template v-if="$auth.$state.loggedIn">

                <base-dropdown tag="li" class="nav-item">
                    <a slot="title" class="nav-link" data-toggle="dropdown" role="button">
                        <i class="ni ni-collection d-lg-none"></i>
                        <vue-letter-avatar :name="$auth.user.username" size='40' :rounded=true />
                    </a>
                    <button class="dropdown-item" @click=$auth.logout()>Logout</button>
                    <router-link :to="'/users/' + $auth.user.username" class="dropdown-item">Profile</router-link>
                </base-dropdown>
                    </template>
                    <template v-else>
                <base class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="/login" class="nav-link">
                        <i class="ni ni-ui-04 d-lg-none"></i>
                        <span>Log in</span>
                    </a>
                </base>
                <base class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="/register" class="nav-link">
                        <i class="ni ni-ui-04 d-lg-none"></i>
                        <span>Register</span>
                    </a>
                </base>
              </template>
            </ul>
        </base-nav>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";
import VueLetterAvatar from 'vue-letter-avatar';
import Vue from 'vue';

Vue.use(VueLetterAvatar);

export default {

    components: {
        BaseNav,
        CloseButton,
        BaseDropdown
    }
};
</script>

<style>
.navbar-main {
    height: 65px;
}
.nav-link {
    line-height: 35px;
}
</style>
