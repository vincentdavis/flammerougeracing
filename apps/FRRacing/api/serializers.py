from rest_framework import serializers
from apps.FRRacing import models


class TTTLeagueStandings_S(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = models.Tttleaguestandings

class Tttstageresrteam_S(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = models.Tttstageresrteam

class Tttriderstats_S(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = models.Tttriderstats

class Tttstagesegtsprint_S(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = models.Tttstagesegtsprint