from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Plant

# Create your views here.

def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant/plant_list.html', {'plants': plants})

class PlantCreateView(CreateView):
    model = Plant
    fields = ["name","price","description","image_url"]