from django.shortcuts import render, get_object_or_404, redirect

from turmas.models import Turma
from .models import Materia
from .forms import MateriaForm

def materia_list(request):
    materias = Materia.objects.all()
    return render(request, 'materias/materia_list.html', {'materias': materias})

def materia_update(request, turma_id, materia_id):
    DIAS_DA_SEMANA = [
    (2, 'Segunda-feira'),
    (3, 'Terça-feira'),
    (4, 'Quarta-feira'),
    (5, 'Quinta-feira'),
    (6, 'Sexta-feira'),
    (7, 'Sábado'),
]
    
    turma = get_object_or_404(Turma, id=turma_id)
    
    # Se estamos editando uma matéria existente
    if materia_id:
        materia = get_object_or_404(Materia, id=materia_id)
    else:
        materia = None

    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia, turma=turma)

        if form.is_valid():
            sala = form.cleaned_data.get('sala')

            # Horários da matéria sendo editada
            horarios_novos = form.cleaned_data.get('horarios_por_dia')

            conflitos = []  # Lista para armazenar informações dos conflitos

            if sala:
                # Pega todas as matérias da sala, exceto a matéria que está sendo editada
                materias_da_sala = sala.materias.exclude(id=materia_id)
                
                # Verifica conflito de horários
                for materia_sala in materias_da_sala:
                    horarios_da_materia = materia_sala.horarios_por_dia

                    # Comparando dias e horários
                    for dia, horarios_novos_dia in horarios_novos.items():
                        if str(dia) in horarios_da_materia:  # Verifica se há matéria no mesmo dia
                            horarios_da_materia_dia = horarios_da_materia[str(dia)]

                            # Verificando se há sobreposição de horários
                            for horario_novo in horarios_novos_dia:
                                if horario_novo in horarios_da_materia_dia:
                                    conflitos.append({
                                        'materia': materia_sala.nome,
                                        'dia': dia,
                                        'horario': horario_novo
                                    })

            # Se houve conflitos, exibe a mensagem de erro
            if conflitos:
                mensagem_conflito = "Conflito(s) de horário encontrado(s): Já existe uma matéria para esta sala nesse horário e dia nessa sala\n"
                for conflito in conflitos:
                    dia_semana = dict(DIAS_DA_SEMANA).get(int(conflito['dia']))  # Traduz o número do dia para o nome
                    mensagem_conflito += f"- Matéria: {conflito['materia']}, Dia: {dia_semana}, Horário: {conflito['horario']}\n"
                
                form.add_error(None, mensagem_conflito)
            else:
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