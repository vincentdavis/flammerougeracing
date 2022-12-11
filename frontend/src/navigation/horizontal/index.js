import { mdiFileOutline, mdiHomeOutline } from '@mdi/js'

export default [
  {
    title: 'Home',
    icon: mdiHomeOutline,
    to: 'home',
  },
  {
    title: 'Tour',
    icon: '',
    to: 'second-page',
    children:[
     {
      title: 'Leaderboard',
     } ,
     {
      title: 'Notice board',
     } ,
     {
      title: 'Schedule',
     } 
    ]
  },
]
