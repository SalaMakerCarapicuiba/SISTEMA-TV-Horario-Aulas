from django import forms
from .models import Sala

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['numero', 'materias']
        # exclude = ['materias']
        widgets = {
              'numero': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
                'placeholder': 'Ex: 101'
            }),
             'materias': forms.CheckboxSelectMultiple(attrs={
                'class': 'space-y-2 text-custom1',
            }),
            }