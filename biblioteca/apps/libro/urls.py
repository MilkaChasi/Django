from django.urls import path, re_path
from .views import crearAutor,Home, listarAutor, editarAutor, eliminarAutor

urlpatterns = [
   path('', Home, name='home'), 
   path('crear_autor/', crearAutor, name = 'crear_autor'),
   path('listar_autor/', listarAutor, name = 'listar_autor'),
   path('editar_autor/<int:id>', editarAutor, name = 'editar_autor'),
   path('eliminar_autor/<int:id>', eliminarAutor, name = 'eliminar_autor'),


]