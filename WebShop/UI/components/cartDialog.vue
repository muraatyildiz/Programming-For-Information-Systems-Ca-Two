<template>
  <div class="box">
    <span v-if="!hasProduct()">No products</span>
    <div
      v-for="(product, index) in getProductsInCart"
      :key="index"
      class="box-item"
    >
      <img :src="$store.state.ApiLink + 'file/serve-image/'+product.imgUrl" :alt="product.imgUrl" class="item-thumb" />
      <h3 class="item-name">{{ product.name }}</h3>
      <span class="item-amount">Amount: {{ product.quantity }}</span>
      <span class="item-price">€ {{ product.price }}, 00</span>
    </div>
    <div class="cart-info" v-if="hasProduct()">
      <span>Total: € {{ totalPrice() }}, 00</span>
      <!-- <router-link to="/checkout"> -->
      <v-btn btnColor="btn btn-small btn-info" @click.native="closeDialog()">
        Check Out
      </v-btn>
      <!-- </router-link> -->
    </div>
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "cartDialog",
  components: {},
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    //   ...mapActions([
    //   'showOrHiddenPopupCart',
    // ]),
    hasProduct() {
      return this.getProductsInCart.length > 0;
    },
    totalPrice() {
      return this.getProductsInCart.reduce(
        (current, next) => current + (next.price*next.quantity),
        0
      );
    },
    // showPopupCart() {
    //   this.showOrHiddenPopupCart();
    // },
    closeDialog() {
      this.$emit("closeForm");
      this.$router.push("/checkOut")
    },
  },
  computed: {
    ...mapGetters(["getProductsInCart"]),
  },
};
</script>
<style scoped>
.box {
  width: 600px;
  height: auto;
  background-color: #fafafa;
  box-shadow: 0px 0px 10px rgba(73, 74, 78, 0.1);
  border-radius: 5px;
  box-sizing: border-box;
  padding: 1em 0.5em;

}

.box:after {
  content: "";
  width: 30px;
  height: 30px;
  transform: rotate(45deg);
  background: inherit;
}

.box-item {
  width: 100%;
  height: 130px;
  background-color: #fff;
  box-sizing: border-box;
  border-radius: 3px;
  padding: 0 0.5em;
  margin-top: 0.3em;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
}

.item-thumb {
  max-width: 70%;
  grid-column: 1/2;
  grid-row: 1/4;
  align-self: center;
}

.item-name {
  grid-column: 2/4;
  grid-row: 1/2;
  font-weight: normal;
}

.item-amount {
  grid-column: 2/3;
  grid-row: 2/4;
  color: #ddd;
}

.cart-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>