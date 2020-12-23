<template>
    <div id="wrapper" class="d-flex flex-column">
      <headroom>
        <header class="header-global">
            <app-header></app-header>
        </header>
      </headroom>
        <main class="flex-fill position-relative">
           <nuxt />
        </main>
        <footer class="footer">
            <app-footer></app-footer>
        </footer>
    </div>
</template>

<script>
import AppHeader from "~/components/AppHeader";
import AppFooter from "~/components/AppFooter";
import { headroom } from 'vue-headroom';

export default {
  components: {
    AppHeader,
    AppFooter,
    headroom
  }
};
</script>

<style>
body, #wrapper {
   min-height:100vh;
}
.headroom {
    background-color: #172b4d;
}
</style>