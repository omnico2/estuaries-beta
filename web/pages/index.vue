<template>
<main>
<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="https://downloads.intercomcdn.com/i/o/39270330/291522149778600b9ba16287/sharetribe_cover-picture_blurry-lights.jpg" alt="First slide">
      <div class="carousel-caption d-none d-md-block">
    <strong>Welcome to Estuaries</strong>
    <title>A Marktplace cms</title>
  </div>
    </div>
  </div>
</div>
    <div class="container page" >
    <div class="row" >
    <div class="col-xs-12 col-md-3">
          <div class="sidebar">
            <p>Popular Tags</p>

          </div>
    </div>
<b-container class="col-xs-12 col-md-9">
    <div class="row" >
      <template v-for="listing in listings">
          <div :key="listing.id" class="col-md-4">
              <listing-card :listing="listing"></listing-card>
          </div>
      </template>
    </div>
</b-container>
  </div>
</div>
</main>
</template>

<script>
import Card from "~/components/Card.vue";
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

<style>
title {
    display: block;
}
.carousel-caption {
    position: absolute;
    right: 15%;
    bottom: 130px;
    left: 15%;
    z-index: 10;
    padding-top: 20px;
    padding-bottom: 20px;
    color: #fff;
    text-align: center;
    font-size: 75px;
}
</style>
