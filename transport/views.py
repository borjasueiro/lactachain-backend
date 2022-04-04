from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TransporterSerializer, TransportSerializer, MilkDeliverySerializer
from .models import Transporter, Transport, MilkDelivery
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.db.models import Q
from .filters import TransportFilter
import django_filters.rest_framework as filters

class TransportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    transporter = TransporterSerializer
    queryset = Transport.objects.all().order_by('car_registration')
    serializer_class = TransportSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TransportFilter
    pagination_class = None

class TransporterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Transporter.objects.all().order_by('name')
    serializer_class = TransporterSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['nif']

class MilkDeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MilkDelivery.objects.all().order_by('date')
    serializer_class = MilkDeliverySerializer
