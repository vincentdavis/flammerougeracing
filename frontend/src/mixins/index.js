import { mapGetters , mapActions} from 'vuex'


export const Index = {
    computed: {
        ...mapGetters(["getters_races", "getters_race_loader", "profile", "getters_zwift_link_modal"]),
        zwift_link_modal_model:{
          set(value) {
            this.zwift_link_modal(value)
          },
          get() {
            return this.getters_zwift_link_modal
          },
        }
    },
    methods:{
        ...mapActions(['get_races', 'detail_races', 'get_profile', 'zwift_link_modal', 'link_zwifit', 'racesAPI', 'zwift_resultAPI',
        'API'
        ]),
        caculate_time(start_date){
            const timeNow = new Date().getTime();
      const timeDifference = new Date(start_date).getTime() - timeNow;
      const millisecondsInOneSecond = 1000;
      const millisecondsInOneMinute = millisecondsInOneSecond * 60;
      const millisecondsInOneHour = millisecondsInOneMinute * 60;
      const millisecondsInOneDay = millisecondsInOneHour * 24;
      const differenceInDays = timeDifference / millisecondsInOneDay;
      const remainderDifferenceInHours =
        (timeDifference % millisecondsInOneDay) / millisecondsInOneHour;
      const remainderDifferenceInMinutes =
        (timeDifference % millisecondsInOneHour) / millisecondsInOneMinute;
      const remainderDifferenceInSeconds =
        (timeDifference % millisecondsInOneMinute) / millisecondsInOneSecond;
      const remainingDays = Math.floor(differenceInDays);
      const remainingHours = Math.floor(remainderDifferenceInHours);
      const remainingMinutes = Math.floor(remainderDifferenceInMinutes);
      const remainingSeconds = Math.floor(remainderDifferenceInSeconds);
      return remainingDays +
        " Days " +
        remainingHours +
        " Hrs " +
        remainingMinutes +
        " Min " +
        remainingSeconds +
        " Sec";
        }
    }
}