<template>
  <div class="container text-center">
    <div class="row content">
      <div
        class="productCard col-md-3 mb-3 p-5"
        v-for="product in products"
        :key="product.id"
      >
        <div class="">
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
  watch: {
    "$route.query"() {
      if (this.$route.query.category && this.$route.query.category != "all") {
        this.getProductListByCategory(this.$route.query.category);
      }
      else if (this.$route.query.search && this.$route.query.search.length > 2) {
        this.getProductListBySearch(this.$route.query.search);
      } else {
        this.getProductList();
      }
    },
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
    getProductListByCategory(category) {
      let link = "product/getByCategory/" + category;
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
    getProductListBySearch(search) {
      let link = "product/getBySearch/" + search;
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
  },
};
</script>
<style>
</style>
