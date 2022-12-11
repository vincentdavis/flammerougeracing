from rest_framework.routers import DefaultRouter
from apps.Setup.rest_api import viewset
router = DefaultRouter()

router.register('appbasic', viewset.AppBasicViewSet)  # App Settings
router.register('forms', viewset.FormsModelViewset)  # App Forms

# router.register('api/dropdownfields', viewset.DropDownFieldValuesViewset)  # App DropDown Fields

urlpatterns = router.urls
