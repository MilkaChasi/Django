from django import forms
from .models import Autor

class Autorforms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'descripcion']