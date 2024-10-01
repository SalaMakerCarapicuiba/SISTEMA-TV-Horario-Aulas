from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import SelectCourseForm, EditCourseForm, CourseForm

def cadastrar_curso(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_curso')  # Redireciona para uma página de sucesso (você pode personalizar)
    else:
        form = CourseForm()
    
    return render(request, 'courses/cadastrar_curso.html', {'form': form})

def select_course_view(request):
    if request.method == 'POST':
        form = SelectCourseForm(request.POST)
        if form.is_valid():
            course_id = form.cleaned_data['course'].id
            return redirect('edit_course', course_id=course_id)
    else:
        form = SelectCourseForm()
    return render(request, 'courses/select_course.html', {'form': form})

def edit_course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirecione para a lista de cursos ou outra página apropriada
    else:
        form = EditCourseForm(instance=course)
    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})