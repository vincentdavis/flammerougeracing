import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axiosIns from '@/plugins/axios.js'


export default new Vuex.Store({
  state: {
    races: []
  },
  getters: {
    getters_races: (state) => state.races,

  },
  mutations: {
    mutation_races(state, data) {
      state.races = data
  },
  },
  actions: {
    get_races({commit}, payload){
      return new Promise((resolve, reject) => {
        commit
        axiosIns.get('/api/races/', payload)
        .then(data => {
          commit('mutation_races', data.data)
          resolve(data)
        })
        .catch(err => {
          reject(err)
        })
      }) 
    }
    },
  modules: {
  }
})
