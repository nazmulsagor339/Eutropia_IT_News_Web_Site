

from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def index(request):

    cloth_one =Cloth.objects.all().order_by('id')
    cloth_two =Cloth.objects.all().order_by('id')

    device_one= Device.objects.all().order_by('id')
    device_two= Device.objects.all().order_by('id')

    jewellery_one=Jewellery.objects.all().order_by('id')
    jewellery_two=Jewellery.objects.all().order_by('id')
  
    context = {
        "cloth_one":cloth_one,
        "cloth_two":cloth_two,
    
        "device_one":device_one,
        "device_two":device_two,
        
        "jewellery_one":jewellery_one,
        "jewellery_two":jewellery_two,
    }
    return render(request, 'index.html', context)