<template>
  <v-app id="inspire">
    <v-app-bar
      shrink-on-scroll
      prominent
      src="https://www.flammerougeracing.com/images/FRRHeader.jpg"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-4"
    >
      <v-spacer></v-spacer>

      <!-- <v-avatar
        class="hidden-sm-and-down"
        color="grey darken-1 shrink"
        size="32"
      ></v-avatar> -->
    </v-app-bar>

    <v-main class=" lighten-3 ml-2 mr-2">
      <v-row>
        <v-col cols="12" sm="2">
              <b>Race Schedule</b>

          <News></News>
        </v-col>

        <v-col cols="12" sm="8">
            <v-card>
              <div class="mt-2">
              <v-tabs v-model="tab" align-with-title>
              <v-tabs-slider color="yellow"></v-tabs-slider>

              <v-tab v-for="item in items" :key="item">
                {{ item }}
              </v-tab>
            </v-tabs>
            <v-tabs-items v-model="tab">
              <v-tab-item>
                <div class="ma-2">
                  <Listview
                    :options="{
                      store_action_name: 'API',
                      api: '/api/TTTLeagueStandings/',
                    }"
                  >
                  </Listview>
                </div>
              </v-tab-item>
              <v-tab-item>
                <div class="ma-2">
                  <Listview
                    :options="{
                      store_action_name: 'API',
                      api: '/api/Tttstageresrteam/',
                    }"
                  >
                  </Listview>
                </div>
              </v-tab-item>
              <v-tab-item>
                <div class="ma-2">
                  <Listview
                    :options="{
                      store_action_name: 'API',
                      api: '/api/Tttriderstats/',
                    }"
                  >
                  </Listview>
                </div>
              </v-tab-item>
              <v-tab-item>
                <div class="ma-2">
                  <Listview
                    :options="{
                      store_action_name: 'API',
                      api: '/api/Tttriderstats/',
                    }"
                  >
                  </Listview>
                </div>
              </v-tab-item>
              <v-tab-item>
                <div class="ma-2">
                  <Listview
                    :options="{
                      store_action_name: 'API',
                      api: '/api/Tttriderstats/',
                    }"
                  >
                  </Listview>
                </div>
              </v-tab-item>
              <v-tab-item>
                <div class="ma-2">
                  <Listview
                    :options="{
                      store_action_name: 'API',
                      api: '/api/Tttriderstats/',
                    }"
                  >
                  </Listview>
                </div>
              </v-tab-item>
              <v-tab-item>
                <div class="ma-2">
                  <Listview
                    :options="{
                      store_action_name: 'API',
                      api: '/api/Tttstagesegtsprint/',
                    }"
                  >
                  </Listview>
                </div>
              </v-tab-item>
            </v-tabs-items>
            </div>
            </v-card>
        </v-col>

        <v-col cols="12" sm="2">
          
   <div class="mt-2">
    <b>Next Event</b>
     <v-img
      src="@/assets/NextTour.png"
    ></v-img>
   </div>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import Listview from "@/components/DataTable/Listview.vue";
import News from "@/components/News.vue";

export default {
  components: {
    Listview,
    News,
  },
  data: () => ({
    links: ["Dashboard", "Messages", "Profile", "Updates"],
    tab: null,
    items: [
      "Team League",
      "Team Stage Result",
      "FRHC League",
      "Virtual Peloton FRCH Race Result",
      "General Calification",
      "DC Results",
      "Green Jersey",
      "Sprinter Results",
      "Palka Dot Jersey",
      "KOM Result",
    ],
  }),
};
</script>