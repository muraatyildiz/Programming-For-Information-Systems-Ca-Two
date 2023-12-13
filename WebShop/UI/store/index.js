import Vue from "vue";
import Cookie from "js-cookie";

export const state = () => ({
	ApiLink2: process.env.NODE_ENV === "development" ? "http://10.69.174.136:8080/" : "/",
	ApiLink: process.env.NODE_ENV === "development" ? "http://192.168.0.63:8080/" : "/",
	auth:false,
	userInfo: {},
	cartProducts: []
});

export const mutations = {
	setUserInfo(state, user) {	
		if (user) {
			state.userInfo = user;
			state.auth=true;				
		}
		else {
			state.userInfo = null;
		}
	},
	setAuth(state, auth){
        state.auth =auth
	},
	addProductToCart(state, product) {
		if (state.cartProducts.includes(product)) {
			product.quantity = state.cartProducts[state.cartProducts.indexOf(product)].quantity + 1
			state.cartProducts[state.cartProducts.indexOf(product)]=product
		} else {
			product.quantity = 1
			state.cartProducts.push(product);
		}
	},
	removeProductFromCart(state, index) {
		state.cartProducts.splice(index, 1)
	}
};
export const actions = {
	requestPost(vuexContext, send) {
		send.link = vuexContext.state.ApiLink + send.link;
	
		return Vue.http.post(send.link, send.data).catch((r) => {
		});
	},
	requestGet(vuexContext, link) {
		link = vuexContext.state.ApiLink + link;
		return Vue.http.get(link).catch((r) => {
		});
	},
	requestPut(vuexContext, send) {
		send.link = vuexContext.state.ApiLink + send.link;
		
		return Vue.http.put(send.link, send.data).catch((r) => {
		});
	},
	requestDelete(vuexContext, link) {
		link = vuexContext.state.ApiLink + link;
	
		return Vue.http.delete(link).catch((r) => {
		});
	},
	setUserInfo(vuexContext,user){
        vuexContext.commit("setUserInfo", user)
		Cookie.set("authKey", true);
	},
	setAuth(vuexContext,auth){
		let cookieAuth=Cookie.get("authKey");
		console.log(cookieAuth)
		if(cookieAuth){
			vuexContext.commit("setAuth", cookieAuth)
		}else{
			vuexContext.commit("setAuth", auth)
		}
		
	},
	logout(vuexContext){
		vuexContext.commit("setAuth", false)
		Cookie.set("authKey", false);
	},
	addProductToCart(vuexContext, product) {
		vuexContext.commit("addProductToCart", product)
	},
	removeProductFromCart(vuexContext, index) {
		vuexContext.commit("removeProductFromCart", index)
	}
};

export const getters = {
	getUserInfo(state) {
		if (state.userInfo) {
			return state.userInfo;
		}
		return null;
	},
	isAuthenticated(state) {		
		return state.auth;
	},
	getProductsInCart(state) {
		return state.cartProducts;
	}
};