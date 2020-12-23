<template>
  <div class="card listing-card">
   <nuxt-link :to="`/listings/${listing.slug}/`">
    <img :src="listing.image" class="card-img-top">
   </nuxt-link>
   <nuxt-link :to="`/listings/${listing.slug}/`">
    <div class="card-body">
      <h5 class="listing-card-title">{{ listing.name }}</h5>
      <p class="listing-card-price">
       {{ listing.price }}
      </p>
    </div>
   </nuxt-link>
   <nuxt-link :to="`/users/${listing.author_id}/`">
    <div class="card-author">
    <row>
    <vue-letter-avatar :name='listing.author_id' size='40' :rounded=true class="card-a-avatar"/>
      <a class="card-a-text">
       {{ listing.author_id }}
      </a>
    </row>
    </div>
   </nuxt-link>
  </div>
</template>
<script>
import Vue from 'vue';
import VueLetterAvatar from 'vue-letter-avatar';

Vue.use(VueLetterAvatar);

export default {
    props: ["listing"]
};
</script>
<style>
.card-body {
    padding: 0;
}
.card-img-top {
    height: 131px;
    width: 222px;
}
.card-author{
    padding: 3px 3px 3px 3px;
    font-size: 20px;
}
.listing-card {
    width: 225px;
    height: 180px;
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
    margin: 5px 5px 5px 5px;
}
.listing-card-title {
    position: absolute;
    top: -20px;
    left: -25px;
    padding: 25px 20px 25px 20px;
    background-color: #172b4d;
    color: rgba(255,255,255,1);
    font-size: 20px;
    border-radius: 50%;
}
.listing-card-price {
    position: absolute;
    bottom: 0px;
    right: -30px;
    padding: 25px 20px 25px 15px;
    background-color: #28a745;
    color: #ffff;
    font-size: 20px;
    border-radius: 50%;
}
</style>