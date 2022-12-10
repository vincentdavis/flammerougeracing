from typing import Any

from django.db.models import QuerySet, Count, Sum, FloatField
from django.db.models.functions import Cast
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import GenericViewSet

from apps.events.api.pagination import StandardResultsSetPagination
from apps.events.api.serailizers import RaceSeriesSerializers, RaceSeriesSerializersReadOnly, RacesSerializers, \
    ZwiftResultSerializers, ZwiftResultSerializersMin
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

    @action(methods=['GET'], detail=True)
    def races(self, request, pk):
        obj = self.get_object()
        return Response(RacesSerializers(obj.races.all(), many=True).data)

    @action(methods=['GET'], detail=True, url_path='results/point_based')
    def points_based(self, request, pk):
        obj = self.get_object()
        return Response("Points")

    @action(methods=['GET'], detail=True, url_path='results/time_based')
    def time_based(self, request, pk):
        obj = self.get_object()
        zwift_id = obj.races.all().values_list('zwift_id')
        time_base_result = ZwiftResult.objects.filter(zwift_id__in=zwift_id).annotate(total_time=Sum(Cast('time_gun', FloatField()))).order_by('total_time').annotate(total_race_partipated=Count('zwift_id'))
        print(time_base_result.count())
        return Response(ZwiftResultSerializersMin(time_base_result, many=True).data)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return RaceSeriesSerializers
        return RaceSeriesSerializers


class RaceAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = RacesSerializers
    queryset = Races.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['race_series', ]

    @action(methods=['GET'], detail=True)
    def result(self, request,  pk):
        obj = self.get_object()
        return Response(ZwiftResultSerializers(ZwiftResult.objects.filter(zwift_id=obj.zwift_id), many=True).data)

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



