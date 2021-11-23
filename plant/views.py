from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TemperatureSerializer, ReceptionSiloSerializer, FinalSiloSerializer, TransferSerializer, ChangesSerializer
from .models import Transfer, Temperature, ReceptionSilo, FinalSilo, Changes

class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all().order_by('date')
    serializer_class = TransferSerializer

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer

class ReceptionSiloViewSet(viewsets.ModelViewSet):
    queryset = ReceptionSilo.objects.all().order_by('code')
    serializer_class = ReceptionSiloSerializer

class FinalSiloViewSet(viewsets.ModelViewSet):
    queryset = FinalSilo.objects.all().order_by('code')
    serializer_class = FinalSiloSerializer

class ChangesViewSet(viewsets.ModelViewSet):
    queryset = Changes.objects.all().order_by('date')
    serializer_class = ChangesSerializer



    