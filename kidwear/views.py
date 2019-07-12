from rest_framework.viewsets import ModelViewSet
from kidwear.models import *
from kidwear.serializers import *
from rest_framework.response import Response
from rest_framework import status

class ClothProducts(ModelViewSet):
    queryset = RainySeason.objects.all()
    serializer_class = RainySeasonSer

class VenProducts(ModelViewSet):
    queryset = Ven.objects.all()
    serializer_class =VenSer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.active=='Yes':
            serializer = self.get_serializer(instance)

        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active='No'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
