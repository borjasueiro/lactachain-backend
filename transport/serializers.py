from rest_framework import serializers

from .models import Transport, Transporter, MilkDelivery
class TransportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transport
        fields = ('car_registration', 'tank_code', 'current_volumn', 'current', 'capacity', 'transporter')

class TransporterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transporter
        fields = ('code', 'name','nif')

class MilkDeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MilkDelivery
        fields = ('code', 'date', 'test', "volumn",'reception_silo','temperature','transporter')