from django.shortcuts import render
from account_engine.models import Property, Image
# Create your views here.

def index(request):
    return render(request, 'index.html')


def residential(request,):
    property = Property.objects.filter(property_type='R')
   
    return render(request, 'residential.html',{
       'property':property,
       
    })


def residential_Single_Listing(request,slug):
    property = Property.objects.get(slug=slug)

    return render(request, 'residential-Single-Listing.html',{
        'property': property,
    })


def commercial(request):
    property = Property.objects.filter(property_type='C')

    return render(request, 'commercial.html',{
        'property': property,
    })


def commercial_Single_Listing(request,slug):
    property = Property.objects.get(slug=slug)

    return render(request, 'commercial-Single-Listing.html',{
        'property':property
    })


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')





