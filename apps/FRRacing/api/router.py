from rest_framework.routers import DefaultRouter
from apps.FRRacing.api import viewset

router = DefaultRouter()
router.register('TTTLeagueStandings',viewset.TTTLeagueStandings )
router.register('Tttstageresrteam',viewset.Tttstageresrteam )
router.register('Tttriderstats',viewset.Tttriderstats )
router.register('Tttstagesegtsprint',viewset.Tttstagesegtsprint )