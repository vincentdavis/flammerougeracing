from typing import Any

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import GenericViewSet

from apps.events.api.pagination import StandardResultsSetPagination
from apps.events.api.serailizers import RaceSeriesSerializers, RaceSeriesSerializersReadOnly, RacesSerializers, \
    ZwiftResultSerializers
from apps.events.models import Races, RaceSeries, ZwiftResult
from django_filters.rest_framework import DjangoFilterBackend


def generate_fields(view, model, includeactions=False, defaultView=[]):
    try:
        defaultViewList = []

        for field in model._meta.fields:
            print(field.name in defaultView)
            if field.name in defaultView:
                defaultViewList.append({"value": field.name, "text": field.verbose_name, "is_default": True})
            else:
                defaultViewList.append({"value": field.name, "text": field.verbose_name, "is_default": False})

        return defaultViewList
    except Exception as e:
        print("Exception", str(e))
        return []

class RaceSeriesAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = RaceSeriesSerializersReadOnly
    queryset = RaceSeries.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return RaceSeriesSerializers
        return RaceSeriesSerializers


class RaceAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = RacesSerializers
    queryset = Races.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['race_series',]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return RacesSerializers
        return RacesSerializers


class ZwiftResultAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ZwiftResultSerializers
    queryset = ZwiftResult.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['zwift_id']

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ZwiftResultSerializers
        return ZwiftResultSerializers

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data['columns'] = generate_fields('', ZwiftResult, defaultView=['pos','name'])
        except Exception as e:
            print(str(e))
        return response



