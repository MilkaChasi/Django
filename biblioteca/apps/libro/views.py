from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import Autor, Libro


class Inicio(TemplateView):
    template_name = 'libro/index.html'

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True) 

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = Autorforms
    success_url = reverse_lazy('libro:listar_autor')

class CrearAutor(CreateView):
    model = Autor
    form_class = Autorforms
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class EliminarAutor(DeleteView):
    model = Autor
    success_url = reverse_lazy('libro:listar_autor')

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')
    



class ListadoLibro(ListView):
    model = Libro 
    template_name = 'libro/libro/lista_libro.html'
    context_object_name = 'libros'
    queryset = Libro.objects.filter(estado = True)
     
class CrearLibro(CreateView):
    model = Libro
    form_class = Libroforms
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:lista_libro')

class ActualizarLibro(UpdateView):
    model = Libro
    template_name = 'libro/libro/crear_libro.html'
    form_class = Autorforms
    success_url = reverse_lazy('libro:lista_libro')

class EliminarLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy('libro:lista_libro')

    def post(self,request,pk,*args,**kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:lista_libro')