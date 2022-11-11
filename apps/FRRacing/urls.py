from django.contrib import admin
from django.urls import path
from apps.FRRacing.api import router

urlpatterns = [

]

urlpatterns += router.router.urls

