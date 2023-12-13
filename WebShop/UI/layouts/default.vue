<template>
  <v-app>
    <div class="row">
      <div class="col-12 banner">
        <img class="bannerImg" src="Christmas-Flowers-Banner-1.png" />
        <div class="bannerContent">
          <h4>
            <em>"Fresh flowers carefully designed by skilled florists"</em>
          </h4>
        </div>
      </div>
    </div>
    <div class="row topbar">
      <!-- Top Bar -->
      <div class="col-1 d-md-block d-lg-none mt-3">
        <!-- The menu button initially displays none and then appears on the mobile screen -->
        <h1>
          <i class="bi bi-list cartIcon" onclick="openNav()"> </i>
        </h1>
      </div>
      <div class="col-lg-2 col-9 text-center text-lg-start">
         <nuxt-link to="./" class="logo">  <a class="logo" href="./">
          <img src="new_logo_BA.png" />
        </a> </nuxt-link>
       
      </div>
      <div class="col-8 d-none d-lg-block mt-2">
        <!-- This menu is not dynamic, when clicked it goes to the home page. Display is none on mobile screen -->
        <div class="topnav">
          <nuxt-link :to="{ path: './', query: { category: 'all' }}"> Home </nuxt-link>
          <nuxt-link :to="{ path: './', query: { category: 'flowers' }}"> Flowers </nuxt-link>
          <nuxt-link :to="{ path: './', query: { category: 'christmas' }}"> Christmas </nuxt-link>
          <nuxt-link :to="{ path: './', query: { category: 'event' }}"> Events </nuxt-link>

          <input
            class="search"
            type="text"
            placeholder="Search.."
            v-model="search"
          />
        </div>
      </div>
      <div class="col-2 text-end mt-3">
        <h3>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      <i @click="openLoginForm" class="bi bi-person userIcon ml-2 pt-1">
            </i>
          <i @click="openCart" class="bi bi-cart cartIcon">
            <span class="btn-circle" v-if="hasProduct()">
              {{ getProductsInCart.length }}
            </span></i>
        </h3>
      </div>
    </div>
    <v-main>
        <Nuxt />
    </v-main>
    <footer class="footer">
      <a class="logoFooter" href="./">
        <img style="width: 100%; height: 100%" src="new_logo_BA.png" />
      </a>
    </footer>
    <v-dialog v-model="cartDialog" width="auto">
      <cart :key="cartKey" @closeForm="cartDialog = false" />
    </v-dialog>
    <v-dialog v-model="loginFormDialog" width="auto">
      <login-form :key="formKey" @closeForm="loginFormDialog = false" />
    </v-dialog>
  </v-app>
</template>

<script>
import cart from "~/components/cartDialog";
import loginForm from "~/components/loginForm";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "DefaultLayout",
  components: { cart,
    loginForm },
  data() {
    return {
      cartKey: "ky",
      formKey: "ky",
      cartDialog: false,
      loginFormDialog:false,
      search:""
    };
  }, 
  watch: {
    'search'() {
        if(this.search.length){
          this.$router.push({path: './', query: { search: this.search }})
        }
      
        
    }
  },
  methods: {
    ...mapActions(["setAuth"]),
    hasProduct() {
      return this.getProductsInCart.length > 0;
    },
    openCart() {
      this.cartKey = new Date().getTime();
      this.cartDialog = true;
    },
    openLoginForm(){    
      this.formKey = new Date().getTime();
      this.loginFormDialog = true;
    }
  
  },
  computed: {
    ...mapGetters(["getProductsInCart"]),
  },
  created(){
    let auth = false
    this.setAuth(auth);
    
  }
};
</script>
<style scoped>
.btn-circle {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  position: absolute;
  top: 12px;
  right: 4px;
  background-color: #19af9f;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: x-large;
  padding-right: 2px !important;
  font-family: sans-serif;
}
</style>
