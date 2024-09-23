from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from django.contrib.auth.views import LoginView
from ertelecom.views import CityViewSet,DistrictViewSet, StreetViewSet,HouseViewSet, EntranceViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register(r'city', CityViewSet),
router.register(r'district', DistrictViewSet),
router.register(r'street', StreetViewSet),
router.register(r'house', HouseViewSet),
router.register(r'entrance', EntranceViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
