from django import forms
from .models import Turma

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'semestre', 'periodo']  # Adicione ou remova campos conforme necessário
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
                'placeholder': 'Ex: AMS'
            }),
            'semestre': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
                'min': 1
            }),
            'periodo': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
            }),

        }
