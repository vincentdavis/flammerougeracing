import json

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters

from apps.FRRacing.api import serializers
from apps.FRRacing import models

def generate_fields(view, model, includeactions=False, defaultView=[]):
    try:

        defaultView = [{"value": field.name, "text": field.verbose_name, "is_default": True}  for field in
               model._meta.fields]
        return defaultView
    except Exception as e:
        print("Exception", str(e))
        return []

class TTTLeagueStandings(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.TTTLeagueStandings_S
    queryset = models.Tttleaguestandings.objects.all()
    filter_backends =[filters.OrderingFilter]
    filterset_fields = ()

    def get_queryset(self):
        return super().get_queryset().filter(leagueid='FRF.2')

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data['columns'] = generate_fields('', models.Tttleaguestandings, defaultView=['leagueteamname'])
        except Exception as e:
            print(str(e))
        return response

class Tttstageresrteam(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.Tttstageresrteam_S
    queryset = models.Tttstageresrteam.objects.all()


    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data['columns'] = generate_fields('', models.Tttstageresrteam, defaultView=['leagueteamname'])
        except Exception as e:
            print(str(e))
        return response

class Tttriderstats(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.Tttriderstats_S
    queryset = models.Tttriderstats.objects.all()


    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data['columns'] = generate_fields('', models.Tttriderstats, defaultView=['leagueteamname'])
        except Exception as e:
            print(str(e))
        return response

class Tttstagesegtsprint(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.Tttstagesegtsprint_S
    queryset = models.Tttstagesegtsprint.objects.all()


    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data['columns'] = generate_fields('', models.Tttstagesegtsprint, defaultView=['leagueteamname'])
        except Exception as e:
            print(str(e))
        return response