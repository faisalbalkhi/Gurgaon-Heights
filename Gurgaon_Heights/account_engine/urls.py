from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('residential/', views.residential, name='residential'),
    path('commercial/', views.commercial, name='commercial'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]