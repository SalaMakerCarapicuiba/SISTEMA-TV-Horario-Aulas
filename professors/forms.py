from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        exclude = ['horas_atuais', 'cursos']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'border border-custom5 p-2 rounded w-full bg-transparent text-custom5',
                'placeholder': 'Ex: Carlos Alberto De Nobrega'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-custom5 p-2 rounded w-full bg-transparent text-custom5',
                'placeholder': 'Ex: carlos.nobrega@fatec.sp.gov.br'
            }),
            'ra': forms.TextInput(attrs={
                'class': 'border border-custom5 p-2 rounded w-full bg-transparent text-custom5',
                'placeholder': 'Ex: 42345-342'
            }),
            'disciplina': forms.Select(attrs={
                'class': 'border border-custom5 p-2 rounded w-full bg-transparent text-custom5',
            }),
            'max_horas': forms.Select(attrs={
                'class': 'border border-custom5 p-2 rounded w-full bg-transparent text-custom5',
            }),
        }

class ProfessorEditarForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'ra', 'max_horas', 'horas_atuais', 'materias']
        exclude = ['horas_atuais']
        widgets = {
            'materias': forms.CheckboxSelectMultiple(),  # Exibe as matérias como checkboxes
        }