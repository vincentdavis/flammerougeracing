import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axiosIns from '@/plugins/axios.js'


export default new Vuex.Store({
  state: {
    profile: null,
    races: [],
    race_loader: false,

    zwift_link_modal: false
  },
  getters: {
    profile: (state) => state.profile,
    getters_zwift_link_modal: (state) => state.zwift_link_modal,
    getters_races: (state) => state.races,
    getters_race_loader: (state) => state.race_loader,

  },
  mutations: {
    mutation_profile(state, data) {
      state.profile = data
  },
    mutation_races(state, data) {
      state.races = data
  },
    mutation_race_loader(state, data) {
      state.race_loader = data
  },
  mutation_zwift_link_modal(state, data) {
      state.zwift_link_modal = data
  },
  },
  actions: {
    zwift_link_modal({commit}, status){
      commit('mutation_zwift_link_modal', status)
    },
    link_zwifit({commit}, payload){

      return new Promise((resolve, reject) => {
        commit
        axiosIns.post('/api/users/zwift_link/', payload)
        .then(data => {
          resolve(data)
        })
        .catch(err => {

          reject(err)
        })
      }) 
    },
    get_profile({commit}){
      commit('mutation_race_loader', true)

      return new Promise((resolve, reject) => {
        commit
        axiosIns.get('/api/users/me/')
        .then(data => {
          commit('mutation_profile', data.data)
          resolve(data)
        })
        .catch(err => {

          reject(err)
        })
      }) 
    },
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
