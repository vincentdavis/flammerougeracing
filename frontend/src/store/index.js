import appConfigStoreModule from '@core/@app-config/appConfigStoreModule'
import Vue from 'vue'
import Vuex from 'vuex'
import app from './app'
import axiosIns from '@/plugins/axios'
import { status_color, exception_rest_api_handler, extract_api_data } from '@/helper'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    Drawer: {
      DrawerModel: false,
      DrawerShowAppBar: false,
      DrawerSize: '35%',
      DrawerFormType: '',
      DrawerForm: [],
      DrawerFormSubmit: {},
      DrawerLoader: true,
      DrawerFormAPICall: false,
      DrawerFormTitle: '',
      DrawerExtraParam: '',
    }, // Used to open drawer

    SecondDrawer: {
      DrawerModel: false,
      DrawerShowAppBar: false,
      DrawerSize: '35%',
      DrawerFormType: '',
      DrawerForm: [],
      DrawerFormSubmit: {},
      DrawerLoader: true,
      DrawerFormAPICall: false,
      DrawerExtraParam: ''
    }, // Used to open customer drawer
  },
  mutations: {
    mutation__drawer(state, value) {
      state.Drawer = Object.assign(state.Drawer, value)
    },
    utation__drawer(state, value) {
      state.Drawer = Object.assign(state.Drawer, value)
    },
  },
  getters: {
    Drawer: state => state.Drawer,
  },
  actions: {
    OpenDrawerOnClick({ commit }, value) {
      commit(value.DrawerMutation, {
        DrawerModel: true,
        DrawerShowAppBar: value.ShowAppBarOnDrawer,
        DrawerSize: value.DrawerSize,
        DrawerFormType: value.DrawerFormType,
        DrawerLoader: true,
        DrawerActionType: value.DrawerActionType,
        DrawerFormTitle: value.DrawerFormTitle,
        DrawerFormSubmit: value.DrawerFormSubmit,
        DrawerApiForm: value.DrawerApiForm,
        DrawerShowAction: value.DrawerShowAction,
      })

      if (value && value.DrawerFormAPICall) {
        commit(value.DrawerMutation, { DrawerLoader: true })
        return new Promise((resolve, reject) => {
          axiosIns.get('api/forms/get_form/?form_name=' + value.DrawerFormType+(value.DrawerExtraParam ? value.DrawerExtraParam : ''))
            .then(data => {
              commit(value.DrawerMutation, {
                DrawerForm: data.data,
                DrawerLoader: false
              })

              resolve(data)
            })
            .catch(err => {
              reject(err)
              commit(value.DrawerMutation, {
                DrawerForm: [],
                DrawerLoader: false
              })
            })
        })
      } else {
        commit(value.DrawerMutation, {
          DrawerModel: true,
          DrawerShowAppBar: value.ShowAppBarOnDrawer,
          DrawerSize: value.DrawerSize,
          DrawerFormType: value.DrawerFormType,
          DrawerLoader: false,
        })
      }
    },
    CloseDrawer({ commit }) {
      commit('mutation__drawer', { DrawerLoader: false ,DrawerModel: false , DrawerForm: []})
    },
    CREATE_EVENT({ commit }, payload) {
      var data = {}
      data =  extract_api_data(payload.data ? payload.data: [])
      return new Promise((resolve, reject) => {
        axiosIns.post('api/race_series/'+payload.custom_action+'/', data)
          .then(data => {
            commit('mutation__drawer', { DrawerLoader: false ,DrawerModel: false , DrawerForm: []})

            resolve(data)

          })
          .catch(err => {
            commit('mutation__drawer', { DrawerLoader: false ,DrawerModel: false , DrawerForm: []})


            reject(err)
          })
      })
    },
    LIST_EVENT({ commit }) {
      return new Promise((resolve, reject) => {
        axiosIns.get('api/race_series/')
          .then(data => {

            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    }

      

  },
  modules: {
    appConfig: appConfigStoreModule,
    app,
  },
})
