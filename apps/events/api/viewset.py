from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.events.api.serailizers import RacesSerializers
from apps.events.models import Races


class RaceAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = RacesSerializers
    queryset = Races.objects.all()
