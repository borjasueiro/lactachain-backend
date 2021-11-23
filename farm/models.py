from django.db import models
from django.utils import timezone
from transport.models import Transporter, Transport
from django.db.models import F
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

MIN_VOL    = 0
MAX_VOL    = 3000000

# Create your models here.
class Farm(models.Model):
    code = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    province = models.CharField(max_length=60)
    town = models.CharField(max_length=60)
    name = models.CharField(max_length=60, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'farm'

class MilkCollection(models.Model):
    code = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    date = models.DateTimeField(default=timezone.now, editable=False)
    test = models.BooleanField()
    volumn = models.IntegerField(validators=[MinValueValidator(MIN_VOL),
                                            MaxValueValidator(MAX_VOL)])  
    farm = models.ForeignKey(
        Farm,
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
        if (transport.current_volumn + self.volumn) > transport.capacity:
            raise serializers.ValidationError({'volumn': ('Volumn cannot be bigger than transport capacity addedd to current volumn')})
    def save(self, *args, **kwargs):
        self.full_clean()
        Transport.objects.filter(transporter=self.transporter.code,current=True).update(transporter=self.transporter.code,current=True,current_volumn=F('current_volumn') + self.volumn)
        return super(MilkCollection, self).save(*args, **kwargs)
    class Meta:
        managed = True
        db_table = 'milkcollection'