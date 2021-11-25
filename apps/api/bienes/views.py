from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.bienes.models import Bienes
from apps.api.bienes.serializers import BienesSerializer


class BienesViewSet(ViewSet):
    def list(self, request):
        serializer = BienesSerializer(Bienes.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk:int):
        try:
            bien = BienesSerializer(Bienes.objects.get(pk=pk))
            return Response(status=status.HTTP_200_OK, data=bien.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})

    def create(self, request):
        serializer = BienesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def update(self, request, pk:int):
        try:
            serializer = BienesSerializer(Bienes.objects.get(pk=pk), data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})

    def destroy(self, request, pk:int):
        try:
            bien = Bienes.objects.get(pk=pk)
            bien.delete()
            return Response(status=status.HTTP_202_ACCEPTED, data={"mensaje": "Eliminado correctamente"})
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})
