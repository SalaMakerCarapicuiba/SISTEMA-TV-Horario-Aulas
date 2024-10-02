from django import forms
from .models import Materia

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nome', 'horario', 'semestre', 'dias_da_semana']