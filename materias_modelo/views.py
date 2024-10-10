from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course
from .models import Materia
from .forms import MateriaModeloForm

def materia_modelo_create(request, id):
    curso = get_object_or_404(Course, id=id)  # Obtém o curso pelo ID

    if request.method == 'POST':
        form = MateriaModeloForm(request.POST)
        if form.is_valid():
            materia = form.save()
            curso.materias.add(materia)  # Associa a matéria ao curso
            return redirect('course_edit', curso.id)  # Redireciona para a lista de MateriaModelo após a criação
    else:
        form = MateriaModeloForm()
    
    return render(request, 'materias_modelo/materias_modelo_create.html', {'form': form})

def materia_modelo_edit(request, id):
    materia = get_object_or_404(Materia, id=id)
    if request.method == "POST":
        form = MateriaModeloForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            courses = materia.course_set.all()  # Obtém todos os cursos associados à matéria
            if courses:
                return redirect('course_edit', courses[0].id)  # Redireciona para o primeiro curso associado
            else:
                return redirect('courses_list')  # Redireciona para a lista de cursos se não houver cursos associados
    else:
        form = MateriaModeloForm(instance=materia)
    return render(request, 'materias_modelo/materias_modelo_edit.html', {'form': form})

def materia_modelo_delete(request, id):
    materia = get_object_or_404(Materia, id=id)
    course = materia.course_set.all()[0]  # Obtém todos os cursos associados à matéria
    if request.method == "POST":
        materia.delete()
        if course:
            return redirect('course_edit', course.id)  # Redireciona para o primeiro curso associado
        else:
            return redirect('courses_list')  # Redireciona para a lista de cursos se não houver cursos associados
    return render(request, 'materias_modelo/materia_modelo_confirm_delete.html', {'materia': materia})