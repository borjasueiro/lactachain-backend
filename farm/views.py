from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FarmSerializer, MilkCollectionSerializer
from .models import Farm, MilkCollection

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all().order_by('name')
    serializer_class = FarmSerializer

class MilkCollectionViewSet(viewsets.ModelViewSet):
    queryset = MilkCollection.objects.all().order_by('date')
    serializer_class = MilkCollectionSerializer




    