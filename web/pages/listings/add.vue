<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ listings.name }}</h2>
      </div>
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
          src="@/static/placeholder.png">
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitListings">
          <div class="form-group">
            <label for>Name</label>
            <input type="text" class="form-control" v-model="listings.name">
          </div>
          <div class="form-group">
            <label for>Price</label>
            <input type="numer" class="form-control" v-model="listings.price">
          </div>
          <div class="form-group">
            <label for>Image</label>
            <input type="file" name="image" @change="onFileChange">
          </div>
          <div class="form-group">
            <label for>Description</label>
            <textarea v-model="listings.description" class="form-control" rows="8"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </main>
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
        error: null
      },
      preview: ""
    };
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
    async submitListings() {

      this.error = null

      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.listings) {
        formData.append(data, this.listings[data]);
      }
      try {
        let response = await this.$axios.$post("/server/listings/", formData, config);
        this.$router.push("/listings/");
      } catch (e)  {
        this.error = e.response.data
      }
    }
  }
};
</script>


<style scoped>
</style>