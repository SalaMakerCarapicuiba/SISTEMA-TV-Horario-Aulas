from django import forms
from .models import Materia

class MateriaModeloForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nome', 'semestre']  # Substitua pelos campos reais do seu modelo