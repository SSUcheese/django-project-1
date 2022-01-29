from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('greetings/', views.greetings),
    path('', views.index),
    path('food/<str:menu>/', views.detail),
]