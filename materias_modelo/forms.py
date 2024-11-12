from django import forms
from .models import Materia

class MateriaModeloForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nome', 'semestre']  # Substitua pelos campos reais do seu modelo
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
                'placeholder': 'Ex: Estatística Aplicada'
            }),
            'semestre': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
                'placeholder': 'Ex: 1'
            }),
        }