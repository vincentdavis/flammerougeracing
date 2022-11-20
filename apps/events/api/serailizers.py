from rest_framework import serializers

from apps.events.models import Races


class RacesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Races
        fields = '__all__'


class RacesSerializersReadOnly(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    start_date = serializers.DateField(format="%d %b %y")
    end_date = serializers.DateField(format="%d %b %y")

    def get_time(self, value):
        return ''

    class Meta:
        model = Races
        fields = '__all__'