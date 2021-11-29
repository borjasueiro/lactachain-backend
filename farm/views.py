from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FarmSerializer, MilkCollectionSerializer
from .models import Farm, MilkCollection
from rest_framework.permissions import IsAuthenticated

class FarmViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Farm.objects.all().order_by('name')
    serializer_class = FarmSerializer

class MilkCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MilkCollection.objects.all().order_by('date')
    serializer_class = MilkCollectionSerializer




    