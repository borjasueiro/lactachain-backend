from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FarmSerializer, MilkCollectionSerializer
from .models import Farm, MilkCollection
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import logging
from django.shortcuts import get_object_or_404
from rest_framework import status

class FarmViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Farm.objects.all().order_by('name')
    serializer_class = FarmSerializer

class MilkCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MilkCollection.objects.all().order_by('date')
    serializer_class = MilkCollectionSerializer
    pagination_class = None
    filterset_fields = ['delivered']

    @action(detail=True, methods=['put'],url_path=r'update_status')
    def update_status(self,request,pk=None):
        model = get_object_or_404(MilkCollection, pk=pk)
        data = {"delivered": True }
        serializer = MilkCollectionSerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    