from django.contrib import admin
from .models import FinalSilo, ReceptionSilo, Temperature, Transfer, Changes
# Register your models here.
admin.site.register(FinalSilo)
admin.site.register(ReceptionSilo)
admin.site.register(Temperature)
admin.site.register(Transfer)
admin.site.register(Changes)