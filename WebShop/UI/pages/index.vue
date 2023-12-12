<template>
  <div class="container text-center">
    <div
      class="row content row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3 p-2"
    >
      <div
        class="productCard col mb-3"
        v-for="product in products"
        :key="product.id"
      >
        <div>
          <nuxt-link :to="{ name: 'id', params: { id: product.id } }">
            <img
              :src="$store.state.ApiLink + 'file/serve-image/' + product.imgUrl"
              width="250"
              height="280"
            />
            <h5 class="productNameCard">{{ product.name }}</h5>

            <p class="productDescription">{{ product.description }}</p>

            <p class="productPrice">€ {{ product.price }},00</p>
          </nuxt-link>
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
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "IndexPage",
  data: () => ({
    products: [],
  }),
  created() {
    this.getProductList();
  },
  methods: {
    ...mapActions(["addProductToCart"]),
    getProductList() {
      let link = "product/list";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          var answer = response.body;
          if (answer.count > 0) {
            this.products = answer.Results;
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
};
</script>
<style>
</style>
