from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['nome','professor_coordenador']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
            }),
            'professor_coordenador': forms.Select(attrs={
               'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400',
            })
        }

class SelectCourseForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Selecione um Curso")

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['nome','professor_coordenador']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'min-w-full flex-1 p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400'
            }),
            'professor_coordenador': forms.Select(attrs={
               'class': 'min-w-full flex-1 p-2 border border-gray-300 rounded-lg bg-transparent text-custom1 placeholder-gray-400'  
            })
        }