from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('residential/', views.residential, name='residential'),
    path('commercial/', views.commercial, name='commercial'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('residential-Single-Listing/', views.residential_Single_Listing, name='residential_Single_Listing'),
    path('commercial-Single-Listing/', views.commercial_Single_Listing, name='commercial_Single_Listing'),
]