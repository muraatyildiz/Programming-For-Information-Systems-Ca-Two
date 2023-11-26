import Vue from "vue";
import VueResource from "vue-resource";
Vue.use(VueResource);

Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'
Vue.http.headers.common['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
Vue.http.headers.common['Access-Control-Request-Method'] = 'GET, POST, PUT';
Vue.http.options.emulateJSON = true