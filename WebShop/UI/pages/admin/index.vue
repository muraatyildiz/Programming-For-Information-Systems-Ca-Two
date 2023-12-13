<template>
   <v-data-table :headers="headers" :items="users " sort-by="calories" class="elevation-1">
       <template v-slot:top>
           <v-toolbar flat>
               <v-toolbar-title>User List</v-toolbar-title>
               <v-divider class="mx-4" inset vertical></v-divider>
               <v-spacer></v-spacer>
           </v-toolbar>
       </template>
 
     
   </v-data-table>
</template>
 
<script>
export default {
  layout: "adminDefault",
  name: "adminPage",
  data() {
    return {
        users:[],
        headers: [
       {
         text: 'User id',
         align: 'start',
         sortable: false,
         value: 'id',
       },
       { text: 'Full Name', value: 'fullName' },
       { text: 'Phone Number', value: 'phoneNumber' },
       { text: 'Email', value: 'email' },
       { text: 'Role', value: 'role', sortable: false },
     ],
    }
  },
  created() {
    this.getUserList();
  },
  methods: {
    getUserList() {
      let link = "login/list";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          var answer = response.body;
          if (answer.count > 0) {
            this.users = answer.Results;
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