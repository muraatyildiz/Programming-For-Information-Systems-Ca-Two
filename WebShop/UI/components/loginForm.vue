<template>
  <div>
    <div class="container form" v-if="!isAuthenticated">
      <label for="uname"><b>Username</b></label>
      <input type="text" placeholder="Enter Username" v-model="user.userName" name="uname" required />

      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" v-model="user.password" name="psw" required />

      <button type="submit" @click="login">Login</button>
      <label>
        <input type="checkbox" checked="checked" name="remember" /> Remember me
      </label>
    </div>
    <div v-if="isAuthenticated" class="adminLink">
      <div style="margin: auto;">
        <h3>Admin</h3>
        <router-link to="./Admin">Go to admin Page</router-link>
      </div>
      <!-- <div style="margin: auto;">
        <i @click="logout">Logout</i>
      </div> -->
    </div>
  </div>
</template>
  <script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "loginForm",
  components: {},
  data() {
    return {
      isLogin: false,
      user:{
        userName:"",
        password:""
      }
    };
  },
  methods: {
    ...mapActions(["setUserInfo","logout"]),
  
    login() {      
      let user = JSON.parse(JSON.stringify(this.user));
      let link = "login/check";
      let send = { link, data: user };
      this.$store.dispatch("requestPost", send).then((response) => {
       var answer = response.body;
       if(answer.Result== 'error'){
        alert("User Name or Password is wrong")
       }else
       this.isLogin = true;
       this.setUserInfo(answer.Results)
      });
      
    },
    logout(){
        this.logout()
    }

    //   closeDialog() {
    //     this.$emit("closeForm");
    //     this.$router.push("/checkOut")
    //   },
  },
  computed: {
      ...mapGetters(["isAuthenticated"]),
  },
  created(){
   console.log( "this.isAuthenticated", this.isAuthenticated)  
}
};
</script>
  <style scoped>
.adminLink{
    background-color: white;
    width: 400px;
  height: 300px;
  text-align: center;
  
}
.form {
  width: 400px;
  height: auto;
  background-color: white;
}
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #04aa6d;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
    display: block;
    float: none;
  }
  .cancelbtn {
    width: 100%;
  }
}
</style>