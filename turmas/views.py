from django.shortcuts import render, get_object_or_404, redirect
from .models import Turma
from .forms import TurmaForm

def turma_list(request):
    turmas = Turma.objects.all()
    return render(request, 'turmas/turma_list.html', {'turmas': turmas})

def turma_create(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turma_list')
    else:
        form = TurmaForm()
    return render(request, 'turmas/turma_form.html', {'form': form})

def turma_update(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('turma_list')
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'turmas/turma_form.html', {'form': form})

def turma_delete(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        turma.delete()
        return redirect('turma_list')
    return render(request, 'turmas/turma_confirm_delete.html', {'turma': turma})