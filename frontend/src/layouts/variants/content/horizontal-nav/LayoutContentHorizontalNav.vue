<template>
  <layout-content-horizontal-nav :nav-menu-items="navMenuItems">
    <!-- Default Slot -->
    <slot></slot>

    <!-- Navbar -->
    <template #navbar>
      <div class="navbar-content-container" :class="{ 'expanded-search': shallShowFullSearch }">
        <!-- Left Content: Search -->
        <div class="d-flex align-center">
          <v-app-bar-nav-icon v-if="$vuetify.breakpoint.mdAndDown"></v-app-bar-nav-icon>
          <router-link to="/" class="d-flex align-center text-decoration-none">
            <v-card elevation="0">
              <v-img :src="appLogo" max-height="60px" max-width="300px" alt="logo" contain> </v-img>
            </v-card>
          </router-link>
        </div>

        <!-- Right Content: I18n, Light/Dark, Notification & User Dropdown -->
        <div class="d-flex align-center">
          <app-bar-search
            :shall-show-full-search.sync="shallShowFullSearch"
            :data="appBarSearchData"
            :filter="searchFilterFunc"
            :search-query.sync="appBarSearchQuery"
            class="me-4"
          ></app-bar-search>
          <app-bar-theme-switcher></app-bar-theme-switcher>
          <app-bar-user-menu class="ms-2"></app-bar-user-menu>
        </div>
      </div>
      <v-overlay
        :value="$store.state.app.shallContentShowOverlay"
        z-index="5"
        absolute
        class="system-bar-overlay"
      ></v-overlay>
    </template>

    <!-- Slot: footer -->
    <template #footer>
      <div class="d-flex justify-space-between">
        <span>COPYRIGHT &copy; {{ new Date().getFullYear() }} Flamme Rouge Racing, All rights Reserved - <a class="text-caption" href="https://flammerougeracing.com/files/Policy/FRRPrivacyPolicy.pdf">Privacy Policy</a> - <a class="text-caption" href="https://flammerougeracing.com/files/Policy/FRRTermsandConditions.pdf">Terms and Conditions</a> </span>
        <div class="d-flex align-center">
          <span>Contact us</span>
           <a href="mailto:rcontrol@flammerougeracing.com" class="text-decoration-none"
          ><v-icon small color="error" class="ml-5">{{icons.mdiEmail}}</v-icon></a
        >
        <a
          target="__blank__"
          href="https://www.facebook.com/groups/141237451557465/"
          class="text-decoration-none"
          ><v-icon small color="error" class="ml-5">{{icons.mdiFacebook}}</v-icon></a
        >
        <a
          target="__blank__"
          href="https://twitter.com/Richard59427760"
          class="text-decoration-none"
          ><v-icon small color="error" class="ml-5">{{icons.mdiTwitter}}</v-icon></a
        >
        <a
          target="__blank__"
          href="https://flammerougeracing.com/"
          class="text-decoration-none"
          ><v-icon small color="error" class="ml-5">{{icons.mdiInstagram}}</v-icon></a
        >
        </div>
      </div>
    </template>

    <!-- App Content -->
    <template #v-app-content>
      <app-customizer class="d-none d-md-block"></app-customizer>
      <app-base-drawer />
      
    </template>
  </layout-content-horizontal-nav>
</template>

<script>
import LayoutContentHorizontalNav from '@core/layouts/variants/content/horizontal-nav/LayoutContentHorizontalNav.vue'
import AppCustomizer from '@core/layouts/components/app-customizer/AppCustomizer.vue'
import navMenuItems from '@/navigation/horizontal'

// App Bar Components
import AppBarSearch from '@core/layouts/components/app-bar/AppBarSearch.vue'
import AppBarThemeSwitcher from '@core/layouts/components/app-bar/AppBarThemeSwitcher.vue'
import AppBarUserMenu from '@/components/AppBarUserMenu.vue'

// Search Data
import appBarSearchData from '@/assets/app-bar-search-data'
import AppBaseDrawer from '@/components/Drawer/AppBaseDrawer.vue'

import { ref, watch } from '@vue/composition-api'

import themeConfig from '@themeConfig'
import { mdiHeartOutline, mdiFacebook , mdiEmail, mdiTwitter, mdiInstagram} from '@mdi/js'

export default {
  components: {
    LayoutContentHorizontalNav,
    AppCustomizer,

    // App Bar Components
    AppBarSearch,
    AppBarThemeSwitcher,
    AppBarUserMenu,
    AppBaseDrawer
  },
  setup() {
    // Search
    const appBarSearchQuery = ref('')
    const shallShowFullSearch = ref(false)
    const maxItemsInGroup = 5
    const totalItemsInGroup = ref({
      pages: 0,
      files: 0,
      contacts: 0,
    })
    watch(appBarSearchQuery, () => {
      totalItemsInGroup.value = {
        pages: 0,
        files: 0,
        contacts: 0,
      }
    })

    const searchFilterFunc = (item, queryText, itemText) => {
      if (item.header || item.divider) return true

      const itemGroup = (() => {
        if (item.to !== undefined) return 'pages'
        if (item.size !== undefined) return 'files'
        if (item.email !== undefined) return 'contacts'

        return null
      })()

      const isMatched = itemText.toLocaleLowerCase().indexOf(queryText.toLocaleLowerCase()) > -1

      if (isMatched) {
        if (itemGroup === 'pages') totalItemsInGroup.value.pages += 1
        else if (itemGroup === 'files') totalItemsInGroup.value.files += 1
        else if (itemGroup === 'contacts') totalItemsInGroup.value.contacts += 1
      }

      return appBarSearchQuery.value && isMatched && totalItemsInGroup.value[itemGroup] <= maxItemsInGroup
    }

    return {
      navMenuItems,

      // Search
      appBarSearchQuery,
      shallShowFullSearch,
      appBarSearchData,
      searchFilterFunc,

      // App Config
      appName: themeConfig.app.name,
      appLogo: themeConfig.app.logo,

      // Icons
      icons: {
        mdiHeartOutline,
        mdiFacebook,
        mdiEmail,
        mdiTwitter,
        mdiInstagram
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.app-title {
  font-size: 1.25rem;
  font-weight: 600;
}

.navbar-content-container {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-grow: 1;
  position: relative;
}
</style>
