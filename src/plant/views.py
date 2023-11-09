from django.shortcuts import render

# Create your views here.

def plant_list(request):
    return render(request, 'plant/plant_list.html', {})