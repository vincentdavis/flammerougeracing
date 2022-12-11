from django.urls import path
from . import (views)
from apps.Setup.rest_api import router
app_name = 'Setup'

urlpatterns = [
    # Views
    path('setupGuard', views.SetupGuard.as_view(), name='setup-guard'),
    path('setupInitial', views.Setupinitial.as_view(), name='setup-inital'),


]
# Api
urlpatterns += router.router.urls
