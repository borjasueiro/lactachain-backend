import django_filters

from .models import Transporter,Transport


class TransportFilter(django_filters.FilterSet):
    transporter = django_filters.NumberFilter(field_name='transporter__code')

    class Meta:
        model = Transport
        fields = ['transporter']