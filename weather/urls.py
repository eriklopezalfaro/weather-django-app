from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('city-name', views.city_name, name='city_name'),

]
