import django_filters 
from .models import *

class DestinationsFilter(django_filters.FilterSet):
    class Meta:
        model = Destinations
        fields = '__all__'