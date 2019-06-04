from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='location'),
    path('<int:destination_id>', views.city, name='destination'), 
]