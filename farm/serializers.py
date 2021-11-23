from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Farm, MilkCollection

class FarmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farm
        fields = ('code', 'province', 'town', 'name')

class MilkCollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MilkCollection
        fields = ('code', 'date', 'test', 'volumn','farm','transporter')

class ValidationErrorSerializer(serializers.Serializer):
    class Meta:
        model = ValidationError
