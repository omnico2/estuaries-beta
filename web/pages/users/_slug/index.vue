<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ users.username }}</h2>
      </div>
      <div class="col-md-6 mb-4">
      <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="users.profilepic"
          alt>
      </div>
      <div class="col-md-4">
          <div>
            <h2>Email</h2>
            <h2>{{users.email}}</h2>            
          </div>
          <div>
            <h3>member since</h3>
            <p>{{users.member_since}}</p>
          </div>
          <div>
            <h3>Last login</h3>
            <p>{{users.last_login}}</p>
          </div>
          <div>
            <h3>About</h3>
            <p>{{users.about_you}}</p>
          </div>
          <nuxt-link :to="`/user/${users.slug}/edit`" >
          <div v-if="$auth.$state.loggedIn">
            <button v-if="author" class="btn btn-primary">Edit</button>
          </div>
          </nuxt-link>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  auth: false,
  middleware: ['auth'],
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        },
        author() {
            return this.$auth.user.pk == this.users.username;
        },
    },
    head(){
        return{
            title: 'view users'
        }
    },
    data(){
        return{
            users: []
        }
    },
    async asyncData({$axios, params}) {
        try{
            let users = await $axios.$get(`/server/user/${params.slug}/`)
            console.log(users)
            return{ users }
        } catch{}
            console.log()
    },
  methods: {
    async submitListings({$axios, users}) {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.users) {
        formData.append(data, users[data]);
      }
      try {
        let response = await this.$axios.$post("/server/user/${users.slug}/", formData, config);
        this.$router.push("/users/");
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>

<style>

</style>