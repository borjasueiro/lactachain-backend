from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TransporterSerializer, TransportSerializer, MilkDeliverySerializer
from .models import Transporter, Transport, MilkDelivery

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all().order_by('car_registration')
    serializer_class = TransportSerializer

class TransporterViewSet(viewsets.ModelViewSet):
    queryset = Transporter.objects.all().order_by('name')
    serializer_class = TransporterSerializer

class MilkDeliveryViewSet(viewsets.ModelViewSet):
    queryset = MilkDelivery.objects.all().order_by('date')
    serializer_class = MilkDeliverySerializer