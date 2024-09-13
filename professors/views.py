from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProfessorForm
from django.contrib.auth.decorators import login_required
from .models import Professor
from django.contrib import messages

@login_required
def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"O professor foi incluido com sucesso.")
            return redirect('listar_professores') 
    else:
        form = ProfessorForm()
    
    return render(request, 'professors/cadastrar_prof.html', {'form': form})

@login_required
def listar_professores(request):
    professores = Professor.objects.all()
    return render(request, 'professors/listar_prof.html', {'professores': professores})

@login_required
def deletar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)

    professor.delete()
    messages.success(request, f"O professor {professor.nome} foi deletado com sucesso.")
    return redirect('listar_professores')
