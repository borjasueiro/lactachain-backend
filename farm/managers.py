from django.db import models
from django.db.models import Q
from transport.models import Transporter, Transport



class MilkCollectionQuerySet(models.query.QuerySet):
  def get_by_capacity(self,code):
    transport = Transport.objects.filter(transporter=code,current=True).first()
    return self.filter(volumn=transport.capacity)

  def get_by_nif(self):
    return self.order_by('nif')

class MilkCollectionManager(models.Manager):

  def get_queryset(self):
    return MilkCollectionQuerySet(self.model, using=self._db)

  def get_by_capacity(self,code):
    return self.get_queryset().get_by_capacity(code)

  def get_by_nif(self):
    return self.get_queryset().get_by_nif()