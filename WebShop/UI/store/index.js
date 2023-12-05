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
