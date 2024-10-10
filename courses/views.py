from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import SelectCourseForm, EditCourseForm, CourseForm

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses_list')  # Redireciona para uma página de sucesso (você pode personalizar)
    else:
        form = CourseForm()
    
    return render(request, 'courses/course_create.html', {'form': form})

def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses_list')  # Redirecione para a lista de cursos ou outra página apropriada
    else:
        form = EditCourseForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form, 'course': course})

def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses_list')  # Redirecionar para a lista de cursos ou outra página de sucesso
    return render(request, 'course_delete_confirm.html', {'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})