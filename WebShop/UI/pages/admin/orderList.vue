<template>
  <v-data-table :headers="headers" :items="orders " sort-by="calories" class="elevation-1">
     <template v-slot:top>
         <v-toolbar flat>
             <v-toolbar-title>Order List</v-toolbar-title>
             <v-divider class="mx-4" inset vertical></v-divider>
             <v-spacer></v-spacer>
         </v-toolbar>
     </template>
 </v-data-table>
</template>
<script>
export default {
 layout: "adminDefault",
 name: "orderListPage",
 data: () => ({
   headers: [
     {
       text: 'Customer Name ',
       align: 'start',
       sortable: false,
       value: 'customerFullName',
     },
     { text: 'Product Name', value: 'productName' },
     { text: 'Ordder Number', value: 'orderNumber' },
     { text: 'Order Date', value: 'orderDate' },
     { text: 'Shipping Date', value: 'shippingDate', sortable: false },
     { text: 'Shipping Address', value: 'shippingAddress', sortable: false },
   ],
   orders: [],
   
 }),


 computed: {
  
 },


 watch: {
 
 },


 created() {
  this.getOrderList();
},
methods: {
  getOrderList() {
    let link = "order/list";
    this.$store
      .dispatch("requestGet", link)
      .then((response) => {
        var answer = response.body;
        if (answer.count > 0) {
          this.orders = answer.Results;
          console.log(this.orders)
        }
      })
      .catch((x) => {
        console.log("Error");
      });
  },
}

};
</script>
<style></style>

