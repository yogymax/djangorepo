from rest_framework.serializers import ModelSerializer
from kidwear.models import *

class RainySeasonSer(ModelSerializer):
    class Meta:
        model = RainySeason
        fields = '__all__'

class VenSer(ModelSerializer):
    class Meta:
        model = Ven
        fields = '__all__'