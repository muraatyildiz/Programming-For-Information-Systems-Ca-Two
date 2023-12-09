<template>
  <div class="container">
    <div class="row detailContent">
      <div class="col-lg-6 detailProduct">
        <img
          
          :src="$store.state.ApiLink + 'file/serve-image/' + product.imgUrl"
        />
      </div>
      <div class="col-lg-6 m-auto">
        <nav class="productNav">
          <nuxt-link to="./">
            Home
          </nuxt-link><span class="divider">/ </span>
          <nuxt-link to="./">
            Events
</nuxt-link>
    
        </nav>
        <h1>{{ product.name }}</h1>
        <div class="mt-5">
          <span class="heading">User Rating&nbsp;&nbsp;&nbsp;</span>
          userRatingStars
          <p>
            selectedProduct.rating ' average based on selectedProduct.reviews +
            ' reviews.
          </p>
          <hr style="border: 3px solid #f1f1f1" />
        </div>
        <div class="mb-5 detailPrice">Price: &nbsp;€ {{ product.price }}, 00</div>
        <p>
          <button
            id="myBtn"
            class="reservationButton"
            @click="addToCart(product)"
          >
            Add to Cart
          </button>
        </p>
      </div>
    </div>

    <div class="row">
      <div class="col-12"><h3>Description</h3></div>
      <div class="col-lg-6">
        <span> {{ product.description }}</span>
      </div>
      <div class="col-lg-6 mt-4">
        <h5><strong>Features:</strong></h5>
        <ul>
          <li>Available in weights 1-70kg</li>
          <li>Reliable</li>
          <li>Comfortable hold</li>
          <li>Chrome handle with knurling</li>
          <li>Reduced impact and noise</li>
          <li>Variety of exercises</li>
          <li>Anti-roll design</li>
          <li>Suitable for home and commercial gyms</li>
          <li>Single arm rows</li>
        </ul>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import { mapActions } from "vuex";
export default {
  layout: "productDetailLayout",
  name: "productDetailPage",
  data: () => ({
    product: {},
  }),
  methods: {
    ...mapActions(["addProductToCart"]),
    getProduct() {
      let id = this.$route.params.id;
      this.loading = true;
      let link = "product/list";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          var answer = response.body;
          if (answer.count > 0) {
            this.product = answer.Results.find((product) => product.id == id);
          }
        })
        .catch((x) => {
          console.log("Error");
        });
    },
    addToCart(product) {
      this.addProductToCart(product);
    },
  },
  created() {
    if (process.client) {
      this.getProduct();
    }
  },
};
</script>
  
  <style>
  .detailProduct {
   
   margin-top: -50px;
}
.detailProduct img {
   width: 90% !important;
   height: 90% !important;
}
.productNav a{
    color: #61b0e0;
    text-decoration: none;
}
</style>