from typing import Any

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import GenericViewSet

from apps.events.api.serailizers import RacesSerializers, RacesSerializersReadOnly
from apps.events.models import Races


class RaceAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = RacesSerializersReadOnly
    queryset = Races.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return RacesSerializers
        return RacesSerializersReadOnly


