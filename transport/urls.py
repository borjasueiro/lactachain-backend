from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'transport', views.TransportViewSet)
router.register(r'transporter', views.TransporterViewSet, basename='Transporter')
router.register(r'milkdelivery', views.MilkDeliveryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]