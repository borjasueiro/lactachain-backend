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
    pagination_class = None

class FinalSiloViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FinalSilo.objects.all().order_by('code')
    serializer_class = FinalSiloSerializer
    pagination_class = None

class ChangesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Changes.objects.all().order_by('date')
    serializer_class = ChangesSerializer


class ExceptionLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.body)
        print(request.scheme)
        print(request.method)
        print(request.META)

        response = self.get_response(request)

        return response
    