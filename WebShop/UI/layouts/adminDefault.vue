<template>
    <v-app dark>
      <v-navigation-drawer
        v-model="drawer"
        :mini-variant="miniVariant"
        :clipped="clipped"
        fixed
        app
      >
        <v-list>
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :to="item.to"
            router
            exact
          >
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar
        :clipped-left="clipped"
        fixed
        app
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
        <v-toolbar-title>{{ title }}</v-toolbar-title>
        <v-spacer />
        <v-btn
          icon
          @click="returnToWebShop"
        >
          Back
        </v-btn>
      </v-app-bar>
      <v-main>
        <v-container>
          <Nuxt />
        </v-container>
      </v-main>
     
      <v-footer
        :absolute="!fixed"
        app
      >
        <span>&copy; {{ new Date().getFullYear() }}</span>
      </v-footer>
    </v-app>
  </template>
 
  <script>
  export default {
   
    data () {
      return {
        clipped: false,
        drawer: false,
        fixed: false,
        items: [
          {
            icon: 'mdi-account',
            title: 'Users',
            to: '/admin'
          },
          {
            icon: 'mdi-truck',
            title: 'Orders',
            to: '/admin/orderList'
          },
          {
            icon: 'mdi-sprout',
            title: 'Products',
            to: '/admin/productList'
          },
          // {
          //   icon: 'mdi-chart-bubble',
          //   title: 'Offers',
          //   to: '/admin/offers'
          // },
          // {
          //   icon: 'mdi-chart-bubble',
          //   title: 'Reviews',
          //   to: '/admin/reviews'
          // }
        ],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'Admin Page'
      }
    },
    methods:{
      returnToWebShop(){
        this.$router.push("/")
      }
    }
  }
  </script>
 

