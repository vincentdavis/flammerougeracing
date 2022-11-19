import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axiosIns from '@/plugins/axios.js'


export default new Vuex.Store({
  state: {
    races: [],
    race_loader: false
  },
  getters: {
    getters_races: (state) => state.races,
    getters_race_loader: (state) => state.race_loader,

  },
  mutations: {
    mutation_races(state, data) {
      state.races = data
  },
    mutation_race_loader(state, data) {
      state.race_loader = data
  },
  },
  actions: {
    get_races({commit}){
      commit('mutation_race_loader', true)

      return new Promise((resolve, reject) => {
        commit
        axiosIns.get('/api/race/')
        .then(data => {
          commit('mutation_race_loader', false)
          commit('mutation_races', data.data)
          resolve(data)
        })
        .catch(err => {
          commit('mutation_race_loader', false)

          reject(err)
        })
      }) 
    },
    detail_races({commit}, query){
      commit('mutation_race_loader', true)

      return new Promise((resolve, reject) => {
        commit
        axiosIns.get('/api/race/'+query)
        .then(data => {
          commit('mutation_race_loader', false)
          resolve(data)
        })
        .catch(err => {
          commit('mutation_race_loader', false)

          reject(err)
        })
      }) 
    }
    },
  modules: {
  }
})
