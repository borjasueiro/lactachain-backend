from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import F
from rest_framework import serializers

MIN_TEMP   = 0
MAX_TEMP   = 300

SILO_TYPE_CHOICES = (
    (1 , 'Storage'),
    (2 , 'Final'),
)
# Create your models here.

class ReceptionSilo(models.Model):
    code = models.AutoField(primary_key=True,blank=False, null=False, unique=True)
    def __str__(self):
        return str(self.code)
    class Meta:
        managed = True
        db_table = 'receptionsilo'

class Temperature(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(MIN_TEMP),
                                            MaxValueValidator(MAX_TEMP)])
    date = models.DateTimeField(default=timezone.now, editable=False)
    reception_silo = models.ForeignKey(
        'receptionsilo',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f'{self.value}'
    class Meta:
        managed = True
        db_table = 'temperature'   

class FinalSilo(models.Model):
    code = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    type = models.CharField(max_length=60, choices=SILO_TYPE_CHOICES, default='1')
    def __str__(self):
        return str(self.code)
    class Meta:
        managed = True
        db_table = 'finalsilo'

class Transfer(models.Model):
    code = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    date = models.DateTimeField(default=timezone.now)
    final_silo = models.ForeignKey(
        FinalSilo,
        on_delete=models.CASCADE,
    )
    reception_silo = models.ForeignKey(
        ReceptionSilo,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return str(self.code)

    class Meta:
        managed = True
        db_table = 'transfer'   

class Changes(models.Model):
    date = models.DateTimeField(default=timezone.now)
    silo_src = models.ForeignKey(
        FinalSilo,
        on_delete=models.CASCADE,
        related_name="silo_src"
    )
    silo_dst = models.ForeignKey(
        FinalSilo,
        on_delete=models.CASCADE,
        related_name="silo_dst"
    )
    def __str__(self):
        return f'Silo_src:{self.silo_src}\nSilo_dst:{self.silo_dst}'
    class Meta:
        managed = True
        db_table = 'changes'