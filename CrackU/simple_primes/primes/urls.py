from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.input.as_view(),name='input'),
    path('primes', views.output.as_view(),name='output'),
]
