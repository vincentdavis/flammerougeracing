from rest_framework import serializers

from apps.events.models import Races


class RacesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Races
        fields = '__all__'