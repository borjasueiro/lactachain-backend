from django.contrib import admin
from .models import MilkDelivery, Transporter, Transport
# Register your models here.
admin.site.register(MilkDelivery)
admin.site.register(Transport)
admin.site.register(Transporter)