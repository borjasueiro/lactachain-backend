from rest_framework import serializers

from .models import Changes, Transfer, Temperature, ReceptionSilo, FinalSilo, Changes

class TransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = ('code','date', "reception_silo", 'final_silo')

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ('value', 'date', "reception_silo")

class ReceptionSiloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReceptionSilo
        fields = '__all__'

class FinalSiloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FinalSilo
        fields = ('code', 'type')

class ChangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Changes
        fields = ('date', 'silo_src', 'silo_dst')