from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.areas.models import Area
from apps.api.areas.serializers import AreaSerializer

# Métodos para los endpoints del crud de Areas
class AreasViewSet(ViewSet):
    def list(self, request):
        serializer = AreaSerializer(Area.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk:int):
        try:
            area = AreaSerializer(Area.objects.get(pk=pk))
            return Response(status=status.HTTP_200_OK, data=area.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})

    def create(self, request):
        try:
            serializer = AreaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            print(request.data)
            return Response(status=status.HTTP_404_NOT_FOUND, data=request.data)
    
    def update(self, request, pk:int):
        try:
            serializer = AreaSerializer(Area.objects.get(pk=pk), data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})

    def destroy(self, request, pk:int):
        try:
            area = Area.objects.get(pk=pk)
            area.delete()
            return Response(status=status.HTTP_202_ACCEPTED, data={"mensaje": "Eliminado correctamente"})
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})
