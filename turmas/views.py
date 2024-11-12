from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from courses.models import Course
from turmas.forms import TurmaForm
from .models import Turma

def turma_create(request, course_id):
    curso = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.curso = curso  # Associando o curso à turma
            turma.save()
            return redirect('course_edit', curso.id)  # Redirecionar após criar
    else:
        form = TurmaForm()
    return render(request, 'turmas/turma_create.html', {'form': form, 'curso': curso})

def turma_edit(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('course_edit', turma.curso.id)  # Redirecionar após editar
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'turmas/turma_edit.html', {'form': form, 'curso': turma.curso, 'turma': turma})

def turma_delete(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    if request.method == 'POST':
        curso_id = turma.curso.id
        turma.delete()
        return redirect('course_edit', curso_id)  # Redirecionar após deletar
    # return render(request, 'turmas/turma_confirm_delete.html', {'turma': turma})
    return redirect('courses_list')

def turma_list(request):
    turmas = Turma.objects.all()
    # Obtendo o course_id de uma turma caso exista ao menos uma
    course_id = turmas.first().curso.id if turmas.exists() else None
    return render(request, 'turmas/turma_list.html', {'turmas': turmas, 'course_id': course_id})
