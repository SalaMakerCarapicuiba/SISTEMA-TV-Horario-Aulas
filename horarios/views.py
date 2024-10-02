from django.shortcuts import render, get_object_or_404, redirect
from .models import Horario
from .forms import HorarioForm

def horario_list(request):
    horarios = Horario.objects.all()
    return render(request, 'horarios/horario_list.html', {'horarios': horarios})

def horario_create(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horario_list')
    else:
        form = HorarioForm()
    return render(request, 'horarios/horario_form.html', {'form': form})

def horario_update(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return redirect('horario_list')
    else:
        form = HorarioForm(instance=horario)
    return render(request, 'horarios/horario_form.html', {'form': form})

def horario_delete(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        horario.delete()
        return redirect('horario_list')
    return render(request, 'horarios/horario_confirm_delete.html', {'horario': horario})