from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('add/', views.doctor_create, name='doctor_create'),
]
