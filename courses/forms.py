from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['nome','professor_coordenador']

class SelectCourseForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Selecione um Curso")

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['nome','professor_coordenador']