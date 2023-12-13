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
          <stars :rate="95" :totalReviews="345"/>
          <hr style="border: 3px solid #f1f1f1" />
        </div>
        <div class="mb-5 detailPrice">Price: &nbsp;€ {{ product.price }}.00</div>
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
          <li>All varieties of Roses are edible!</li>
          <li>Red roses – love and passion</li>
          <li>White roses - innocence and spirituality</li>
          <li>Yellow roses – warmth, friendship, and joy</li>
          <li>Pink roses – gratitude, elegance, and sweetness</li>
          <li>Orange roses – pride, energy, and intense desire</li>
          <li>Blue roses – secret love, mystery, and uniqueness</li>
          <li>Lavender roses – love at first sight, wonder, and enchantment</li>
          <li>Black roses – end of a relationship, change, and courage</li>
        </ul>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import { mapActions } from "vuex";
  import stars from "~/components/ratingStars";
export default {
  layout: "productDetailLayout",
  name: "productDetailPage",
  components: {
    stars,
  },
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