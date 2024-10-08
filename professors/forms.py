from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        exclude = ['horas_atuais', 'cursos']

class ProfessorEditarForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'ra', 'max_horas', 'horas_atuais', 'materias']
        exclude = ['horas_atuais']
        widgets = {
            'materias': forms.CheckboxSelectMultiple(),  # Exibe as matérias como checkboxes
        }