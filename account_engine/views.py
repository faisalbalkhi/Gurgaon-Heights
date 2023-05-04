from django.shortcuts import render
from account_engine.models import Property
# Create your views here.

def index(request):
    return render(request, 'index.html')


def residential(request):
    residential = Property.objects.filter(property_type='R')

    return render(request, 'residential.html',{
       'residential':residential ,
    })


def commercial(request):
    commercial = Property.objects.filter(property_type='C')

    return render(request, 'commercial.html',{
        'commercial': commercial,
    })


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def residential_Single_Listing(request,slug):
    residential_single_list = Property.objects.get(slug=slug)
    
    return render(request, 'residential-Single-Listing.html',{
        'residential_single_list':residential_single_list
    })


def commercial_Single_Listing(request):
    return render(request, 'commercial-Single-Listing.html')