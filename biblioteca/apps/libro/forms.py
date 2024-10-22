from django import forms
from .models import Autor, Libro

class Autorforms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'descripcion']
        labels = {
            'nombre': 'Nombre del Autor',
            'apellido': 'Apellido del Autor',
            'nacionalidad': 'Nacionalidad del Autor',
            'descripcion': 'Pequeña descripción'
        }
        widgets = {
            'nombre' : forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor'
                }
            ),
            'apellido' : forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del autor'
                }
            ),
            'nacionalidad' : forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese la nacionalidad del autor'
                }
            ), 
            'descripcion' : forms.Textarea(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese una pequeña descripción sobre el autor'
                }
            )          
        }



class Libroforms(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'autor_id']
        labels = {
            'titulo': 'Título del Libro',
            'fecha_publicacion': 'Fecha de publicación del libro',
            'autor': 'Nombre del Autor',
        }
        widgets = {
            'titulo' : forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el título del libro'
                }
            ),
            'fecha_publicacion' : forms.SelectDateWidget(

            ),
             'autor_id' : forms.SelectMultiple(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor'
                }
            ),

        }
    