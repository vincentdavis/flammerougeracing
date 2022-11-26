from rest_framework import serializers

from apps.events.models import Races, RaceSeries, ZwiftResult


class RaceSeriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = RaceSeries
        fields = '__all__'


class ZwiftResultSerializers(serializers.ModelSerializer):
    zwift_id = serializers.IntegerField(required=False)
    time = serializers.SerializerMethodField(method_name="set_empty")
    height = serializers.SerializerMethodField(method_name="set_empty")
    max_hr = serializers.SerializerMethodField(method_name="set_empty")
    hrmax = serializers.SerializerMethodField(method_name="set_empty")
    weight = serializers.SerializerMethodField(method_name="set_empty")
    np = serializers.SerializerMethodField(method_name="set_empty")
    hrr = serializers.SerializerMethodField(method_name="set_empty")
    hreff = serializers.SerializerMethodField(method_name="set_empty")
    avg_power = serializers.SerializerMethodField(method_name="set_empty")
    avg_wkg = serializers.SerializerMethodField(method_name="set_empty")
    wkg_ftp = serializers.SerializerMethodField(method_name="set_empty")
    wftp = serializers.SerializerMethodField(method_name="set_empty")
    wkg1200 = serializers.SerializerMethodField(method_name="set_empty")
    wkg300 = serializers.SerializerMethodField(method_name="set_empty")
    wkg120 = serializers.SerializerMethodField(method_name="set_empty")
    wkg60 = serializers.SerializerMethodField(method_name="set_empty")
    wkg5 = serializers.SerializerMethodField(method_name="set_empty")
    w1200 = serializers.SerializerMethodField(method_name="set_empty")
    w300 = serializers.SerializerMethodField(method_name="set_empty")
    w120 = serializers.SerializerMethodField(method_name="set_empty")
    w60 = serializers.SerializerMethodField(method_name="set_empty")
    w30 = serializers.SerializerMethodField(method_name="set_empty")
    w15 = serializers.SerializerMethodField(method_name="set_empty")
    w5 = serializers.SerializerMethodField(method_name="set_empty")
    info_notes = serializers.SerializerMethodField(method_name="set_empty")
    avg_hr = serializers.SerializerMethodField(method_name="set_empty")
    wkg15 = serializers.SerializerMethodField(method_name="set_empty")
    wkg30 = serializers.SerializerMethodField(method_name="set_empty")
    def set_empty(self, value):
        return  ""
    class Meta:
        model = ZwiftResult
        fields = '__all__'


class RaceSeriesSerializersReadOnly(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    start_date = serializers.DateField(format="%d %b %y")
    end_date = serializers.DateField(format="%d %b %y")

    def get_time(self, value):
        return ''

    class Meta:
        model = RaceSeries
        fields = '__all__'

class RacesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Races
        fields = '__all__'