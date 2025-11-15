from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'home'),
    path('doctors/', views.doctors_list, name="doctors-list"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
