from rest_framework import serializers

from apps.events.models import Races


class RacesSerializers(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    def get_time(self,value):
        return ''
    class Meta:
        model = Races
        fields = '__all__'