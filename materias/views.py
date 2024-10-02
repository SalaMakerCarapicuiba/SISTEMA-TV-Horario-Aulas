from django.shortcuts import render, get_object_or_404, redirect
from .models import Materia
from .forms import MateriaForm

def materia_list(request):
    materias = Materia.objects.all()
    return render(request, 'materias/materia_list.html', {'materias': materias})

def materia_create(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm()
    return render(request, 'materias/materia_form.html', {'form': form})

def materia_update(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materias/materia_form.html', {'form': form})

def materia_delete(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('materia_list')
    return render(request, 'materias/materia_confirm_delete.html', {'materia': materia})