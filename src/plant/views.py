from django.shortcuts import render
from .models import Plant

# Create your views here.

def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant/plant_list.html', {'plants': plants})