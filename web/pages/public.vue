<template>
    <div>
    	<h2 class="subtitle">
        	<template v-if="$auth.loggedIn">Logged in as {{ $auth.user.pk }}</template>
        	<template v-else>Nuxt + Django + Auth</template>
      	</h2>
        <b-alert show variant="success">
            You should see this page without need to authentication!
        </b-alert>
    </div>
</template>

<script>
export default {
    middleware: ['auth'],
    options: {
        auth: false
    }
}
</script>
