<template>
    <div>
      <div class="col-md-6 mb-4">
      <img
          v-if="preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="preview"
          alt>
        <img
          v-else
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="listings.image">
      </div>
      <div class="col-md-4">
        <form @submit="submitedit">
          <div class="form-group">
            <label for>Listing Name</label>
            <input type="text" class="form-control" v-model="listings.name">
          </div>
          <div class="form-group">
            <label for>Image</label>
            <input type="file" name="image" @change="onFileChange">
          </div>
          <div class="form-group">
            <label for>Price</label>
            <input type="numer" class="form-control" v-model="listings.price">
          </div>
          <div class="form-group">
            <label for>Listings Description</label>
            <input type="text" class="form-control" v-model="listings.description">
          </div>
          <button v-if="editable" type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
  </div>
</div>
</template>

<script>
export default {
  head() {
    return {
      title: "Add Listings"
    };
  },
  middleware: ['auth'],
    computed: {
      state () {
        return JSON.stringify(this.$auth.$state, undefined, 2)
      },
      editable() {
        return this.$auth.user.pk == this.listings.author_id;
      },
  },
  data(){
    return{
      value: false,
      nameRules: [
        v => !! v || 'Any contents is required'
      ],
     listings: 
     {
        name: "",
        description: "",
        price: "",
        image: "",
        slug: "",
      },
      preview: ""
    };
  },
  async asyncData({$axios, params}){
    try{
      let listings = await $axios.$get(`/server/listings/${params.slug}/`)
      return { listings }
    } catch(e){console.log(e)}
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.listings.image = files[0]
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitedit(){
      const config = {
      headers: { "content-type": "multipart/form-data" }
    };
    let editlisting = this.listings

    let formData = new FormData()
    for(let data in editlisting){
      formData.append(data, editlisting[data])
    }
     try{
      let response = await this.$axios.$patch(`/server/listings/${editlisting.slug}/`, formData, config)
      this.$router.push('/')
    } catch(e){ console.log(e)}
    }
  }
}
</script>


<style>

</style>