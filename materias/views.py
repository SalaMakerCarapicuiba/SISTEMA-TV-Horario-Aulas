from django.shortcuts import render, get_object_or_404, redirect

from turmas.models import Turma
from .models import Materia
from .forms import MateriaForm

def materia_list(request):
    materias = Materia.objects.all()
    return render(request, 'materias/materia_list.html', {'materias': materias})

def materia_update(request, turma_id, materia_id):
    turma = get_object_or_404(Turma, id=turma_id)
    
    # Se estamos editando uma matéria existente
    if materia_id:
        materia = get_object_or_404(Materia, id=materia_id)
    else:
        materia = None

    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia, turma=turma)
        if form.is_valid():
            form.save()
            return redirect('turma_edit', turma.id)
    else:
        form = MateriaForm(instance=materia, turma=turma)

    context = {
        'form': form,
        'turma': turma,
    }
    return render(request, 'materias/materia_form.html', context)

def materia_delete(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('materia_list')
    return render(request, 'materias/materia_confirm_delete.html', {'materia': materia})