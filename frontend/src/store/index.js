import Vue from 'vue'
import Vuex from 'vuex'
import Axios from '@/plugins/axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    API({ commit }, payload) {
      return new Promise((resolve, reject) => {
        Axios.get(payload.api + payload.query_params)
          .then(data => {
            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
  },
  modules: {
  }
})
