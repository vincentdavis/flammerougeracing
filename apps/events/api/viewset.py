from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.events.api.serailizers import RacesSerializers
from apps.events.models import Races


class RacesVieSet(RetrieveModelMixin,CreateModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = RacesSerializers
    queryset = Races.objects.all()
