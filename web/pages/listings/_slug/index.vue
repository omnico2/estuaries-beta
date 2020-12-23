<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ listings.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
      <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="listings.image"
          alt>
      </div>
      <div class="col-md-4">
          <div>
            <h2>Price</h2>
            <h2>{{listings.price}}</h2>            
          </div>
          <div>
            <h3>Description</h3>
            <p>{{listings.description}}</p>
          </div>
          <nuxt-link :to="`/listings/${listings.slug}/edit`" >
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
            return this.$auth.user.pk == this.listings.author_id;
        },
    },
    head(){
        return{
            title: 'view listings'
        }
    },
    data(){
        return{
            listings: []
        }
    },
    async asyncData({$axios, params}) {
        try{
            let listings = await $axios.$get(`/server/listings/${params.slug}/`)
            console.log(listings)
            return{ listings }
        } catch{}
            console.log()
    },
  methods: {
    async submitListings({$axios, listings}) {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.listings) {
        formData.append(data, listings[data]);
      }
      try {
        let response = await this.$axios.$post("/server/listings/${listings.slug}/", formData, config);
        this.$router.push("/listings/");
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>

<style>

</style>