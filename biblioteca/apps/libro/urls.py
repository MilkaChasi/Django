from django.urls import path, re_path
from .views import *

urlpatterns = [
 
   path('crear_autor/', CrearAutor.as_view() , name = 'crear_autor'),
   path('listar_autor/', ListadoAutor.as_view(), name = 'listar_autor'),
   path('editar_autor/<int:pk>', ActualizarAutor.as_view(), name = 'editar_autor'),
   path('eliminar_autor/<int:pk>', EliminarAutor.as_view(), name = 'eliminar_autor'),



   path('lista_libro/', ListadoLibro.as_view(), name = 'lista_libro'),
   path('crear_libro/', CrearLibro.as_view() , name = 'crear_libro'),
   path('editar_libro/<int:pk>', ActualizarLibro.as_view(), name = 'editar_libro'),
   path('eliminar_libro/<int:pk>', EliminarLibro.as_view(), name = 'eliminar_libro'),



]