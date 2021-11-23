from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'transfer', views.TransferViewSet)
router.register(r'temperature', views.TemperatureViewSet)
router.register(r'receptionsilo', views.ReceptionSiloViewSet)
router.register(r'finalsilo', views.FinalSiloViewSet)
router.register(r'changes', views.ChangesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]