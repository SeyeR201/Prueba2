from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from. import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('products', views.products, name='products'),
    path('beyond', views.beyond, name='beyond'),
    path('conservas', views.conservas, name='conservas'),
    path('quesos', views.quesos, name='quesos'),
]