from django.shortcuts import render
from rest_framework import viewsets, filters
from ertelecom.models import City, District, Street, House, Entrance
from . serializers import CitySerializer,DistrictSerializer,StreetSerializer,HouseSerializer, EntranceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet

class CitySetFilter(FilterSet):
    class Meta:
        model = City
        fields = '__all__'

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    model = City
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = CitySetFilter

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    model = District
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend,]
class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    model = Street
    serializer_class = StreetSerializer
    filter_backends = [DjangoFilterBackend,]
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    model = House
    serializer_class = HouseSerializer
    filter_backends = [DjangoFilterBackend,]
class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    model = Entrance
    serializer_class = EntranceSerializer
    filter_backends = [DjangoFilterBackend,]
