from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('vista-administrador/', views.vista_administrador, name="vista_administrador"),
    path('contacto/', views.contacto, name="contacto"),
    path('menu/', views.menu, name="menu"),

    path('ingredientes', views.lista_ingredientes, name="ingredientes"),
    path('ingresar_ingredientes', views.ingresar_ingredientes, name="ingresar_ingredientes"),
    path('editar_ingredientes/<int:ingredientes_id>', views.editar_ingredientes, name='editar_ingredientes'),
    path('eliminar_ingredientes/<int:ingrediente_id>/', views.eliminar_ingredientes, name='eliminar_ingredientes'),

    path('masa', views.lista_tiposMasa, name="masa"),
    path('ingresar_masa', views.ingresar_masa, name="ingresar_masa"),
    path('editar_masa/<int:masa_id>/', views.editar_masa, name='editar_masa'),
    path('eliminar_masa/<int:masa_id>/', views.eliminar_masa, name='eliminar_masa'),
    
    path('tamanos', views.lista_tiposTamanos, name="tamanos"),
    path('ingresar_tamanos', views.ingresar_tamano, name="ingresar_tamanos"),
    path('editar_tamanos/<int:tamanos_id>/', views.editar_tamano, name='editar_tamanos'),
    path('eliminar_tamanos/<int:tamanos_id>/', views.eliminar_tamano, name='eliminar_tamanos'),

    path('pizza', views.lista_pizza, name="pizza"),
    path('ingresar_pizza', views.ingresar_pizza, name="ingresar_pizza"),
    path('editar_pizza/<int:pizza_id>/', views.editar_pizza, name='editar_pizza'),
    path('eliminar_pizza/<int:pizza_id>/', views.eliminar_pizza, name='eliminar_pizza'),

    path('detalle_pizza/<int:pizza_id>/', views.detalle_pizza, name='detalle_pizza'),

    path('registro/', views.registro, name="registro"),

]
