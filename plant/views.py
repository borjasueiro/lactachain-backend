from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TemperatureSerializer, ReceptionSiloSerializer, FinalSiloSerializer, TransferSerializer, ChangesSerializer
from .models import Transfer, Temperature, ReceptionSilo, FinalSilo, Changes
from rest_framework.permissions import IsAuthenticated

class TransferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Transfer.objects.all().order_by('date')
    serializer_class = TransferSerializer

class TemperatureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer

class ReceptionSiloViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ReceptionSilo.objects.all().order_by('code')
    serializer_class = ReceptionSiloSerializer

class FinalSiloViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FinalSilo.objects.all().order_by('code')
    serializer_class = FinalSiloSerializer

class ChangesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Changes.objects.all().order_by('date')
    serializer_class = ChangesSerializer



    