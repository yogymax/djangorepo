from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from electornics.models import *
from electornics.serializers import *
from rest_framework.decorators import action

class ElectornicProducts(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer

class VendorProducts(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSer
