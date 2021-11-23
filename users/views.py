from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UsersSerializer
from .models import Users


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('nif')
    serializer_class = UsersSerializer




    