<template>
    <v-data-table :headers="headers" :items="list " sort-by="calories" class="elevation-1">
       <template v-slot:top>
           <v-toolbar flat>
               <v-toolbar-title>Order List</v-toolbar-title>
               <v-divider class="mx-4" inset vertical></v-divider>
               <v-spacer></v-spacer>
             
               <v-dialog v-model="dialogDelete" max-width="500px">
                   <v-card>
                       <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                       <v-card-actions>
                           <v-spacer></v-spacer>
                           <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                           <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                           <v-spacer></v-spacer>
                       </v-card-actions>
                   </v-card>
               </v-dialog>
           </v-toolbar>
       </template>
       <template v-slot:item.actions="{ item }">
           <v-icon small class="mr-2" @click="editItem(item)">
               mdi-pencil
           </v-icon>
           <v-icon small @click="deleteItem(item)">
               mdi-delete
           </v-icon>
       </template>
       <template v-slot:no-data>
           <v-btn color="primary" @click="initialize">
               Reset
           </v-btn>
       </template>
   </v-data-table>
</template>
<script>
export default {
   layout: "adminDefault",
   name: "orderListPage",
   data: () => ({
     dialog: false,
     dialogDelete: false,
     headers: [
       {
         text: 'Orders Number',
         align: 'start',
         sortable: false,
         value: 'orderNumber',
       },
       { text: 'Product Name', value: 'productName' },
       { text: 'Amount', value: 'amount' },
       { text: 'Delivery', value: 'delivery' },
       { text: 'Actions', value: 'actions', sortable: false },
     ],
     list: [],
     editedIndex: -1,
     editedItem: {
       name: '',
       calories: 0,
       fat: 0,
       carbs: 0,
       protein: 0,
     },
     defaultItem: {
       name: '',
       calories: 0,
       fat: 0,
       carbs: 0,
       protein: 0,
     },
   }),


   computed: {
     formTitle () {
       return this.editedIndex === -1 ? 'New Product' : 'Edit Product'
     },
   },


   watch: {
     dialog (val) {
       val || this.close()
     },
     dialogDelete (val) {
       val || this.closeDelete()
     },
   },


   created () {
     this.initialize()
   },
   methods: {
     initialize () {
       this.list = [
         {
           orderNumber: '1001',
           productName: 'Product Name1',
           amount: 540,
           delivery:"UnderProgress",
           description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ",
         
         },
         {
           orderNumber: '1002',
           productName:  'Product Name2',
           amount: 90,
           delivery:"UnderProgress",
           description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
          
         },
         {
           orderNumber: '1003',
           productName:  'Product Name3',
           amount: 160,
           delivery:"UnderProgress",
           description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
          
         },
         {
           orderNumber: '1004',
           productName:  'Product Name4',
           amount: 30,
           delivery:"UnderProgress",
           description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
       
         },
         {
           orderNumber: '1005',
           productName: 'Product Name5',
           amount: 160,
           delivery:"Done",
           description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
          
         },
         {
           orderNumber: '1006',
           productName:  'Product Name6',
           amount: 52,
           delivery:"Done",
           description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
         
         },
         {
           orderNumber: '1007',
           productName:  'Product Name7',
           amount: 20,
           delivery:"Done",
           description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
         
         },
         {
           orderNumber: '1008',
           productName: 'Product Name8',
           amount: 32,
           delivery:"Done",
           description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
          
         },
         {
           orderNumber: '1009',
           productName:  'Product Name9',
           amount: 250,
           delivery:"Done",
           description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
          
         },
         {
           orderNumber: '1010',
           productName:  'Product Name 10',
           amount: 260,
           delivery:"Done",
           description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
         
         },
       ]
     },


     editItem (item) {
       this.editedIndex = this.desserts.indexOf(item)
       this.editedItem = Object.assign({}, item)
       this.dialog = true
     },


     deleteItem (item) {
       this.editedIndex = this.desserts.indexOf(item)
       this.editedItem = Object.assign({}, item)
       this.dialogDelete = true
     },


     deleteItemConfirm () {
       this.desserts.splice(this.editedIndex, 1)
       this.closeDelete()
     },


     close () {
       this.dialog = false
       this.$nextTick(() => {
         this.editedItem = Object.assign({}, this.defaultItem)
         this.editedIndex = -1
       })
     },


     closeDelete () {
       this.dialogDelete = false
       this.$nextTick(() => {
         this.editedItem = Object.assign({}, this.defaultItem)
         this.editedIndex = -1
       })
     },


     save () {
       if (this.editedIndex > -1) {
         Object.assign(this.desserts[this.editedIndex], this.editedItem)
       } else {
         this.desserts.push(this.editedItem)
       }
       this.close()
     },
   },
};
</script>
<style></style>

