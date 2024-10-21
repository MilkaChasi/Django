from django import forms
from .models import Autor

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