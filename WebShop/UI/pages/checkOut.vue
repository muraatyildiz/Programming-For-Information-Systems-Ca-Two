<template>
  <div class="container">
    <div class="row">
      <div class="checkout-box">
        <ul class="checkout-list">
          <transition-group name="fade">
            <li
              v-for="(product, index) in getProductsInCart"
              :key="index"
              class="checkout-product"
            >
              <img
                :src="
                  $store.state.ApiLink + 'file/serve-image/' + product.imgUrl
                "
                alt=""
                class="product-image"
              />
              <h3 class="product-name">{{ product.name }}</h3>
              <span class="product-name">x{{ product.quantity }}</span>
              <span class="product-price"
                >€ {{ product.price * product.quantity }},00
              </span>
              <button class="product-remove" @click="remove(index)">X</button>
            </li>
          </transition-group>
        </ul>
        <div v-if="!hasProduct()" class="checkout-message">
          <h3>No products...</h3>
          <router-link to="./">Back to list of products</router-link>
        </div>
        <h3 class="total" v-if="hasProduct()">
          Total: € {{ totalPrice() }}, 00
        </h3>
      </div>
      <div class="col-lg-6 mb-2 checkOutForm" v-if="hasProduct()">
        <h3>Customer Informations</h3>
        <label for="fname">Full Name</label>
        <input
          v-model="order.customerFullName"
          type="text"
          id="fname"
          name="firstname"
        />
        <label for="email">Email</label>
        <input
          v-model="order.customerEmail"
          type="text"
          id="email"
          name="email"
        />
        <label for="pNumber"> Phone Number</label>
        <input
          v-model="order.customerPhoneNumber"
          type="text"
          id="pNumber"
          name="phoneNumber"
        />
        <div class="col-50">
          <h3>Payment</h3>
          <label for="fname">Accepted Cards</label>
          <div class="icon-container">
            <i class="fa fa-cc-visa" style="color: navy"></i>
            <i class="fa fa-cc-amex" style="color: blue"></i>
            <i class="fa fa-cc-mastercard" style="color: red"></i>
            <i class="fa fa-cc-discover" style="color: orange"></i>
          </div>
          <label for="cname">Name on Card</label>
          <input
            v-model="defaultPayment.name"
            type="text"
            id="cname"
            name="cardname"
          />
          <label for="ccnum">Credit card number</label>
          <input
            v-model="defaultPayment.number"
            type="text"
            id="ccnum"
            name="cardnumber"
          />
          <label for="expmonth">Exp Month</label>
          <input
            v-model="defaultPayment.month"
            type="text"
            id="expmonth"
            name="expmonth"
          />

          <div class="row">
            <div class="col-50">
              <label for="expyear">Exp Year</label>
              <input
                v-model="defaultPayment.year"
                type="text"
                id="expyear"
                name="expyear"
              />
            </div>
            <div class="col-50">
              <label for="cvv">CVV</label>
              <input
                v-model="defaultPayment.cvv"
                type="text"
                id="cvv"
                name="cvv"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-6 mb-2 checkOutForm" v-if="hasProduct()">
        <h3>Shipping Informations</h3>
        <label for="fname">Name for Shipping</label>
        <input
          v-model="order.shippingName"
          type="text"
          id="fname"
          name="firstname"
        />
        <label for="email">Address for Shipping </label>
        <input
          v-model="order.shippingAddress"
          type="text"
          id="address"
          name="address"
        />
        <label for="pNumber"> Phone Number for Shipping</label>
        <input
          v-model="order.shippingPhoneNumber"
          type="text"
          id="pNumber"
          name="phoneNumber"
        />
        <label for="dDate"> Date for Shipping</label>
        <input
          v-model="order.shippingDate"
          type="date"
          id="dDate"
          name="dDate"
        />
        <label for="subject">Card Message</label>
        <textarea
          v-model="order.shippingCardMessage"
          id="subject"
          name="subject"
          placeholder="Write a delivery message for your order.."
          style="height: 200px"
        ></textarea>
        <button class="checkOutButton" @click="addOrder">Complete Order</button>
      </div>
    </div>
  </div>
</template>
  
  <script>
import { mapGetters, mapActions } from "vuex";

export default {
  layout: "productDetailLayout",
  data() {
    return {
      order: {
        customerFullName: "Murat Yildiz",
        customerEmail: "murat@dbs.ie",
        customerPhoneNumber: "0588556256",
        paymentDone: false,
        shippingName: "Paul Laird",
        shippingAddress: "13/14 Aungier Street Dublin 2, D02 WC04,  Ireland.",
        shippingPhoneNumber: "084085261996",
        shippingDate: "2023-12-24",
        shippingCardMessage: "Hope you have a good Christmas with your family. Happy christmas. Irene, Jeevitha and Murat",
        orderDate: new Date().toISOString().slice(0, 10),
        totalPrice: "",
        products: [],
      },
      defaultPayment: {
        name: "MURAT YILDIZ",
        number: "3434 4565 3454 9864",
        month: "09",
        year: "2026",
        cvv: "899",
      },
    };
  },
  computed: {
    ...mapGetters(["getProductsInCart"]),
  },

  methods: {
    ...mapActions(["removeProduct", "removeProductFromCart"]),
    hasProduct() {
      return this.getProductsInCart.length > 0;
    },
    totalPrice() {
      return this.getProductsInCart.reduce(
        (current, next) => current + next.price * next.quantity,
        0
      );
    },
    remove(index) {
      this.removeProductFromCart(index);
    },
    addOrder() {
      this.order.products = this.getProductsInCart;
      this.order.totalPrice = this.getProductsInCart.reduce(
        (current, next) => current + next.price * next.quantity,
        0
      );
      let order = JSON.parse(JSON.stringify(this.order));
      let link = "order/add";
      let send = { link, data: order };
      this.$store.dispatch("requestPost", send).then((response) => {
        var answer = response.body;
        if (answer.Result == "Success") {
          this.$router.push("./");
          alert("Order created successfully")
        } else {
        }
      });
    },
  },
};
</script>
  
  <style >
.checkout-box {
  width: 100%;
  max-width: 900px;
  display: flex;
  flex-direction: column;
  margin: 50px auto;
  box-sizing: border-box;
  padding: 1em;
}

.checkout-list {
  padding: 0;
}

.checkout-product {
  display: grid;
  grid-template-columns: 2fr 2fr 2fr 2fr 0.5fr;
  background-color: #fff;
  box-shadow: 0px 0px 10px rgba(73, 74, 78, 0.1);
  border-radius: 5px;
  list-style: none;
  box-sizing: border-box;
  padding: 0.8em;
  margin: 1em 0;
}

.checkout-product * {
  place-self: center;
}
.product-image {
  grid-column: 1/2;
  width: 50%;
}

.product-name {
  box-sizing: border-box;
}

.product-price {
  font-size: 1.2em;
  font-weight: bold;
}

.product-remove {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  border: 0;
  background-color: #e0e0e0;
  color: #fff;
  cursor: pointer;
}

.total {
  font-size: 2em;
  font-weight: bold;
  align-self: flex-end;
}

.checkout-message {
  font-size: 1.5em;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s;
}

.fade-enter,
.fade-leave-to {
  transform: translateX(-40px);
  opacity: 0;
}

.checkOutForm {
  background-color: #fff;
  padding: 10px 20px 0px 20px;
  border: none;
}

.checkOutForm input[type="text"],
input[type="date"],
textarea {
  width: 100%;
  margin-bottom: 20px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.checkOutForm label {
  margin-bottom: 10px;
  display: block;
}
.icon-container {
  margin-bottom: 20px;
  padding: 7px 0;
  font-size: 24px;
}

.checkOutButton {
  background-color: #19af9f;
  color: white;
  padding: 12px;
  margin: 10px 0;
  border: none;
  width: 100%;
  border-radius: 3px;
  cursor: pointer;
  font-size: 17px;
}

.checkOutButton:hover {
  opacity: 0.7;
}
</style>