from django.shortcuts import render, redirect
from .forms import CourseForm

def cadastrar_curso(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_curso')  # Redireciona para uma página de sucesso (você pode personalizar)
    else:
        form = CourseForm()
    
    return render(request, 'courses/cadastrar_curso.html', {'form': form})