from django.shortcuts import render, redirect
from .forms import ProfessorForm

def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_professor')  # Redireciona para uma página de sucesso (você pode personalizar)
    else:
        form = ProfessorForm()
    
    return render(request, 'professors/cadastrar_prof.html', {'form': form})