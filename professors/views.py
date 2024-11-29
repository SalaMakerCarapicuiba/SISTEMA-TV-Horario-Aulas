from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProfessorEditarForm, ProfessorForm
from django.contrib.auth.decorators import login_required
from .models import Professor
from django.contrib import messages
from materias.models import Materia

#@login_required
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

#@login_required
def listar_professores(request):
    professores = Professor.objects.all()
    return render(request, 'professors/listar_prof.html', {'professores': professores})

#@login_required
def deletar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)

    professor.delete()
    messages.success(request, f"O professor {professor.nome} foi deletado com sucesso.")
    return redirect('listar_professores')

def detalhes_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    materias = Materia.objects.filter(professor_id=professor.id)

    return render(request, 'professors/detalhes_professor.html', {'professor': professor, 'materias': materias})

def editar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)  # Pega o professor pelo id\

    if request.method == 'POST':
        form = ProfessorEditarForm(request.POST, instance=professor)  # Preenche o form com os dados submetidos
        if form.is_valid():
            form.save()  # Salva as mudanças no banco de dados
            return redirect('detalhes_professor', id=professor.id)  # Redireciona para os detalhes do professor
    else:
        form = ProfessorForm(instance=professor)  # Preenche o form com os dados do professor para edição
    return render(request, 'professors/editar_professor.html', {'form': form, 'professor': professor})