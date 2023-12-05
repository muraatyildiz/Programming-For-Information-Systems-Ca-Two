import Vue from "vue";

export const state = () => ({
	ApiLink2: process.env.NODE_ENV === "development" ? "http://10.69.174.136:8080/" : "/", 
	ApiLink:  process.env.NODE_ENV === "development" ? "http://192.168.0.63:8080/" : "/", 
	userInfo :null,
});

export const mutations = {
	setUserInfo(state, user) {
		if (user) {
			state.userInfo = user;
		}
		else {
			state.userInfo = null;
		}
	}
};
export const actions = {
	requestPost(vuexContext, send) {	
		send.link = vuexContext.state.ApiLink + send.link;
        console.log(send.data)
		return Vue.http.post(send.link,  send.data).catch((r) => {			
		});
	},
	requestGet(vuexContext, link) {
	   link = vuexContext.state.ApiLink + link;
		return Vue.http.get(link).catch((r) => {
					});
	},
    requestPut(vuexContext, send) {	
		send.link = vuexContext.state.ApiLink + send.link;
        console.log(send.data)
		return Vue.http.put(send.link, send.data).catch((r) => {			
		});
	},
	requestDelete(vuexContext, link) {
	   link = vuexContext.state.ApiLink + link;
       console.log(link);
		return Vue.http.delete(link).catch((r) => {
		});
	},
};

export const getters = {
	getUserInfo(state) {
		if (state.userInfo) {
			return state.userInfo;
		}
		return null;
	}
};