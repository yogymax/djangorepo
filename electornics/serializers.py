from rest_framework.serializers import ModelSerializer
from electornics.models import *

class ProductSer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VendorSer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'