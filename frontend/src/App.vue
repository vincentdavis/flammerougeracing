<template>
  <div>
    <v-app v-if="dialog">
      <div class="text-center">
        <v-dialog transition="scale-transition"  v-model="dialog" hide-overlay persistent width="300">
          <v-card elevation="0" :loading="true">
            <v-img src="@/assets/images/FRR.png"></v-img>
            <!-- <v-card-text>
              <div class="text-center mt-2">
                <v-progress-linear rounded height="5" indeterminate></v-progress-linear>
              </div>
            </v-card-text> -->
          </v-card>
        </v-dialog>
      </div>
    </v-app>

    <component v-else :is="resolveLayoutVariant" :class="`skin-variant--${appSkinVariant}`">
      <transition :name="appRouteTransition" mode="out-in" appear>
        <router-view></router-view>
      </transition>
    </component>
  </div>
</template>

<script>
// eslint-disable-next-line object-curly-newline
import { computed } from '@vue/composition-api'
// eslint-disable-next-line import/no-unresolved
import useAppConfig from '@core/@app-config/useAppConfig'
import { useRouter } from '@core/utils'
import { useLayout } from '@core/layouts/composable/useLayout'

// Layouts
import LayoutContentVerticalNav from '@/layouts/variants/content/vertical-nav/LayoutContentVerticalNav.vue'
import LayoutContentHorizontalNav from '@/layouts/variants/content/horizontal-nav/LayoutContentHorizontalNav.vue'
import LayoutBlank from '@/layouts/variants/blank/LayoutBlank.vue'

// Dynamic vh
import useDynamicVh from '@core/utils/useDynamicVh'

export default {
  components: {
    LayoutContentVerticalNav,
    LayoutContentHorizontalNav,
    LayoutBlank,
  },

  data() {
    return {
      dialog: true,
    }
  },
  mounted() {
    setTimeout(() => {
      this.dialog = false
      this.$router.push({ name: 'home' })
    }, 1000)
  },
  setup() {
    const { route } = useRouter()
    const { appContentLayoutNav, appSkinVariant, appRouteTransition } = useAppConfig()

    const { handleBreakpointLayoutSwitch } = useLayout()
    handleBreakpointLayoutSwitch()

    const resolveLayoutVariant = computed(() => {
      if (route.value.meta.layout === 'blank') return 'layout-blank'
      if (route.value.meta.layout === 'content') return `layout-content-${appContentLayoutNav.value}-nav`

      return 'layout-blank'
    })

    useDynamicVh()

    return {
      resolveLayoutVariant,
      appSkinVariant,
      appRouteTransition,
    }
  },
}
</script>
