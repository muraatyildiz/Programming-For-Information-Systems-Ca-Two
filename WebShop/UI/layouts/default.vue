<template>
  <v-app> 
    <div class="row">
      <div class="col-12 banner">
        <img
          class="bannerImg"
          src="Christmas-Flowers-Banner-1.png"
        />
        <div class="bannerContent">
          <h4><em>"Fresh flowers carefully designed by skilled florists"</em></h4>
        </div>
      </div>
    </div>
    <div class="row topbar">
      <!-- Top Bar -->
      <div class="col-1 d-md-block d-lg-none mt-3">
        <!-- The menu button initially displays none and then appears on the mobile screen -->
        <h1>
          <i class="bi bi-list cartIcon" onclick="openNav()"></i>
        </h1>
      </div>
      <div class="col-lg-2 col-9 text-center text-lg-start">
        <a class="logo" href="./">
          <img
          src="new_logo_BA.png"
        />
        </a>
      </div>
      <div class="col-8 d-none d-lg-block mt-2">
        <!-- This menu is not dynamic, when clicked it goes to the home page. Display is none on mobile screen -->
        <div class="topnav">
          <a href="./">Home</a>
          <a href="./">Flowers</a>
          <a href="./">Chrismas</a>
          <a href="./">Events</a>
          <input
            class="search"
            type="text"
            placeholder="Search.."
            onkeyup="productSearch()"
          />
        </div>
      </div>
      <div class="col-2 text-end mt-3">
        <h3>
          <i onclick="openModal(0)" class="bi bi-cart cartIcon"></i>
        </h3>
      </div>
    </div>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <footer class="footer">
        <a class="logoFooter" href="./">
          <img style=" width:100%;
            height:100%;"
          src="new_logo_BA.png"
        />
         
        </a>
      </footer>   
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      
    }
  }
}
</script>
