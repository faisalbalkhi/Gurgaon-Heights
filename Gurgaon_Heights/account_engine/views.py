from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def residential(request):
    return render(request, 'residential.html')


def commercial(request):
    return render(request, 'commercial.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def career(request):
    return render(request, 'career.html')


def residential_Single_Listing(request):
    return render(request, 'residentialSingleListing.html')


def commercial_Single_Listing(request):
    return render(request, 'commercialSingleListing.html')