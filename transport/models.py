from django.db import models
from django.utils import timezone
from plant.models import ReceptionSilo
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import F
from rest_framework import serializers

MIN_VOL    = 0
MAX_VOL    = 3000000
MIN_TEMP   = 0
MAX_TEMP   = 300
# Create your models here.

class Transporter(models.Model):
    code = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField(max_length=60)
    nif = models.CharField(max_length=60, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'transporter'

class Transport(models.Model):
    car_registration = models.CharField(max_length=20,primary_key=True, blank=False, null=False, unique=True)
    tank_code = models.CharField(max_length=20)
    current = models.BooleanField(default=False)
    capacity = models.IntegerField(validators=[MinValueValidator(MIN_VOL),
                                            MaxValueValidator(MAX_VOL)])
    current_volumn = models.IntegerField(validators=[MinValueValidator(MIN_VOL),
                                            MaxValueValidator(MAX_VOL)], default=0,blank=True, editable=False)
    transporter = models.ForeignKey(
        Transporter,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f'CAR: {self.car_registration}\nTANK:{self.tank_code}'
    def clean(self):
        if self.current_volumn > self.capacity:
            raise serializers.ValidationError({'current_ volumn': ('Current volumn cannot be bigger than transport capacity')})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.current:
            Transport.objects.filter(transporter=self.transporter.code).update(current=False)
        return super(Transport, self).save(*args, **kwargs)
    class Meta:
        managed = True
        db_table = 'transport'
        unique_together = (('car_registration', 'tank_code'),)     

class MilkDelivery(models.Model):
    code = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    date = models.DateTimeField(default=timezone.now, editable=False)
    test = models.BooleanField()
    volumn = models.IntegerField(validators=[MinValueValidator(MIN_VOL),
                                            MaxValueValidator(MAX_VOL)]) 
    temperature = models.IntegerField(validators=[MinValueValidator(MIN_TEMP),
                                            MaxValueValidator(MAX_TEMP)])
    reception_silo = models.ForeignKey(
        ReceptionSilo,
        on_delete=models.CASCADE,
    )
    transporter = models.ForeignKey(
        Transporter,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return str(self.code)
    def clean(self):
        transport = Transport.objects.filter(transporter=self.transporter.code,current=True).first()
        if (transport.current_volumn - self.volumn) < 0:
            raise serializers.ValidationError({'volumn': ('Volumn cannot be bigger than transport current volumn')})
    def save(self, *args, **kwargs):
        self.full_clean()
        Transport.objects.filter(transporter=self.transporter.code,current=True).update(transporter=self.transporter.code,current_volumn=F('current_volumn') - self.volumn)
        return super(MilkDelivery, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'milkdelivery' 