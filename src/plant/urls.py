from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path("add/", views.PlantCreateView.as_view(), name="PlantCreateView"),
]