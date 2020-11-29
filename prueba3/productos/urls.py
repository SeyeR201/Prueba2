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
    path('agregar',views.agregar, name='agregar'),
    path('agregar_productos',views.agregar_productos, name='agregar_productos'),
    path('eliminar',views.eliminar, name='eliminar'),
    path('eliminar_producto', views.eliminar_producto, name='eliminar_producto'),
    path('editar', views.editar, name='editar'),
    path('editar_producto', views.editar_producto, name='editar_producto'),
    path('editar_productos', views.editar_productos, name='editar_productos'),
    path('mostrar_productos', views.mostrar_productos, name='mostrar_productos'),
    path('mostrar_productos_ns', views.mostrar_productos_ns, name='mostrar_productos_ns'),
    path('listar', views.listar, name='listar'),
]