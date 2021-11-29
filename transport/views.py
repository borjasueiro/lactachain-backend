from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TransporterSerializer, TransportSerializer, MilkDeliverySerializer
from .models import Transporter, Transport, MilkDelivery
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class TransportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Transport.objects.all().order_by('car_registration')
    serializer_class = TransportSerializer

class TransporterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TransporterSerializer
    def get_queryset(self):
        """
        This view should return a list of all the transporter
        for the currently authenticated user.
        """
        queryset = Transporter.objects.all().order_by('name')
        nif = self.request.query_params.get('nif')
        if nif is not None:
            queryset = queryset.filter(nif=nif)
        return queryset

class MilkDeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MilkDelivery.objects.all().order_by('date')
    serializer_class = MilkDeliverySerializer