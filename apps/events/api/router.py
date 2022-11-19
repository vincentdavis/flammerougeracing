from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.events.api.viewset import RacesVieSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("races", RacesVieSet)

urlpatterns = router.urls
