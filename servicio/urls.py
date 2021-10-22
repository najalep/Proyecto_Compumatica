"""
    Urls de la aplicacion servicio
"""
from django.urls import path
from servicio.views import views
from servicio.views.cliente.views import *
from servicio.views.area.views import *
from servicio.views.empleado.views import *
from servicio.views.categoria.views import *
from servicio.views.marca.views import *
from servicio.views.articulo.views import *
from servicio.views.factura.views import *

urlpatterns = [

    path('index/', views.index , name="index"),

    #Urls de clientes
    path('client/list/',ClientListView.as_view(),name='client_list'),
    path('client/add/',ClientCreateView.as_view(),name='client_create'),
    path('client/edit/<int:pk>/',ClientUpdateView.as_view(),name='client_update'),
    path('client/dele/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    #Urls de Area
    path('area/list/',AreaListView.as_view(),name='area_list'),
    path('area/add/',AreaCreateView.as_view(),name='area_create'),
    path('area/edit/<int:pk>/',AreaUpdateView.as_view(),name='area_update'),
    path('area/dele/<int:pk>/', AreaDeleteView.as_view(), name='area_delete'),

    #Urls de Empleado
    path('empleado/list/',EmpleadoListView.as_view(),name='empleado_list'),
    path('empleado/add/',EmpleadoCreateView.as_view(),name='empleado_create'),
    path('empleado/edit/<int:pk>/',EmpleadoUpdateView.as_view(),name='empleado_update'),
    path('empleado/dele/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),

    #Urls de categoria
    path('categoria/list/',CategoriaListView.as_view(),name='categoria_list'),
    path('categoria/add/',CategoriaCreateView.as_view(),name='categoria_create'),
    path('categoria/edit/<int:pk>/',CategoriaUpdateView.as_view(),name='categoria_update'),
    path('categoria/dele/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),

    #Urls de Marca
    path('marca/list/',MarcaListView.as_view(),name='marca_list'),
    path('marca/add/',MarcaCreateView.as_view(),name='marca_create'),
    path('marca/edit/<int:pk>/',MarcaUpdateView.as_view(),name='marca_update'),
    path('marca/dele/<int:pk>/', MarcaDeleteView.as_view(), name='marca_delete'),

    #Urls de Articulo
    path('articulo/list/',ArticuloListView.as_view(),name='articulo_list'),
    path('articulo/add/',ArticuloCreateView.as_view(),name='articulo_create'),
    path('articulo/edit/<int:pk>/',ArticuloUpdateView.as_view(),name='articulo_update'),
    path('articulo/dele/<int:pk>/', ArticuloDeleteView.as_view(), name='articulo_delete'),

    #Urls de Factura
    path('factura/add/', FacturaCreateView.as_view(), name='factura_create'),

]


















