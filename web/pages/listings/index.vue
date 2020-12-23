<template>
  <main class="container mt-6">
    <div class="row">
      <div class="col-12 text-right mb-6">
      </div>
      <template v-for="listing in listings">
          <div :key="listing.id" class="col-md-3">
            <nuxt-link :to="`/listings/${listing.slug}/`">
              <card card-lift--hover :listing="listing"></card>
            </nuxt-link>
          </div>
      </template>
    </div>
  </main>
</template>

<script>
import ListingCard from "~/components/Card.vue";
export default {
  head() {
    return {
      title: "Listings list"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let listings = await $axios.$get(`/server/listings/`);
      return { listings };
    } catch (e) {
      return { listings: [] };
    }
  },
  data() {
    return {
      listings: []
    };
  },
  methods: {
    async deleteListing(listing_id) {
      try {
        await this.$axios.$delete(`/server/listings/${listing_id}/`); 
        let newListings = await this.$axios.$get("/server/listings/"); 
        this.listings = newListings; 
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>

</style>